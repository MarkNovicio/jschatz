from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('registration', views.registration_form),
    path('user/registration', views.register_user),
    path('login_page', views.login_page),
    path('user/login', views.login),
    #path('forgot_password_page', views.forgot_password_page),
    path('reset_password/', auth_views.PasswordChangeView.as_view()),
    #path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(), name="password_reset_done"),
    #path('reset_<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name ="password_reset_confirm"),
    #path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(), name ="password_reset_complete")
]
