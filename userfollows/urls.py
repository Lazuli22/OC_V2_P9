from django.urls import path

from . import views

urlpatterns = [
    path('unsubscribe/(?P<username>.*)', views.unsubscribe, name="unsubscribe"),
    path('search/', views.search, name="search"),
    path('', views.listing, name="listing"),
]
