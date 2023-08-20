# from django.db import models
from django.contrib.auth.models import User
from django.contrib.gis.db import models


class HealthStatus(models.Model):
    name = models.CharField(max_length=255)
    objects = models.Manager()

    def __str__(self):
        return self.name


class Variety(models.Model):
    name = models.CharField(max_length=255)
    objects = models.Manager()

    def __str__(self):
        return self.name


class DiseaseName(models.Model):
    name = models.CharField(max_length=255)
    objects = models.Manager()

    def __str__(self):
        return self.name


class Feature(models.Model):
    user = models.ForeignKey(User,
                             on_delete=models.CASCADE,
                             related_name="em_user",
                             blank=True, null=True)
    location = models.PointField(srid=4326)
    geo_tag_photo = models.ImageField(upload_to="geoTag_Image",
                                      blank=True, null=True)
    Date = models.DateField(blank=True, null=True)
    name = models.CharField(max_length=20)
    variety = models.CharField(max_length=255,
                               blank=True, null=True)
    health_status = models.ForeignKey(HealthStatus,
                                      on_delete=models.CASCADE,
                                      related_name="health_status",
                                      blank=True, null=True)

    disease_name = models.CharField(max_length=255,
                                    blank=True, null=True)
    slug = models.SlugField(blank=True, null=True)

    solution = models.TextField(blank=True, null=True)

    objects = models.Manager()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Feature'


class IRN_adm1(models.Model):
    id_0 = models.BigIntegerField()
    iso = models.CharField(max_length=3)
    name_0 = models.CharField(max_length=75)
    id_1 = models.BigIntegerField()
    name_1 = models.CharField(max_length=75)
    type_1 = models.CharField(max_length=50)
    engtype_1 = models.CharField(max_length=50)
    nl_name_1 = models.CharField(max_length=50, blank=True, null=True)
    varname_1 = models.CharField(max_length=150, blank=True, null=True)
    geom = models.MultiPolygonField()

    objects = models.Manager()

    def __str__(self):
        return self.name_1

    class Meta:
        verbose_name = 'countie'
