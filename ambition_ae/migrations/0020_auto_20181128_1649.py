# Generated by Django 2.1.3 on 2018-11-28 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ambition_ae', '0019_auto_20181113_0715'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aeinitial',
            name='ae_classification',
            field=models.CharField(choices=[('anaemia', 'Anaemia'), ('bacteraemia/sepsis', 'Bacteraemia/Sepsis'), ('CM_IRIS', 'CM IRIS'), ('diarrhoea', 'Diarrhoea'), ('hypokalaemia', 'Hypokalaemia'), ('neutropaenia', 'Neutropaenia'), ('pneumonia', 'Pneumonia'), ('respiratory_distress', 'Respiratory distress'), ('TB', 'TB'), ('thrombocytopenia', 'Thrombocytopenia'), ('thrombophlebitis', 'Renal impairment'), ('OTHER', 'Other')], max_length=150),
        ),
        migrations.AlterField(
            model_name='aetmg',
            name='ae_classification',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='historicalaeinitial',
            name='ae_classification',
            field=models.CharField(choices=[('anaemia', 'Anaemia'), ('bacteraemia/sepsis', 'Bacteraemia/Sepsis'), ('CM_IRIS', 'CM IRIS'), ('diarrhoea', 'Diarrhoea'), ('hypokalaemia', 'Hypokalaemia'), ('neutropaenia', 'Neutropaenia'), ('pneumonia', 'Pneumonia'), ('respiratory_distress', 'Respiratory distress'), ('TB', 'TB'), ('thrombocytopenia', 'Thrombocytopenia'), ('thrombophlebitis', 'Renal impairment'), ('OTHER', 'Other')], max_length=150),
        ),
        migrations.AlterField(
            model_name='historicalaetmg',
            name='ae_classification',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
    ]