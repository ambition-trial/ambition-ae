from django.urls.conf import path
from django.views.generic.base import RedirectView

from .admin_site import ambition_ae_admin
from edc_action_item.admin_site import edc_action_item_admin
from django.conf import settings

app_name = 'ambition_ae'

urlpatterns = [
    path('admin/', ambition_ae_admin.urls),
    path('', RedirectView.as_view(url='admin/'), name='home_url'),
]


if settings.APP_NAME == 'ambition_ae':
    urlpatterns += [
        path('admin/', edc_action_item_admin.urls),
    ]
