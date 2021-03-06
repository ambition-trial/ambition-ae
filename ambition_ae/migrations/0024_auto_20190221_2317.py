# Generated by Django 2.1.5 on 2019-02-21 21:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("ambition_ae", "0023_aesusar_historicalaesusar")]

    operations = [
        migrations.AlterField(
            model_name="aesusar",
            name="report_status",
            field=models.CharField(
                choices=[
                    ("open", "Open. Some information is still pending."),
                    ("closed", "Closed. This report is complete"),
                ],
                default="closed",
                editable=False,
                max_length=25,
                verbose_name="What is the status of this report?",
            ),
        ),
        migrations.AlterField(
            model_name="historicalaesusar",
            name="report_status",
            field=models.CharField(
                choices=[
                    ("open", "Open. Some information is still pending."),
                    ("closed", "Closed. This report is complete"),
                ],
                default="closed",
                editable=False,
                max_length=25,
                verbose_name="What is the status of this report?",
            ),
        ),
    ]
