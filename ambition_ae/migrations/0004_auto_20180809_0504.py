# Generated by Django 2.1 on 2018-08-09 03:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ambition_ae', '0003_auto_20180707_2155'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aefollowup',
            name='tracking_identifier',
            field=models.CharField(max_length=30, unique=True),
        ),
        migrations.AlterField(
            model_name='aeinitial',
            name='tracking_identifier',
            field=models.CharField(max_length=30, unique=True),
        ),
        migrations.AlterField(
            model_name='aetmg',
            name='tracking_identifier',
            field=models.CharField(max_length=30, unique=True),
        ),
        migrations.AlterField(
            model_name='historicalaefollowup',
            name='tracking_identifier',
            field=models.CharField(db_index=True, max_length=30),
        ),
        migrations.AlterField(
            model_name='historicalaeinitial',
            name='tracking_identifier',
            field=models.CharField(db_index=True, max_length=30),
        ),
        migrations.AlterField(
            model_name='historicalaetmg',
            name='tracking_identifier',
            field=models.CharField(db_index=True, max_length=30),
        ),
        migrations.AlterField(
            model_name='historicalrecurrencesymptom',
            name='tracking_identifier',
            field=models.CharField(db_index=True, max_length=30),
        ),
        migrations.AlterField(
            model_name='recurrencesymptom',
            name='tracking_identifier',
            field=models.CharField(max_length=30, unique=True),
        ),
    ]