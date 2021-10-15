from django.conf.urls import url
from django.urls import path

from . import views

urlpatterns = [
    url('unsubscribe/(?P<username>.*)', views.unsubscribe, name="unsubscribe"),
    path('search/', views.search, name="search"),
    url('', views.listing, name="listing"),
]
