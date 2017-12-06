from django_revision.modeladmin_mixin import ModelAdminRevisionMixin
from edc_model_admin import (
    ModelAdminNextUrlRedirectMixin, ModelAdminFormInstructionsMixin,
    ModelAdminFormAutoNumberMixin, ModelAdminAuditFieldsMixin,
    ModelAdminReadOnlyMixin, ModelAdminInstitutionMixin,
    ModelAdminRedirectOnDeleteMixin)
from edc_metadata import NextFormGetter

from ..models import AeInitial


class ModelAdminMixin(ModelAdminNextUrlRedirectMixin, ModelAdminFormInstructionsMixin,
                      ModelAdminFormAutoNumberMixin, ModelAdminRevisionMixin,
                      ModelAdminAuditFieldsMixin, ModelAdminReadOnlyMixin,
                      ModelAdminInstitutionMixin, ModelAdminRedirectOnDeleteMixin):

    list_per_page = 10
    date_hierarchy = 'modified'
    empty_value_display = '-'
    next_form_getter_cls = NextFormGetter


class NonAeInitialModelAdminMixin:

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'ae_initial':
            if request.GET.get('ae_initial'):
                kwargs["queryset"] = AeInitial.objects.filter(
                    id__exact=request.GET.get('ae_initial', 0))
            else:
                kwargs["queryset"] = AeInitial.objects.none()
        return super().formfield_for_foreignkey(db_field, request, **kwargs)
