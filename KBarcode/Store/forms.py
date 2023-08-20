from django import forms
from django.contrib.auth.models import User
from django.http import HttpRequest
from django.utils.text import slugify

from .models import Store


class NewPostForm(forms.ModelForm):
    class Meta:
        model = Store
        exclude = ["user", "slug"]
        widgets = {
            "name": forms.TextInput(attrs={"class": "input"}),
            "brand": forms.TextInput(attrs={"class": "input"}),
            "tags": forms.TextInput(attrs={"class": "input"}),
            "code": forms.Textarea(attrs={"class": "input"}),
            # "box_size": forms.IntegerField(attrs={"class": "input"}),
            "body": forms.TextInput(attrs={"class": "input"}),
            "video_link": forms.URLInput(attrs={"class": "input"}),
            "banner": forms.FileInput(attrs={"class": "input"}),
            "category": forms.Select(attrs={"class": "input"}),
            "gender": forms.Select(attrs={"class": "input"}),
            "age": forms.Select(attrs={"class": "input"}),
            "available": forms.CheckboxInput(),
        }

    def save(self, comit: bool, request):
        post: Store = super().save(commit=False)
        cd = self.cleaned_data
        title = cd["name"]
        post.slug = slugify(title)
        post.user = request.user

        if comit:
            post.save()

        return post
