from django.contrib.admin import AdminSite as DjangoAdminSite


class AdminSite(DjangoAdminSite):
    site_title = 'Ambition Adverse Events'
    site_header = 'Ambition Adverse Events'
    index_title = 'Ambition Adverse Events'
    site_url = '/administration/'


ambition_ae_admin = AdminSite(name='ambition_ae_admin')
