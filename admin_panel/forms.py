from django import forms
from blog_posting import models


class CreatePost(forms.ModelForm):
    class Meta:
        model = models.Post
        exclude = ("created_at", "modified_at", "published")



