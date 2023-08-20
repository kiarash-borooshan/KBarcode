from django import forms
from django.utils.text import slugify
from .models import Feature


class NewEmPostForm(forms.ModelForm):
    class Meta:
        model = Feature
        exclude = ["user", "slug"]
        widgets = {
            # TODO: add location to widget
            "geo_tag_photo": forms.FileInput(attrs={"class": "input"}),
            "Date": forms.DateInput(attrs={"class": "input"}),
            "name": forms.TextInput(attrs={"class": "input"}),
            "variety": forms.Select(attrs={"class": "input"}),
            "health_status": forms.Select(attrs={"class": "input"}),
            "disease_name": forms.Select(attrs={"class": "input"}),
            "solution": forms.Textarea(attrs={"class": "input"}),
        }

    def save(self, comit: bool, request):
        post: Feature = super().save(commit=False)
        cd = self.cleaned_data
        title = cd["name"]
        post.slug = slugify(title)
        post.user = request.user

        if comit:
            post.save()

        return post
