from django.urls import path
from . import views
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [

    path('', views.home, name='home'),
    path('subscribe', views.subscribe, name='subscribe'),
    path('subscribe_validation', csrf_exempt(views.subscribe_validation), name='subscribe_validation'),
]