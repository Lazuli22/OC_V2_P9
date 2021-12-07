from django.urls import path, re_path

from . import views

urlpatterns = [
    re_path('unsubscribe/(?P<username>.*)', views.unsubscribe, name="unsubscribe"),
    path('search/', views.search, name="search"),
    path('', views.listing, name="listing"),
]
