from django.urls import path
from . import views

urlpatterns = [
    path('registration', views.registration_form),
    path('user/registration', views.register_user),
    path('login_page', views.login_page)
]
