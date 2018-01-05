from django.conf import settings
from django_revision.modeladmin_mixin import ModelAdminRevisionMixin
from edc_model_admin import (
    ModelAdminNextUrlRedirectMixin, ModelAdminFormInstructionsMixin,
    ModelAdminFormAutoNumberMixin, ModelAdminAuditFieldsMixin,
    ModelAdminReadOnlyMixin, ModelAdminInstitutionMixin,
    ModelAdminRedirectOnDeleteMixin)
from edc_metadata import NextFormGetter

from ..models import AeInitial
from django.urls.base import reverse


class ModelAdminMixin(ModelAdminNextUrlRedirectMixin, ModelAdminFormInstructionsMixin,
                      ModelAdminFormAutoNumberMixin, ModelAdminRevisionMixin,
                      ModelAdminAuditFieldsMixin, ModelAdminReadOnlyMixin,
                      ModelAdminInstitutionMixin, ModelAdminRedirectOnDeleteMixin):

    list_per_page = 10
    date_hierarchy = 'modified'
    empty_value_display = '-'
    next_form_getter_cls = NextFormGetter

    post_url_on_delete_name = settings.DASHBOARD_URL_NAMES.get(
        'subject_dashboard_url')

    def post_url_on_delete_kwargs(self, request, obj):
        return dict(subject_identifier=obj.subject_identifier)

    def redirect_url(self, request, obj, post_url_continue=None):
        if obj:
            return reverse(settings.DASHBOARD_URL_NAMES.get(
                'subject_dashboard_url'), kwargs=dict(subject_identifier=obj.subject_identifier))
        else:
            return super().redirect_url(request, obj, post_url_continue)


class NonAeInitialModelAdminMixin:

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'ae_initial':
            if request.GET.get('ae_initial'):
                kwargs["queryset"] = AeInitial.objects.filter(
                    id__exact=request.GET.get('ae_initial', 0))
            else:
                kwargs["queryset"] = AeInitial.objects.none()
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

    def get_readonly_fields(self, request, obj=None):
        fields = super().get_readonly_fields(request, obj=obj)
        if obj:
            fields = fields + ('ae_initial', )
        return fields + ('tracking_identifier', 'action_identifier')
