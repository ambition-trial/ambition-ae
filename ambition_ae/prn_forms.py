from edc_prn import Prn, site_prn_forms

from .admin_site import ambition_ae_admin

prn_models = [
    'ambition_ae.aeinitial',
    'ambition_ae.aefollowup',
    'ambition_ae.aefinal',
    'ambition_ae.aetmg',
]

for model in prn_models:
    prn = Prn(
        model=model,
        url_namespace=ambition_ae_admin.name)
    site_prn_forms.register(prn)
