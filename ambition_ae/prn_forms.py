from edc_action_item import site_action_items
from edc_prn import Prn, site_prn_forms, AlreadyRegistered

from .admin_site import ambition_ae_admin

for action_item in site_action_items.registry.values():
    if action_item.prn_form_action:
        prn = Prn(
            model=action_item.model,
            url_namespace=ambition_ae_admin.name)
        try:
            site_prn_forms.register(prn)
        except AlreadyRegistered:
            pass
