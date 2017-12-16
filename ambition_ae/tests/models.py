from django.db import models
from edc_base.model_mixins.base_uuid_model import BaseUuidModel
from django.db.models.deletion import PROTECT


class SubjectVisit(BaseUuidModel):

    subject_identifier = models.CharField(
        max_length=50)


class PatientHistory(BaseUuidModel):

    subject_visit = models.ForeignKey(SubjectVisit, on_delete=PROTECT)

    first_arv_regimen = models.CharField(
        max_length=50)
