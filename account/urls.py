from django.urls import path
from . import views
from . views import SignUpView, MyLoginView

urlpatterns = [
    path('', views.account_view, name='account_view'),
    path("signup/",SignUpView.as_view(), name="signup"),
    path("login/", MyLoginView.as_view(), name="login"),
]