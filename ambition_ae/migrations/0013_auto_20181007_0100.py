# Generated by Django 2.1 on 2018-10-06 23:00

from django.db import migrations
from edc_action_item.data_fixers import fix_null_historical_action_identifier


def fix(apps, schema_editor):

    fix_null_historical_action_identifier(
        app_label="ambition_ae",
        models=["aeinitial", "aefollowup", "recurrencesymptom", "aetmg"],
    )


class Migration(migrations.Migration):

    dependencies = [("ambition_ae", "0012_auto_20181009_0545")]

    operations = [migrations.RunPython(fix)]
