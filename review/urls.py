from django.conf.urls import url
from django.urls import path
from . import views

app_name = "review"

urlpatterns = [
    path('update/<int:id_review>/post/<int:id_post>', views.update_review, name="update_review"),
    url('create/(?P<id_post>.*)',
        views.create_review_post, name="create_review_post"),
    url('', views.create_review, name="create_review"),
]
