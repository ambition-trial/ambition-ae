# Generated by Django 2.1 on 2018-09-01 13:12

import ambition_ae.models.ae_tmg
import ambition_ae.models.recurrence_symptom
import edc_action_item.managers
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("ambition_ae", "0007_auto_20180823_2235")]

    operations = [
        migrations.AlterModelManagers(
            name="aefollowup",
            managers=[
                ("on_site", edc_action_item.managers.ActionIdentifierSiteManager()),
                ("objects", edc_action_item.managers.ActionIdentifierManager()),
            ],
        ),
        migrations.AlterModelManagers(
            name="aeinitial",
            managers=[
                ("on_site", edc_action_item.managers.ActionIdentifierSiteManager()),
                ("objects", edc_action_item.managers.ActionIdentifierManager()),
            ],
        ),
        migrations.AlterModelManagers(
            name="aetmg",
            managers=[
                ("on_site", edc_action_item.managers.ActionIdentifierSiteManager()),
                ("objects", edc_action_item.managers.ActionIdentifierManager()),
            ],
        ),
        migrations.AlterModelManagers(
            name="recurrencesymptom",
            managers=[
                ("on_site", edc_action_item.managers.ActionIdentifierSiteManager()),
                ("objects", edc_action_item.managers.ActionIdentifierManager()),
            ],
        ),
        migrations.AddField(
            model_name="aeinitial",
            name="amphotericin_relation",
            field=models.CharField(
                choices=[
                    ("not_related", "Not related"),
                    ("possibly_related", "Possibly related"),
                    ("probably_related", "Probably related"),
                    ("definitely_related", "Definitely related"),
                    ("unlikely_related", "Unlikely related"),
                    ("N/A", "Not applicable"),
                ],
                max_length=25,
                null=True,
                verbose_name="Amphotericin formulation:",
            ),
        ),
        migrations.AddField(
            model_name="historicalaeinitial",
            name="amphotericin_relation",
            field=models.CharField(
                choices=[
                    ("not_related", "Not related"),
                    ("possibly_related", "Possibly related"),
                    ("probably_related", "Probably related"),
                    ("definitely_related", "Definitely related"),
                    ("unlikely_related", "Unlikely related"),
                    ("N/A", "Not applicable"),
                ],
                max_length=25,
                null=True,
                verbose_name="Amphotericin formulation:",
            ),
        ),
        migrations.AlterField(
            model_name="aeinitial",
            name="ambisome_relation",
            field=models.CharField(
                choices=[
                    ("not_related", "Not related"),
                    ("possibly_related", "Possibly related"),
                    ("probably_related", "Probably related"),
                    ("definitely_related", "Definitely related"),
                    ("unlikely_related", "Unlikely related"),
                    ("N/A", "Not applicable"),
                ],
                editable=False,
                max_length=25,
                null=True,
                verbose_name="Relationship to Ambisome:",
            ),
        ),
        migrations.AlterField(
            model_name="aeinitial",
            name="amphotericin_b_relation",
            field=models.CharField(
                choices=[
                    ("not_related", "Not related"),
                    ("possibly_related", "Possibly related"),
                    ("probably_related", "Probably related"),
                    ("definitely_related", "Definitely related"),
                    ("unlikely_related", "Unlikely related"),
                    ("N/A", "Not applicable"),
                ],
                editable=False,
                max_length=25,
                null=True,
                verbose_name="Relationship to Amphotericin B:",
            ),
        ),
        migrations.AlterField(
            model_name="historicalaeinitial",
            name="ambisome_relation",
            field=models.CharField(
                choices=[
                    ("not_related", "Not related"),
                    ("possibly_related", "Possibly related"),
                    ("probably_related", "Probably related"),
                    ("definitely_related", "Definitely related"),
                    ("unlikely_related", "Unlikely related"),
                    ("N/A", "Not applicable"),
                ],
                editable=False,
                max_length=25,
                null=True,
                verbose_name="Relationship to Ambisome:",
            ),
        ),
        migrations.AlterField(
            model_name="historicalaeinitial",
            name="amphotericin_b_relation",
            field=models.CharField(
                choices=[
                    ("not_related", "Not related"),
                    ("possibly_related", "Possibly related"),
                    ("probably_related", "Probably related"),
                    ("definitely_related", "Definitely related"),
                    ("unlikely_related", "Unlikely related"),
                    ("N/A", "Not applicable"),
                ],
                editable=False,
                max_length=25,
                null=True,
                verbose_name="Relationship to Amphotericin B:",
            ),
        ),
    ]
