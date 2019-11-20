# Generated by Django 2.2.7 on 2019-11-20 13:49

import _socket
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django_audit_fields.fields.hostname_modification_field
import django_audit_fields.fields.userfield
import django_audit_fields.fields.uuid_auto_field
import django_audit_fields.models.audit_model_mixin
import django_revision.revision_field
import edc_action_item.managers
import edc_adverse_event.model_mixins.death_report_tmg_model_mixin
import edc_model.validators.date
import edc_model_fields.fields.other_charfield
import edc_protocol.validators
import edc_utils.date
import simple_history.models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('edc_action_item', '0024_auto_20191024_1000'),
        ('sites', '0002_alter_domain_unique'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('edc_adverse_event', '0003_auto_20191026_2231'),
        ('ambition_ae', '0041_auto_20191017_108'),
    ]

    operations = [
        migrations.CreateModel(
            name='DeathReport',
            fields=[
                ('revision', django_revision.revision_field.RevisionField(blank=True, editable=False, help_text='System field. Git repository tag:branch:commit.', max_length=75, null=True, verbose_name='Revision')),
                ('created', models.DateTimeField(blank=True, default=django_audit_fields.models.audit_model_mixin.utcnow)),
                ('modified', models.DateTimeField(blank=True, default=django_audit_fields.models.audit_model_mixin.utcnow)),
                ('user_created', django_audit_fields.fields.userfield.UserField(blank=True, help_text='Updated by admin.save_model', max_length=50, verbose_name='user created')),
                ('user_modified', django_audit_fields.fields.userfield.UserField(blank=True, help_text='Updated by admin.save_model', max_length=50, verbose_name='user modified')),
                ('hostname_created', models.CharField(blank=True, default=_socket.gethostname, help_text='System field. (modified on create only)', max_length=60)),
                ('hostname_modified', django_audit_fields.fields.hostname_modification_field.HostnameModificationField(blank=True, help_text='System field. (modified on every save)', max_length=50)),
                ('device_created', models.CharField(blank=True, max_length=10)),
                ('device_modified', models.CharField(blank=True, max_length=10)),
                ('id', django_audit_fields.fields.uuid_auto_field.UUIDAutoField(blank=True, editable=False, help_text='System auto field. UUID primary key.', primary_key=True, serialize=False)),
                ('subject_identifier', models.CharField(max_length=50, unique=True)),
                ('tracking_identifier', models.CharField(max_length=30, unique=True)),
                ('action_identifier', models.CharField(max_length=50, unique=True)),
                ('parent_action_identifier', models.CharField(help_text='action identifier that links to parent reference model instance.', max_length=30, null=True)),
                ('related_action_identifier', models.CharField(help_text='action identifier that links to related reference model instance.', max_length=30, null=True)),
                ('action_item_reason', models.TextField(editable=False, null=True)),
                ('report_datetime', models.DateTimeField(default=edc_utils.date.get_utcnow, validators=[edc_protocol.validators.datetime_not_before_study_start, edc_model.validators.date.datetime_not_future], verbose_name='Report Date')),
                ('death_datetime', models.DateTimeField(validators=[edc_model.validators.date.datetime_not_future], verbose_name='Date and Time of Death')),
                ('study_day', models.IntegerField(validators=[django.core.validators.MinValueValidator(1)], verbose_name='Study day')),
                ('death_as_inpatient', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=5, verbose_name='Death as inpatient')),
                ('cause_of_death_other', edc_model_fields.fields.other_charfield.OtherCharField(blank=True, max_length=100, null=True, verbose_name='If other, please specify ...')),
                ('narrative', models.TextField(verbose_name='Narrative')),
                ('cause_of_death_old', models.CharField(default='QUESTION_RETIRED', editable=False, help_text='Main cause of death in the opinion of the local study doctor and local PI', max_length=50, verbose_name='Main cause of death')),
                ('tb_site', models.CharField(choices=[('meningitis', 'Meningitis'), ('pulmonary', 'Pulmonary'), ('disseminated', 'Disseminated'), ('N/A', 'Not applicable')], default='N/A', max_length=25, verbose_name='If cause of death is TB, specify site of TB disease')),
                ('action_item', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='edc_action_item.ActionItem')),
                ('cause_of_death', models.ForeignKey(help_text='Main cause of death in the opinion of the local study doctor and local PI', null=True, on_delete=django.db.models.deletion.PROTECT, to='edc_adverse_event.CauseOfDeath', verbose_name='Main cause of death')),
                ('parent_action_item', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='+', to='edc_action_item.ActionItem')),
                ('related_action_item', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='+', to='edc_action_item.ActionItem')),
                ('site', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='+', to='sites.Site')),
            ],
            options={
                'verbose_name': 'Death Report',
                'abstract': False,
            },
            managers=[
                ('on_site', edc_action_item.managers.ActionIdentifierSiteManager()),
                ('objects', edc_action_item.managers.ActionIdentifierManager()),
            ],
        ),
        migrations.CreateModel(
            name='HistoricalDeathReportTmgSecond',
            fields=[
                ('revision', django_revision.revision_field.RevisionField(blank=True, editable=False, help_text='System field. Git repository tag:branch:commit.', max_length=75, null=True, verbose_name='Revision')),
                ('created', models.DateTimeField(blank=True, default=django_audit_fields.models.audit_model_mixin.utcnow)),
                ('modified', models.DateTimeField(blank=True, default=django_audit_fields.models.audit_model_mixin.utcnow)),
                ('user_created', django_audit_fields.fields.userfield.UserField(blank=True, help_text='Updated by admin.save_model', max_length=50, verbose_name='user created')),
                ('user_modified', django_audit_fields.fields.userfield.UserField(blank=True, help_text='Updated by admin.save_model', max_length=50, verbose_name='user modified')),
                ('hostname_created', models.CharField(blank=True, default=_socket.gethostname, help_text='System field. (modified on create only)', max_length=60)),
                ('hostname_modified', django_audit_fields.fields.hostname_modification_field.HostnameModificationField(blank=True, help_text='System field. (modified on every save)', max_length=50)),
                ('device_created', models.CharField(blank=True, max_length=10)),
                ('device_modified', models.CharField(blank=True, max_length=10)),
                ('id', django_audit_fields.fields.uuid_auto_field.UUIDAutoField(blank=True, db_index=True, editable=False, help_text='System auto field. UUID primary key.')),
                ('report_status', models.CharField(choices=[('open', 'Open. Some information is still pending.'), ('closed', 'Closed. This report is complete')], max_length=25, verbose_name='What is the status of this report?')),
                ('report_closed_datetime', models.DateTimeField(blank=True, null=True, validators=[edc_model.validators.date.datetime_not_future], verbose_name='Date and time report closed.')),
                ('subject_identifier', models.CharField(max_length=50)),
                ('tracking_identifier', models.CharField(db_index=True, max_length=30)),
                ('action_identifier', models.CharField(db_index=True, max_length=50)),
                ('parent_action_identifier', models.CharField(help_text='action identifier that links to parent reference model instance.', max_length=30, null=True)),
                ('related_action_identifier', models.CharField(help_text='action identifier that links to related reference model instance.', max_length=30, null=True)),
                ('action_item_reason', models.TextField(editable=False, null=True)),
                ('history_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('report_datetime', models.DateTimeField(default=edc_utils.date.get_utcnow, validators=[edc_protocol.validators.datetime_not_before_study_start, edc_model.validators.date.datetime_not_future], verbose_name='Report Date')),
                ('cause_of_death_other', models.CharField(blank=True, max_length=100, null=True, verbose_name='If "Other" above, please specify')),
                ('cause_of_death_agreed', models.CharField(blank=True, choices=[('Yes', 'Yes'), ('No', 'No')], help_text='If No, explain in the narrative below', max_length=15, null=True, verbose_name='Is the cause of death agreed between study doctor and TMG member?')),
                ('narrative', models.TextField(blank=True, null=True, verbose_name='Narrative')),
                ('cause_of_death_old', models.CharField(blank=True, default='QUESTION_RETIRED', help_text='Main cause of death in the opinion of TMG member', max_length=50, null=True, verbose_name='Main cause of death')),
                ('tb_site', models.CharField(blank=True, choices=[('meningitis', 'Meningitis'), ('pulmonary', 'Pulmonary'), ('disseminated', 'Disseminated'), ('N/A', 'Not applicable')], default='N/A', max_length=25, verbose_name='If cause of death is TB, specify site of TB disease')),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('action_item', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='edc_action_item.ActionItem')),
                ('cause_of_death', models.ForeignKey(blank=True, db_constraint=False, help_text='Main cause of death in the opinion of the local study doctor and local PI', null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='edc_adverse_event.CauseOfDeath', verbose_name='Main cause of death')),
                ('death_report', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='ambition_ae.DeathReport')),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('parent_action_item', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='edc_action_item.ActionItem')),
                ('related_action_item', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='edc_action_item.ActionItem')),
                ('site', models.ForeignKey(blank=True, db_constraint=False, editable=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='sites.Site')),
            ],
            options={
                'verbose_name': 'historical Death Report TMG (2nd)',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='HistoricalDeathReportTmg',
            fields=[
                ('revision', django_revision.revision_field.RevisionField(blank=True, editable=False, help_text='System field. Git repository tag:branch:commit.', max_length=75, null=True, verbose_name='Revision')),
                ('created', models.DateTimeField(blank=True, default=django_audit_fields.models.audit_model_mixin.utcnow)),
                ('modified', models.DateTimeField(blank=True, default=django_audit_fields.models.audit_model_mixin.utcnow)),
                ('user_created', django_audit_fields.fields.userfield.UserField(blank=True, help_text='Updated by admin.save_model', max_length=50, verbose_name='user created')),
                ('user_modified', django_audit_fields.fields.userfield.UserField(blank=True, help_text='Updated by admin.save_model', max_length=50, verbose_name='user modified')),
                ('hostname_created', models.CharField(blank=True, default=_socket.gethostname, help_text='System field. (modified on create only)', max_length=60)),
                ('hostname_modified', django_audit_fields.fields.hostname_modification_field.HostnameModificationField(blank=True, help_text='System field. (modified on every save)', max_length=50)),
                ('device_created', models.CharField(blank=True, max_length=10)),
                ('device_modified', models.CharField(blank=True, max_length=10)),
                ('id', django_audit_fields.fields.uuid_auto_field.UUIDAutoField(blank=True, db_index=True, editable=False, help_text='System auto field. UUID primary key.')),
                ('report_status', models.CharField(choices=[('open', 'Open. Some information is still pending.'), ('closed', 'Closed. This report is complete')], max_length=25, verbose_name='What is the status of this report?')),
                ('report_closed_datetime', models.DateTimeField(blank=True, null=True, validators=[edc_model.validators.date.datetime_not_future], verbose_name='Date and time report closed.')),
                ('subject_identifier', models.CharField(max_length=50)),
                ('tracking_identifier', models.CharField(db_index=True, max_length=30)),
                ('action_identifier', models.CharField(db_index=True, max_length=50)),
                ('parent_action_identifier', models.CharField(help_text='action identifier that links to parent reference model instance.', max_length=30, null=True)),
                ('related_action_identifier', models.CharField(help_text='action identifier that links to related reference model instance.', max_length=30, null=True)),
                ('action_item_reason', models.TextField(editable=False, null=True)),
                ('history_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('report_datetime', models.DateTimeField(default=edc_utils.date.get_utcnow, validators=[edc_protocol.validators.datetime_not_before_study_start, edc_model.validators.date.datetime_not_future], verbose_name='Report Date')),
                ('cause_of_death_other', models.CharField(blank=True, max_length=100, null=True, verbose_name='If "Other" above, please specify')),
                ('cause_of_death_agreed', models.CharField(blank=True, choices=[('Yes', 'Yes'), ('No', 'No')], help_text='If No, explain in the narrative below', max_length=15, null=True, verbose_name='Is the cause of death agreed between study doctor and TMG member?')),
                ('narrative', models.TextField(blank=True, null=True, verbose_name='Narrative')),
                ('cause_of_death_old', models.CharField(blank=True, default='QUESTION_RETIRED', help_text='Main cause of death in the opinion of TMG member', max_length=50, null=True, verbose_name='Main cause of death')),
                ('tb_site', models.CharField(blank=True, choices=[('meningitis', 'Meningitis'), ('pulmonary', 'Pulmonary'), ('disseminated', 'Disseminated'), ('N/A', 'Not applicable')], default='N/A', max_length=25, verbose_name='If cause of death is TB, specify site of TB disease')),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('action_item', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='edc_action_item.ActionItem')),
                ('cause_of_death', models.ForeignKey(blank=True, db_constraint=False, help_text='Main cause of death in the opinion of the local study doctor and local PI', null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='edc_adverse_event.CauseOfDeath', verbose_name='Main cause of death')),
                ('death_report', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='ambition_ae.DeathReport')),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('parent_action_item', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='edc_action_item.ActionItem')),
                ('related_action_item', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='edc_action_item.ActionItem')),
                ('site', models.ForeignKey(blank=True, db_constraint=False, editable=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='sites.Site')),
            ],
            options={
                'verbose_name': 'historical Death Report TMG (1st)',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='HistoricalDeathReport',
            fields=[
                ('revision', django_revision.revision_field.RevisionField(blank=True, editable=False, help_text='System field. Git repository tag:branch:commit.', max_length=75, null=True, verbose_name='Revision')),
                ('created', models.DateTimeField(blank=True, default=django_audit_fields.models.audit_model_mixin.utcnow)),
                ('modified', models.DateTimeField(blank=True, default=django_audit_fields.models.audit_model_mixin.utcnow)),
                ('user_created', django_audit_fields.fields.userfield.UserField(blank=True, help_text='Updated by admin.save_model', max_length=50, verbose_name='user created')),
                ('user_modified', django_audit_fields.fields.userfield.UserField(blank=True, help_text='Updated by admin.save_model', max_length=50, verbose_name='user modified')),
                ('hostname_created', models.CharField(blank=True, default=_socket.gethostname, help_text='System field. (modified on create only)', max_length=60)),
                ('hostname_modified', django_audit_fields.fields.hostname_modification_field.HostnameModificationField(blank=True, help_text='System field. (modified on every save)', max_length=50)),
                ('device_created', models.CharField(blank=True, max_length=10)),
                ('device_modified', models.CharField(blank=True, max_length=10)),
                ('id', django_audit_fields.fields.uuid_auto_field.UUIDAutoField(blank=True, db_index=True, editable=False, help_text='System auto field. UUID primary key.')),
                ('subject_identifier', models.CharField(db_index=True, max_length=50)),
                ('tracking_identifier', models.CharField(db_index=True, max_length=30)),
                ('action_identifier', models.CharField(db_index=True, max_length=50)),
                ('parent_action_identifier', models.CharField(help_text='action identifier that links to parent reference model instance.', max_length=30, null=True)),
                ('related_action_identifier', models.CharField(help_text='action identifier that links to related reference model instance.', max_length=30, null=True)),
                ('action_item_reason', models.TextField(editable=False, null=True)),
                ('history_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('report_datetime', models.DateTimeField(default=edc_utils.date.get_utcnow, validators=[edc_protocol.validators.datetime_not_before_study_start, edc_model.validators.date.datetime_not_future], verbose_name='Report Date')),
                ('death_datetime', models.DateTimeField(validators=[edc_model.validators.date.datetime_not_future], verbose_name='Date and Time of Death')),
                ('study_day', models.IntegerField(validators=[django.core.validators.MinValueValidator(1)], verbose_name='Study day')),
                ('death_as_inpatient', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=5, verbose_name='Death as inpatient')),
                ('cause_of_death_other', edc_model_fields.fields.other_charfield.OtherCharField(blank=True, max_length=100, null=True, verbose_name='If other, please specify ...')),
                ('narrative', models.TextField(verbose_name='Narrative')),
                ('cause_of_death_old', models.CharField(default='QUESTION_RETIRED', editable=False, help_text='Main cause of death in the opinion of the local study doctor and local PI', max_length=50, verbose_name='Main cause of death')),
                ('tb_site', models.CharField(choices=[('meningitis', 'Meningitis'), ('pulmonary', 'Pulmonary'), ('disseminated', 'Disseminated'), ('N/A', 'Not applicable')], default='N/A', max_length=25, verbose_name='If cause of death is TB, specify site of TB disease')),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('action_item', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='edc_action_item.ActionItem')),
                ('cause_of_death', models.ForeignKey(blank=True, db_constraint=False, help_text='Main cause of death in the opinion of the local study doctor and local PI', null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='edc_adverse_event.CauseOfDeath', verbose_name='Main cause of death')),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('parent_action_item', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='edc_action_item.ActionItem')),
                ('related_action_item', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='edc_action_item.ActionItem')),
                ('site', models.ForeignKey(blank=True, db_constraint=False, editable=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='sites.Site')),
            ],
            options={
                'verbose_name': 'historical Death Report',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='DeathReportTmg',
            fields=[
                ('revision', django_revision.revision_field.RevisionField(blank=True, editable=False, help_text='System field. Git repository tag:branch:commit.', max_length=75, null=True, verbose_name='Revision')),
                ('created', models.DateTimeField(blank=True, default=django_audit_fields.models.audit_model_mixin.utcnow)),
                ('modified', models.DateTimeField(blank=True, default=django_audit_fields.models.audit_model_mixin.utcnow)),
                ('user_created', django_audit_fields.fields.userfield.UserField(blank=True, help_text='Updated by admin.save_model', max_length=50, verbose_name='user created')),
                ('user_modified', django_audit_fields.fields.userfield.UserField(blank=True, help_text='Updated by admin.save_model', max_length=50, verbose_name='user modified')),
                ('hostname_created', models.CharField(blank=True, default=_socket.gethostname, help_text='System field. (modified on create only)', max_length=60)),
                ('hostname_modified', django_audit_fields.fields.hostname_modification_field.HostnameModificationField(blank=True, help_text='System field. (modified on every save)', max_length=50)),
                ('device_created', models.CharField(blank=True, max_length=10)),
                ('device_modified', models.CharField(blank=True, max_length=10)),
                ('id', django_audit_fields.fields.uuid_auto_field.UUIDAutoField(blank=True, editable=False, help_text='System auto field. UUID primary key.', primary_key=True, serialize=False)),
                ('report_status', models.CharField(choices=[('open', 'Open. Some information is still pending.'), ('closed', 'Closed. This report is complete')], max_length=25, verbose_name='What is the status of this report?')),
                ('report_closed_datetime', models.DateTimeField(blank=True, null=True, validators=[edc_model.validators.date.datetime_not_future], verbose_name='Date and time report closed.')),
                ('subject_identifier', models.CharField(max_length=50)),
                ('tracking_identifier', models.CharField(max_length=30, unique=True)),
                ('action_identifier', models.CharField(max_length=50, unique=True)),
                ('parent_action_identifier', models.CharField(help_text='action identifier that links to parent reference model instance.', max_length=30, null=True)),
                ('related_action_identifier', models.CharField(help_text='action identifier that links to related reference model instance.', max_length=30, null=True)),
                ('action_item_reason', models.TextField(editable=False, null=True)),
                ('report_datetime', models.DateTimeField(default=edc_utils.date.get_utcnow, validators=[edc_protocol.validators.datetime_not_before_study_start, edc_model.validators.date.datetime_not_future], verbose_name='Report Date')),
                ('cause_of_death_other', models.CharField(blank=True, max_length=100, null=True, verbose_name='If "Other" above, please specify')),
                ('cause_of_death_agreed', models.CharField(blank=True, choices=[('Yes', 'Yes'), ('No', 'No')], help_text='If No, explain in the narrative below', max_length=15, null=True, verbose_name='Is the cause of death agreed between study doctor and TMG member?')),
                ('narrative', models.TextField(blank=True, null=True, verbose_name='Narrative')),
                ('cause_of_death_old', models.CharField(blank=True, default='QUESTION_RETIRED', help_text='Main cause of death in the opinion of TMG member', max_length=50, null=True, verbose_name='Main cause of death')),
                ('tb_site', models.CharField(blank=True, choices=[('meningitis', 'Meningitis'), ('pulmonary', 'Pulmonary'), ('disseminated', 'Disseminated'), ('N/A', 'Not applicable')], default='N/A', max_length=25, verbose_name='If cause of death is TB, specify site of TB disease')),
                ('action_item', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='edc_action_item.ActionItem')),
                ('cause_of_death', models.ForeignKey(help_text='Main cause of death in the opinion of the local study doctor and local PI', null=True, on_delete=django.db.models.deletion.PROTECT, to='edc_adverse_event.CauseOfDeath', verbose_name='Main cause of death')),
                ('death_report', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='ambition_ae.DeathReport')),
                ('parent_action_item', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='+', to='edc_action_item.ActionItem')),
                ('related_action_item', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='+', to='edc_action_item.ActionItem')),
                ('site', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='+', to='sites.Site')),
            ],
            options={
                'verbose_name': 'Death Report TMG (1st)',
                'verbose_name_plural': 'Death Report TMG (1st)',
                'abstract': False,
            },
            managers=[
                ('on_site', edc_adverse_event.model_mixins.death_report_tmg_model_mixin.DeathReportTmgSiteManager()),
                ('objects', edc_adverse_event.model_mixins.death_report_tmg_model_mixin.DeathReportTmgManager()),
            ],
        ),
        migrations.CreateModel(
            name='DeathReportTmgSecond',
            fields=[
            ],
            options={
                'verbose_name': 'Death Report TMG (2nd)',
                'verbose_name_plural': 'Death Report TMG (2nd)',
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('ambition_ae.deathreporttmg',),
            managers=[
                ('on_site', edc_adverse_event.model_mixins.death_report_tmg_model_mixin.DeathReportTmgSecondSiteManager()),
                ('objects', edc_adverse_event.model_mixins.death_report_tmg_model_mixin.DeathReportTmgSecondManager()),
            ],
        ),
        migrations.AddIndex(
            model_name='deathreporttmg',
            index=models.Index(fields=['subject_identifier', 'action_identifier', 'site', 'id'], name='ambition_ae_subject_809724_idx'),
        ),
        migrations.AddIndex(
            model_name='deathreport',
            index=models.Index(fields=['subject_identifier', 'action_identifier', 'site', 'id'], name='ambition_ae_subject_ec758c_idx'),
        ),
    ]
