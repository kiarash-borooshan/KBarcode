from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.core.files.uploadedfile import InMemoryUploadedFile
from .models import Profile, EmProfile


class RegisterForm(UserCreationForm):
    """ form for KBarcode Users """
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
        widgets = {
            "username": forms.TextInput(attrs={'class': 'input',
                                               "placeholder": "نام مغازه خود را وارد فرمایید"}),
            "email": forms.EmailInput(attrs={'class': 'input',
                                             "placeholder": "ایمیل خود را وارد فرمایید"}),
            "password1": forms.PasswordInput(attrs={'class': 'input',
                                                    "placeholder": "پسورد"}),
            "password2": forms.PasswordInput(attrs={'class': 'input',
                                                    "placeholder": "تکرار پسورد"}),
        }


class RegisterEmForm(UserCreationForm):
    """ form for Ai Earth Monitor user """
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        widgets = {
                    "username": forms.TextInput(attrs={'class': 'input',
                                                       "placeholder": "نام کاربری خود را وارد فرمایید"}),
                    "email": forms.EmailInput(attrs={'class': 'input',
                                                     "placeholder": "ایمیل خود را وارد فرمایید"}),
                    "password1": forms.PasswordInput(attrs={'class': 'input',
                                                            "placeholder": "پسورد"}),
                    "password2": forms.PasswordInput(attrs={'class': 'input',
                                                            "placeholder": "تکرار پسورد"}),
                }


class RegisterProfileForm(forms.ModelForm):
    """ profile form for KBarcode user """
    class Meta:
        model = Profile
        exclude = ["user"]
        widgets = {
            "phone_number": forms.TextInput(attrs={"class": "input",
                                                   "placeholder": "شماره موبایل خود را بدین فرمت وارد نمایید: به "
                                                                  "عنوان مثال ۰۹۳۳۴۲۲۷۶۷۹"}),
            "photo": forms.FileInput(attrs={"class": "input",
                                            "placeholder": "تصویری از مغازه خود بارگذاری نمایید"})
        }

    def clean_photo(self):
        cd = self.cleaned_data

        try:
            photo: InMemoryUploadedFile = cd["photo"]
            photo_name = photo.name
            photo_format = photo_name.rsplite(".", 1)[-1]
            extensions = ["jpeg", "jpg", "png"]

            if photo_format not in extensions:
                raise forms.ValidationError("تصویر شما از فرمت مورد نظر نمی‌باشد")

        except(Exception, ):
            pass

        return cd["photo"]


class RegisterEmProfileForm(forms.ModelForm):
    """for Ai Earth Monitor """
    class Meta:
        model = EmProfile
        exclude = ["user"]
        widgets = {
            'phone_number': forms.TextInput(attrs={'class': 'input',
                                                   "placeholder": "شماره موبایل: به عنوان مثال ۰۹۳۳۴۲۲۷۶۷۹"}),
        }


class LoginForm(forms.Form):
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            "class": "input"
        })
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={"class": "input"})
    )


class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']
        widgets = {
            "username": forms.TextInput(attrs={'class': 'input',
                                               "placeholder": "نام مغازه خود را وارد فرمایید"}),
            "email": forms.EmailInput(attrs={'class': 'input',
                                             "placeholder": "ایمیل خود را وارد فرمایید"})
        }


class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user']
        widgets = {
            'phone_number': forms.TextInput(attrs={'class': 'input',
                                                   "placeholder": "شماره موبایل: به عنوان مثال ۰۹۳۳۴۲۲۷۶۷۹"}),
        }

        labels = {
            "photo": "تصویری از مغازه خود بارگذاری فرمایید"
        }


class ProfileEmEditForm(forms.ModelForm):
    class Meta:
        model = EmProfile
        exclude = ['user']
        widgets = {
            'phone_number': forms.TextInput(attrs={'class': 'input',
                                                   "placeholder": "شماره موبایل: به عنوان مثال ۰۹۳۳۴۲۲۷۶۷۹"})
        }


class PasswordEditForm(forms.Form):
    old_password = forms.CharField(
        label="your old password",
        widget=forms.PasswordInput(attrs={"class": "input"})
    )
    new_password = forms.CharField(
        label="new password",
        widget=forms.PasswordInput(attrs={"class": "input"})
    )
    new_password2 = forms.CharField(
        label="confirm password",
        widget=forms.PasswordInput(attrs={"class": "input"})
    )


class DeleteForm(forms.Form):
    password = forms.CharField(
        label="confirm your password",
        widget=forms.PasswordInput(attrs={"class": "input"}),
        required=True,
        help_text="your account need delete"
    )


class ThemeForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ("theme", )
        widgets = {
            "theme": forms.RadioSelect()
        }
