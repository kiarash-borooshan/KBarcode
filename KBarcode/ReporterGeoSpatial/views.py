from django.contrib.auth.decorators import login_required
from django.core.serializers import serialize
from django.http import HttpResponse
from .models import IRN_adm1, Feature
from django.views.generic import TemplateView
from django.shortcuts import render, redirect
from .forms import NewEmPostForm

# Create your views here.


@login_required(login_url="account:login_em")
def home_page_view_dashboard(TemplateView):
    template_name = "index.html"
    return render(TemplateView,
                  "ReporterGeoSpatial/dashboard_em.html")


def county_datasets(request):
    counties = serialize("geojson", IRN_adm1.objects.all())
    return HttpResponse(counties, content_type="json")


def point_dataset(request):
    points = serialize("geojson", Feature.objects.all())
    return HttpResponse(points, content_type="json")


@login_required(login_url="ReporterGeoSpatial:login_em")
def create_new_em_post(request):
    if request.method == "POST":
        em_form = NewEmPostForm(data=request.POST)
        if em_form.is_valid():
            post = em_form.save(comit=True, request=request)
            post.save()

            return redirect("ReporterGeoSpatial:em_dashboard")

    else:
        em_form = NewEmPostForm()

    return render(request,
                  "ReporterGeoSpatial/create_new_em_post.html",
                  {"form": em_form})
