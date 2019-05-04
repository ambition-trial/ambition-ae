import inflect

from edc_constants.constants import OTHER, YES
from edc_reports import Report
from reportlab.lib import colors
from reportlab.lib.units import cm
from reportlab.platypus.flowables import Spacer
from reportlab.platypus.para import Paragraph
from reportlab.platypus.tables import Table, TableStyle
from textwrap import fill
from edc_registration.models import RegisteredSubject
from edc_utils.age import formatted_age
from ambition_rando.models.randomization_list import RandomizationList
from reportlab.lib.pagesizes import A4
from django.contrib.auth import get_user_model
from django.core.exceptions import ObjectDoesNotExist
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER

User = get_user_model()
p = inflect.engine()


class AEReport(Report):

    default_page = dict(
        rightMargin=0.5 * cm,
        leftMargin=1.0 * cm,
        topMargin=1.5 * cm,
        bottomMargin=1.5 * cm,
        pagesize=A4,
    )

    def __init__(self, ae_initial=None, **kwargs):
        self.ae_initial = ae_initial
        self.registered_subject = RegisteredSubject.objects.get(
            subject_identifier=self.ae_initial.subject_identifier
        )
        self.drug_assignment = RandomizationList.objects.get(
            subject_identifier=self.ae_initial.subject_identifier
        ).get_drug_assignment_display()
        self.bg_cmd = ("BACKGROUND", (0, 0), (0, -1), colors.lightgrey)
        super().__init__(**kwargs)

    @property
    def row_data(self):

        classification_text = fill(
            self.ae_initial.get_ae_classification_display(), width=80
        )
        if self.ae_initial.ae_classification == OTHER:
            classification_text = fill(
                f"{classification_text}: {self.ae_initial.ae_classification_other}",
                width=80,
            )

        sae_reason = (
            fill(f": {self.ae_initial.get_sae_reason_display()}", width=80)
            if self.ae_initial.sae == YES
            else ""
        )
        sae_text = f"{self.ae_initial.get_sae_display()}{sae_reason}"

        susar_reported = ""
        if self.ae_initial.susar == YES:
            susar_reported = (
                ": reported"
                if self.ae_initial.susar_reported == YES
                else ": not reported"
            )
        susar_text = f"{self.ae_initial.get_susar_display()}{susar_reported}"

        return [
            [
                [
                    "Report date:",
                    self.ae_initial.report_datetime.strftime("%Y-%m-%d %H:%M"),
                ],
                [
                    "Awareness date:",
                    self.ae_initial.ae_awareness_date.strftime("%Y-%m-%d"),
                ],
                [
                    "Actual start date:",
                    self.ae_initial.ae_start_date.strftime("%Y-%m-%d"),
                ],
                ["Classification:", classification_text],
                ["Severity:", self.ae_initial.get_ae_grade_display()],
                ["SAE:", sae_text],
                ["SUSAR:", susar_text],
            ]
        ]

    @property
    def title(self):
        return f"ADVERSE EVENT REPORT FOR {self.ae_initial.subject_identifier}"

    def get_report_story(self, **kwargs):

        story = []

        story.append(Paragraph(self.title, self.styles["line_label_center"]))

        age = formatted_age(
            self.registered_subject.dob, reference_dt=self.ae_initial.report_datetime
        )
        rows = [
            [["Subject:", self.ae_initial.subject_identifier]],
            [["Gender/Age:", f"{self.registered_subject.get_gender_display()} {age}"]],
            [
                [
                    "Study site:",
                    f"{self.registered_subject.site.id}: {self.registered_subject.site.name.title()}",
                ]
            ],
            [
                [
                    "Randomization date:",
                    self.registered_subject.randomization_datetime.strftime(
                        "%Y-%m-%d %H:%M"
                    ),
                ]
            ],
            [["Assignment:", fill(self.drug_assignment, width=80)]],
        ]
        for row in rows:
            t = Table(row, (4 * cm, 14 * cm))
            self.set_table_style(t, bg_cmd=self.bg_cmd)
            t.hAlign = "LEFT"
            story.append(t)

        story.append(Spacer(0.1 * cm, 0.5 * cm))
        story.append(Spacer(0.1 * cm, 0.5 * cm))

        t = Table([["Section 1: Initial AE Report"]], (18 * cm))
        self.set_table_style(t, bg_cmd=self.bg_cmd)
        story.append(t)
        t = Table([[f"Prepared by {self.get_user(self.ae_initial)}."]], (18 * cm))
        self.set_table_style(t)
        story.append(t)

        story.append(Spacer(0.1 * cm, 0.5 * cm))

        # basics
        for row in self.row_data:
            t = Table(row, (4 * cm, 14 * cm))
            self.set_table_style(t, bg_cmd=self.bg_cmd)
            t.hAlign = "LEFT"
            story.append(t)

        story.append(Spacer(0.1 * cm, 0.5 * cm))

        # Description
        t = Table([["Description of AE:"]], (18 * cm))
        self.set_table_style(t, bg_cmd=self.bg_cmd)
        story.append(t)
        t = Table([[fill(self.ae_initial.ae_description, width=100)]], (18 * cm))
        self.set_table_style(t)
        story.append(t)

        story.append(Spacer(0.1 * cm, 0.5 * cm))

        # relationship
        rows = [
            [
                [
                    "Is the incident related to the patient involvement in the study?",
                    self.ae_initial.get_ae_study_relation_possibility_display(),
                ]
            ],
            [
                [
                    "Relationship to Fluconozole:",
                    self.ae_initial.get_fluconazole_relation_display(),
                ]
            ],
            [
                [
                    "Relationship to Flucytosine:",
                    self.ae_initial.get_flucytosine_relation_display(),
                ]
            ],
            [
                [
                    "Relationship to Amphotericin formulation:",
                    self.ae_initial.get_amphotericin_relation_display(),
                ]
            ],
        ]
        for row in rows:
            t = Table(row, (14 * cm, 4 * cm))
            self.set_table_style(t, bg_cmd=self.bg_cmd)
            story.append(t)

        story.append(Spacer(0.1 * cm, 0.5 * cm))

        t = Table([["Action taken for treatment of AE:"]], (18 * cm))
        self.set_table_style(t, bg_cmd=self.bg_cmd)
        story.append(t)
        t = Table([[fill(self.ae_initial.ae_treatment, width=80)]], (18 * cm))
        self.set_table_style(t)
        story.append(t)

        # cause (Part3)
        rows = [
            fill(
                "Has a reason other than the specified study drug been "
                "identified as the cause of the event(s)?",
                width=60,
            )
        ]
        if self.ae_initial.ae_cause == YES:
            rows.append(
                f"{self.ae_initial.get_ae_cause_display()}: {self.ae_initial.ae_cause_other}"
            )
            table_dimensions = (9 * cm, 9 * cm)
        else:
            rows.append(self.ae_initial.get_ae_cause_display())
            table_dimensions = (14 * cm, 4 * cm)
        t = Table([rows], table_dimensions)
        self.set_table_style(t, bg_cmd=self.bg_cmd)
        story.append(t)
        t = Table(
            [
                [
                    "Was the AE a recurrence of CM symptoms?",
                    self.ae_initial.get_ae_cm_recurrence_display(),
                ]
            ],
            (14 * cm, 4 * cm),
        )
        self.set_table_style(t, bg_cmd=self.bg_cmd)
        story.append(t)

        story.append(Spacer(0.1 * cm, 0.5 * cm))
        story.append(Spacer(0.1 * cm, 0.5 * cm))

        t = Table([["Section 2: Follow-up Reports"]], (18 * cm))
        self.set_table_style(t, bg_cmd=self.bg_cmd)
        story.append(t)
        total = self.ae_initial.ae_follow_ups.count()
        row_text = (
            f"There {p.plural_verb('is', total)} {p.no('follow-up report', total)}."
        )
        t = Table([[row_text]], (18 * cm))
        self.set_table_style(t)
        story.append(t)

        story.append(Spacer(0.1 * cm, 0.5 * cm))

        for index, obj in enumerate(self.ae_initial.ae_follow_ups):
            self.append_followup_story(story, obj, index + 1, total)
            story.append(Spacer(0.1 * cm, 0.5 * cm))

        story.append(
            Paragraph(f"-- End of report --", self.styles["line_label_center"])
        )

        return story

    def append_followup_story(self, story, obj, index, total):
        rows = [
            [["Reference:", obj.action_identifier]],
            [["Report date:", obj.report_datetime.strftime("%Y-%m-%d %H:%M")]],
            [["Outcome date:", obj.outcome_date.strftime("%Y-%m-%d")]],
            [["Outcome:", obj.get_outcome_display()]],
            [["Severity increase:", obj.get_ae_grade_display()]],
            [["Follow-up report:", obj.get_followup_display()]],
        ]

        t = Table([[f"Follow-up Report {index}/{total}"]], (18 * cm))
        self.set_table_style(t, bg_cmd=self.bg_cmd)
        story.append(t)
        t = Table([[f"Prepared by {self.get_user(obj)}."]], (18 * cm))
        self.set_table_style(t)
        story.append(t)
        for row in rows:
            t = Table(row, (4 * cm, 14 * cm))
            self.set_table_style(t, bg_cmd=self.bg_cmd)
            story.append(t)

        t = Table([["Description summary of AE outcome:"]], (18 * cm))
        self.set_table_style(t, bg_cmd=self.bg_cmd)
        story.append(t)
        t = Table([[fill(obj.relevant_history, width=100)]], (18 * cm))
        self.set_table_style(t)
        story.append(t)

    def get_user(self, obj, field=None):
        field = field or "user_created"
        try:
            user = User.objects.get(username=getattr(obj, field))
        except ObjectDoesNotExist:
            user_created = getattr(obj, field)
        else:
            user_created = f"{user.first_name} {user.last_name}"
        return user_created

    def on_later_pages(self, canvas, doc):
        super().on_later_pages(canvas, doc)
        styles = getSampleStyleSheet()
        styles.add(ParagraphStyle(name="header", fontSize=6, alignment=TA_CENTER))
        width, height = A4
        canvas.setFont("Helvetica", 6)
        canvas.drawCentredString(width / 2, height - 35, self.title)

    def set_table_style(self, t, bg_cmd=None):
        cmds = [
            ("INNERGRID", (0, 0), (-1, -1), 0.25, colors.black),
            ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
            ("BOX", (0, 0), (-1, -1), 0.25, colors.black),
        ]
        if bg_cmd:
            cmds.append(bg_cmd)
        t.setStyle(TableStyle(cmds))
        t.hAlign = "LEFT"
        return t
