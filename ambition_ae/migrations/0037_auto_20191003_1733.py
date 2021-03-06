# Generated by Django 2.2.5 on 2019-10-03 15:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [("ambition_ae", "0036_auto_20190807_0024")]

    operations = [
        migrations.AddField(
            model_name="aeinitial",
            name="study_drug_relation",
            field=models.CharField(
                choices=[
                    ("not_related", "Not related"),
                    ("unlikely_related", "Unlikely related"),
                    ("possibly_related", "Possibly related"),
                    ("probably_related", "Probably related"),
                    ("definitely_related", "Definitely related"),
                    ("N/A", "Not applicable"),
                ],
                max_length=25,
                null=True,
                verbose_name="Relation to study drug:",
            ),
        ),
        migrations.AddField(
            model_name="historicalaeinitial",
            name="study_drug_relation",
            field=models.CharField(
                choices=[
                    ("not_related", "Not related"),
                    ("unlikely_related", "Unlikely related"),
                    ("possibly_related", "Possibly related"),
                    ("probably_related", "Probably related"),
                    ("definitely_related", "Definitely related"),
                    ("N/A", "Not applicable"),
                ],
                max_length=25,
                null=True,
                verbose_name="Relation to study drug:",
            ),
        ),
        migrations.AlterField(
            model_name="aeinitial",
            name="sae_reason",
            field=models.ForeignKey(
                help_text="If subject deceased, submit a Death Report",
                on_delete=django.db.models.deletion.PROTECT,
                to="edc_adverse_event.SaeReason",
                verbose_name='If "Yes", reason for SAE:',
            ),
        ),
    ]
