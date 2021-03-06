from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from core.models import Ticket
from core.models import User


class Review(models.Model):
    """
    A class to represent a review
        ticket : foreigner key
            a id of ticket/post
        rating : float
            a rating linked to a review
        user : foreigner key
            a id of review's author
        headline : str
            a headline of a review
        body : str
            a body of a review
        time_created :
            the time when the review is created
    """
    ticket = models.ForeignKey(to=Ticket, on_delete=models.CASCADE)
    rating = models.PositiveSmallIntegerField(
        # validates that rating must be between 0 and 5
        validators=[MinValueValidator(0), MaxValueValidator(5)])
    user = models.ForeignKey(
        to=User, on_delete=models.CASCADE)
    headline = models.CharField(max_length=128)
    body = models.TextField(max_length=8192, blank=True)
    time_created = models.DateTimeField(auto_now_add=True)
