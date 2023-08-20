from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("core.url")),
    path("account/", include("Account.url")),
    path("spatial/", include("ReporterGeoSpatial.url", namespace="reporterGeoSpatial")),

]
