from django import forms
from core.models import User


class UserForm(forms.Form):
    user_list = forms.ModelChoiceField(
        to_field_name="username",
        queryset=User.objects.all().order_by("username"))