# Generated by Django 2.1 on 2018-08-14 01:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ambition_ae', '0005_auto_20180813_0311'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='aeinitial',
            name='ae_intensity',
        ),
        migrations.RemoveField(
            model_name='historicalaeinitial',
            name='ae_intensity',
        ),
    ]
