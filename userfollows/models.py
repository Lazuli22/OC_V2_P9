from django.db import models
from core.models import User


class UserFollows(models.Model):
    """
        A class to represent new userFollow

        Attributes
        ----------
        to :Foreign key to User
        followed_user : Foreign key to Followed user
    """
    user = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE,
        related_name='following')
    followed_user = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE,
        related_name='followed_by'
    )

    class Meta:
        # ensures we don't get multiple UserFollows instances
        # for unique user-user_followed pairs
        unique_together = ('user', 'followed_user', )
