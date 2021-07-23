from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('user/registration', views.register_user)
]
