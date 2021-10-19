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
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.conf import settings
from core import views


urlpatterns = [
    path('', views.connection, name="connection"),
    url('register/', views.register_request, name="register_request"),
    url('login/', views.login_request, name="login_request"),
    path('home/', views.home, name="home"),
    path('ticket/', views.create_ticket, name="create_ticket"),
    url('userfollows/', include('userfollows.urls')),
    url('review/', include('review.urls')),
    url('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(
                    settings.MEDIA_URL,
                    document_root=settings.MEDIA_ROOT)
