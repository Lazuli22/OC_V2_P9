"""LitReview URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from django.conf.urls.static import static
from django.conf import settings
from core import views


urlpatterns = [
    path('', views.connection, name="connection"),
    path('logout/', views.logout, name="logout"),
    path('home/', views.home, name="home"),
    path('ticket/', views.create_ticket, name="create_ticket"),
    path('posts/', include('core.urls')),
    path('userfollows/', include('userfollows.urls')),
    path('review/', include('review.urls', namespace="review")),
    path('admin/', admin.site.urls),
]

urlpatterns += static(
                settings.MEDIA_URL,
                document_root=settings.MEDIA_ROOT)
urlpatterns += static(
                settings.STATIC_URL,
                document_root=settings.STATIC_ROOT)
