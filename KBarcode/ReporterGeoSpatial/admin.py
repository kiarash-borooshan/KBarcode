from django.contrib import admin
from leaflet.admin import LeafletGeoAdmin
from .models import Feature, IRN_adm1, HealthStatus
# Register your models here.


@admin.register(Feature)
class IncidenceDecor(LeafletGeoAdmin):
    list_display = ("name", "location")
    prepopulated_fields = {
        "slug": ["name", "variety", "disease_name"]
    }


@admin.register(HealthStatus)
class HealthStatusDecore(LeafletGeoAdmin):
    list_display = ("name", )


@admin.register(IRN_adm1)
class CountiesDecor(LeafletGeoAdmin):
    list_display = ("name_1", "varname_1")

