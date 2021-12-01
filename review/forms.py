from django.forms import ModelForm
from .models import Review


class NewReviewForm(ModelForm):
    """
        A class to represent a form for a new review

        Attributes
        ----------
        healdine :str
        body : str
        rating : str
    """
    class Meta:
        model = Review
        fields = [
            "headline",
            "body",
            "rating",
            ]

    def save(self, user, ticket, review_id, commit=True,):
        if review_id is None:
            review = super(NewReviewForm, self).save(commit=False)
        else:
            review = Review.objects.get(id=review_id)
        review.user = user
        review.ticket = ticket
        if commit:
            review.save()
        return review
