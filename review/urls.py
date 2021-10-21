from django.conf.urls import url
from . import views

urlpatterns = [
    url('modify/(?P<post_id>.*)', views.modify_post, name="modify_post"),
    url('delete/(?P<post_id>.*)', views.delete_post, name="delete_post"),
    url('', views.posts, name="posts"),
]
