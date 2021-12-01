from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from .models import Ticket, User


class NewUserForm(UserCreationForm):
    """
        A class to represent a form for a new person

        Attributes
        ----------
        username :str
        email : str
        password1 : str
        password2 : str

    """
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


class NewTicketForm(ModelForm):
    """
        A class to represent a form for a new ticket

        Attributes
        ----------
        ticket :str
            name of ticket
        description : str
            description of ticket
        image : im
            picture of ticket

    """
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
