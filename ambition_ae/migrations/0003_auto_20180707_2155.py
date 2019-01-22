# Generated by Django 2.0.7 on 2018-07-07 19:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [("ambition_ae", "0002_auto_20180409_1213")]

    operations = [
        migrations.AlterModelOptions(
            name="historicalaefollowup",
            options={
                "get_latest_by": "history_date",
                "ordering": ("-history_date", "-history_id"),
                "verbose_name": "historical AE Follow-up Report",
            },
        ),
        migrations.AlterModelOptions(
            name="historicalaeinitial",
            options={
                "get_latest_by": "history_date",
                "ordering": ("-history_date", "-history_id"),
                "verbose_name": "historical AE Initial Report",
            },
        ),
        migrations.AlterModelOptions(
            name="historicalaetmg",
            options={
                "get_latest_by": "history_date",
                "ordering": ("-history_date", "-history_id"),
                "verbose_name": "historical AE TMG Report",
            },
        ),
        migrations.AlterModelOptions(
            name="historicalrecurrencesymptom",
            options={
                "get_latest_by": "history_date",
                "ordering": ("-history_date", "-history_id"),
                "verbose_name": "historical Recurrence of Symptoms",
            },
        ),
        migrations.RenameField(
            model_name="aefollowup",
            old_name="parent_tracking_identifier",
            new_name="parent_reference_identifier",
        ),
        migrations.RenameField(
            model_name="aefollowup",
            old_name="related_tracking_identifier",
            new_name="related_reference_identifier",
        ),
        migrations.RenameField(
            model_name="aeinitial",
            old_name="parent_tracking_identifier",
            new_name="parent_reference_identifier",
        ),
        migrations.RenameField(
            model_name="aeinitial",
            old_name="related_tracking_identifier",
            new_name="related_reference_identifier",
        ),
        migrations.RenameField(
            model_name="aetmg",
            old_name="parent_tracking_identifier",
            new_name="parent_reference_identifier",
        ),
        migrations.RenameField(
            model_name="aetmg",
            old_name="related_tracking_identifier",
            new_name="related_reference_identifier",
        ),
        migrations.RenameField(
            model_name="historicalaefollowup",
            old_name="parent_tracking_identifier",
            new_name="parent_reference_identifier",
        ),
        migrations.RenameField(
            model_name="historicalaefollowup",
            old_name="related_tracking_identifier",
            new_name="related_reference_identifier",
        ),
        migrations.RenameField(
            model_name="historicalaeinitial",
            old_name="parent_tracking_identifier",
            new_name="parent_reference_identifier",
        ),
        migrations.RenameField(
            model_name="historicalaeinitial",
            old_name="related_tracking_identifier",
            new_name="related_reference_identifier",
        ),
        migrations.RenameField(
            model_name="historicalaetmg",
            old_name="parent_tracking_identifier",
            new_name="parent_reference_identifier",
        ),
        migrations.RenameField(
            model_name="historicalaetmg",
            old_name="related_tracking_identifier",
            new_name="related_reference_identifier",
        ),
        migrations.RenameField(
            model_name="historicalrecurrencesymptom",
            old_name="parent_tracking_identifier",
            new_name="parent_reference_identifier",
        ),
        migrations.RenameField(
            model_name="historicalrecurrencesymptom",
            old_name="related_tracking_identifier",
            new_name="related_reference_identifier",
        ),
        migrations.RenameField(
            model_name="recurrencesymptom",
            old_name="parent_tracking_identifier",
            new_name="parent_reference_identifier",
        ),
        migrations.RenameField(
            model_name="recurrencesymptom",
            old_name="related_tracking_identifier",
            new_name="related_reference_identifier",
        ),
    ]
