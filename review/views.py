from django.shortcuts import render, redirect
from core.models import Ticket, User
from core.forms import NewTicketForm
from review.models import Review
from .forms import NewReviewForm


def create_review(request):
    if request.method == "POST":
        ticket_form = NewTicketForm(request.POST, request.FILES)
        review_form = NewReviewForm(request.POST)
        if ticket_form.is_valid() and review_form.is_valid():
            ticket = ticket_form.save(request.user.id)
            user = User.objects.filter(username=request.user)
            review_form.save(review_id=None, user=user[0], ticket=ticket)
        return redirect("home")
    else:
        ticket_form = NewTicketForm()
        review_form = NewReviewForm()
        return render(
            request=request,
            template_name="review.html",
            context={
                    "ticket_form": ticket_form,
                    "review_form": review_form
                    }
        )


# Comment est ce que je peux mutualiser les 2 méthodes...
def create_review_post(request, id_post):
    ticket = Ticket.objects.filter(id=id_post)
    if request.method == "GET":
        review_form = NewReviewForm()
        return render(
                request=request,
                template_name="review_create_post.html",
                context={
                    "ticket_form_id": ticket[0].id,
                    "ticket_form": ticket,
                    "review_form": review_form}
            )
    else:
        review_form = NewReviewForm(request.POST)
        score = request.POST.get('val')
        print(score)
        review_form.rating = score
        if review_form.is_valid():
            user = User.objects.filter(username=request.user)
            print(score)
            review_form.save(review=None, user=user[0], ticket=ticket[0])
        return redirect("home")


def update_review(request, **args):
    review_toUpdate = Review.objects.get(id=args["id_review"])
    post_reviewed = Ticket.objects.get(id=args["id_post"])
    if request.method == "GET":
        review_form = NewReviewForm(instance=review_toUpdate)
        return render(
                request=request,
                template_name="update_review.html",
                context={
                    "id_review": review_toUpdate.id,
                    "id_ticket": post_reviewed.id,
                    "review_form": review_form,
                    "ticket_form": post_reviewed
                    }
            )
    elif request.method == "POST":
        review_form = NewReviewForm(request.POST)
        if review_form.is_valid():
            user = User.objects.filter(username=request.user)
            review_toUpdate.headline = review_form.cleaned_data.get("headline")
            review_toUpdate.body = review_form.cleaned_data.get("body")
            review_toUpdate.rating = review_form.cleaned_data.get("rating")
            review_toUpdate.ticket_id = args["id_post"]
            review_toUpdate.user_id = user[0].id
            review_toUpdate.save()
        return redirect("home")
