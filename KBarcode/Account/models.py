from django.contrib.auth.models import User
# from django.db import models
from django.contrib.gis.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
"""" !!! cannot recognize in pycharm but it works """
from phonenumber_field.modelfields import PhoneNumberField


class Profile(models.Model):
    """ for KBarcode """
    Theme_Choices = (
        ("is-light", "Light"),
        ("is-success", "Green"),
        ("is-warning", "Yellow"),
        ("is-info", "Blue"),
        ("is-dark", "Dark")
    )

    user = models.OneToOneField(User,
                                on_delete=models.CASCADE,
                                related_name="profile")
    # phone_number = PhoneNumberField()
    phone_number = PhoneNumberField(blank=True, null=True)
    photo = models.ImageField(blank=True, null=True)
    location = models.PointField(blank=True, null=True)
    theme = models.CharField(max_length=50,
                             choices=Theme_Choices,
                             default="is-success")
    objects = models.Manager()

    def __str__(self):
        return f"{self.user}"


@receiver(post_save, sender=User)
def create_profile(sender, **kwargs):
    user = kwargs.get("instance")
    created = kwargs.get("created")

    if created:
        profile = Profile(user=user)
        profile.save()


class EmProfile(models.Model):
    user = models.OneToOneField(User,
                                on_delete=models.CASCADE,
                                related_name="Em_profile")
    phone_number = PhoneNumberField(blank=True, null=True)

    objects = models.Manager()

    def __str__(self):
        return f"{self.user}"


@receiver(post_save, sender=User)
def create_em_user_profile(sender, **kwargs):
    user = kwargs.get("instance")
    created = kwargs.get("created")

    if created:
        profile = EmProfile(user=user)
        profile.save()
