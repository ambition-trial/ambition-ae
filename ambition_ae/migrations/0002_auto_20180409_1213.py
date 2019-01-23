# Generated by Django 2.0.3 on 2018-04-09 10:13

import ambition_ae.models.ae_initial
import ambition_ae.models.managers
import ambition_ae.models.recurrence_symptom

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("ambition_ae", "0001_initial")]

    operations = [
        migrations.AlterModelManagers(
            name="aefollowup",
            managers=[("on_site", ambition_ae.models.managers.CurrentSiteManager())],
        ),
        migrations.AlterModelManagers(
            name="aeinitial",
            managers=[
                ("on_site", ambition_ae.models.ae_initial.ActionIdentifierSiteManager())
            ],
        ),
        migrations.AlterModelManagers(
            name="aetmg",
            managers=[("on_site", ambition_ae.models.managers.CurrentSiteManager())],
        ),
        migrations.AlterModelManagers(
            name="recurrencesymptom",
            managers=[
                (
                    "on_site",
                    ambition_ae.models.recurrence_symptom.ActionIdentifierSiteManager(),
                )
            ],
        ),
        migrations.AddField(
            model_name="aefollowup",
            name="parent_tracking_identifier",
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name="aefollowup",
            name="related_tracking_identifier",
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name="aeinitial",
            name="parent_tracking_identifier",
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name="aeinitial",
            name="related_tracking_identifier",
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name="aetmg",
            name="parent_tracking_identifier",
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name="aetmg",
            name="related_tracking_identifier",
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name="historicalaefollowup",
            name="parent_tracking_identifier",
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name="historicalaefollowup",
            name="related_tracking_identifier",
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name="historicalaeinitial",
            name="parent_tracking_identifier",
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name="historicalaeinitial",
            name="related_tracking_identifier",
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name="historicalaetmg",
            name="parent_tracking_identifier",
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name="historicalaetmg",
            name="related_tracking_identifier",
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name="historicalrecurrencesymptom",
            name="parent_tracking_identifier",
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name="historicalrecurrencesymptom",
            name="related_tracking_identifier",
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name="recurrencesymptom",
            name="parent_tracking_identifier",
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name="recurrencesymptom",
            name="related_tracking_identifier",
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name="aefollowup",
            name="subject_identifier",
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name="aefollowup",
            name="tracking_identifier",
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name="aeinitial",
            name="subject_identifier",
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name="aeinitial",
            name="tracking_identifier",
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name="aetmg",
            name="subject_identifier",
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name="aetmg",
            name="tracking_identifier",
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name="historicalaefollowup",
            name="subject_identifier",
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name="historicalaefollowup",
            name="tracking_identifier",
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name="historicalaeinitial",
            name="subject_identifier",
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name="historicalaeinitial",
            name="tracking_identifier",
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name="historicalaetmg",
            name="subject_identifier",
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name="historicalaetmg",
            name="tracking_identifier",
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name="historicalrecurrencesymptom",
            name="subject_identifier",
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name="historicalrecurrencesymptom",
            name="tracking_identifier",
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name="recurrencesymptom",
            name="subject_identifier",
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name="recurrencesymptom",
            name="tracking_identifier",
            field=models.CharField(max_length=30, null=True),
        ),
    ]
