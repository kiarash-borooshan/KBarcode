from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("core.url")),
    path("account/", include("Account.url")),
    path("spatial/", include("ReporterGeoSpatial.url", namespace="reporterGeoSpatial")),
    path("store", include("Store.url", namespace="store")),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
