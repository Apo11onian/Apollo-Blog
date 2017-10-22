from django.urls import path
from . import views
from django.views.generic import RedirectView
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('logout', views.LogoutView.as_view(), name="Logout"),
    path('login/', views.LoginView.as_view(), name="LoginPage"),
    path('panel', login_required(views.Panel.as_view()), name="Panel"),
    path('posts/create', login_required(views.CreatePost.as_view()), name="CreatePost"),
    path('', login_required(RedirectView.as_view(url="login")), name="LoginPage"),
]
