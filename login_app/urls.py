from django.urls import path
from . import views

urlpatterns = [
    path('user/registration', views.register_user)
]
