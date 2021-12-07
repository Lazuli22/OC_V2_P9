from django.urls import path, re_path
from . import views

app_name = "review"

urlpatterns = [
    path('update/<int:id_review>/post/<int:id_post>', views.update_review, name="update_review"),
    re_path('create/(?P<id_post>.*)',
        views.create_review_post, name="create_review_post"),
    path('', views.create_review, name="create_review"),
]
