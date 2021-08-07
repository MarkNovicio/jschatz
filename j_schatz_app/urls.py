from django.urls import path
from . import views
urlpatterns = [
    path('', views.index),
    path('about', views.about),
    path('contact', views.contact),
    path('user/contact', views.submit_user_message),
    path('success', views.success_page),
    path('user/post_challenge', views.post_challenge)
]