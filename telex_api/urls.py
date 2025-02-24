from django.contrib import admin
from django.urls import path
from telex_api.views import IntegrationJSONView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('interval-integration.json', IntegrationJSONView.as_view(), name='integration-json'),
]