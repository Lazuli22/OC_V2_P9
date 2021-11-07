from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from .models import Ticket, User


# USerForm
class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = [
            "username",
            "email",
            "password1",
            "password2"
            ]

    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user


# TicketForm
class NewTicketForm(ModelForm):
    class Meta:
        model = Ticket
        fields = [
            "ticket",
            "description",
            "image"
            ]

    def save(self, user_id, commit=True,):
        ticket = super(NewTicketForm, self).save(commit=False)
        ticket.user_id = user_id
        if commit:
            ticket.save()
        return ticket
