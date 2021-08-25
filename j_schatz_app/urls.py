from django.urls import path
from . import views
urlpatterns = [
    path('', views.index),
    path('about', views.about),
    path('contact', views.contact),
    path('user/contact', views.submit_user_message),
    path('success', views.success_page),
    path('post_challenge', views.post_challenge),
    path('post_challenge/challenges', views.challenge),
    path('post_challenge/coding_challenges/<int:challenge_id>', views.single_coding_challenge),
    path('post_challenge/challenge_publisher/<int:publisher_id>', views.code_publisher),
    path('post_challenge/coding_challenges/<int:challenge_id>/delete', views.delete_challenge),
    path('users/update', views.update_user)
]