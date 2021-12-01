from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    """
    A class to represent a user of the software
    """
    pass


class Ticket(models.Model):
    """
    A class to represent a ticket to post
        ticket : str
            a name of the ticket
        description : str
            a description of the ticket
        image : str
            a picture of the ticket
        user : foreigner key
            a id of ticket's author
        time_created :
            the time when the ticket is created
    """
    ticket = models.CharField(max_length=128)
    description = models.TextField(max_length=2048, blank=True)
    user = models.ForeignKey(
                            to=User,
                            on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/', blank=True)
    time_created = models.DateTimeField(auto_now_add=True)
