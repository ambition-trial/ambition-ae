from django.db import models


class DeathReportTmgManager(models.Manager):

    def get_by_natural_key(self, subject_identifier):
        return self.get(death_report__subject_identifier=subject_identifier)
