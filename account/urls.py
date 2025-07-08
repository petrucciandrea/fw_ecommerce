from django.urls import path
from . import views
from . views import SignUpView, MyLoginView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.account_view, name='account_view'),
    path("signup/",SignUpView.as_view(), name="signup"),
    path("login/", MyLoginView.as_view(), name="login"),
    path('password_change_form/', auth_views.PasswordChangeView.as_view(template_name='registration/password_change_form.html'), name='password_change_form'),
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(template_name='registration/password_change_done.html'), name='password_change_done'),

    path('password_reset/', auth_views.PasswordResetView.as_view(
        template_name='registration/password_reset.html',
        email_template_name='registration/password_reset_email.html',
        subject_template_name='registration/password_reset_subject.txt',
        success_url='/password_reset/done/'
    ), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(
        template_name='registration/password_reset_done.html'
    ), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
        template_name='registration/password_reset_confirm.html',
        success_url='/reset/done/'
    ), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(
        template_name='registration/password_reset_complete.html'
    ), name='password_reset_complete'),
]