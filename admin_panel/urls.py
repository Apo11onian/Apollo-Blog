from django.urls import path
from . import views
from django.views.generic import RedirectView


urlpatterns = [
    path('login/', views.LoginView.as_view(), name="LoginPage"),
    path('panel', views.Panel.as_view(), name="Panel"),
    path('', RedirectView.as_view(url="login"), name="LoginPage"),
]
