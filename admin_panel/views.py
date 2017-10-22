from django.views import View
from django.views.generic import TemplateView, CreateView, ListView
from django.contrib import auth
from django.contrib import messages
from django import http
from django.urls import reverse
from admin_panel import forms
from blog_posting.models import Post


class LoginView(TemplateView):
    template_name = "admin/login.html"

    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        user_object = auth.authenticate(request, username=username, password=password)
        if user_object is None:
            messages.error(request, "Invalid credentials")
            return self.get(request)
        auth.login(request, user_object)
        messages.success(request, "You've been logged in")
        return http.HttpResponseRedirect(self.get_next_url(request))

    def get_next_url(self, request):
        if "next" in request.GET:
            return request.GET['next']
        else:
            return reverse("admin:Panel")


class Panel(TemplateView):
    template_name = "admin/panel.html"


class LogoutView(View):
    def get(self, request):
        auth.logout(request)
        return http.HttpResponseRedirect("/administration/login")


class CreatePost(CreateView):
    template_name = "admin/create_post.html"
    model = Post
    form_class = forms.CreatePost

    def get_success_url(self):
        return reverse("admin:ListPosts")

class ListPosts(ListView):
    template_name = "admin/list_posts.html"
    model = Post
