from django import forms
from blog_posting import models
from datetime import datetime


class CreatePost(forms.ModelForm):
    class Meta:
        model = models.Post
        exclude = ("created_at", "modified_at", "published")

    def save(self, commit=True):
        blog_post_object = super(CreatePost, self).save(commit=False)
        assert isinstance(blog_post_object, models.Post)
        blog_post_object.published = False
        blog_post_object.modified_at = datetime.now()
        blog_post_object.created_at = datetime.now()
        blog_post_object.save()
        return blog_post_object


class CreateTag(forms.ModelForm):
    class Meta:
        model = models.Tag
        fields = ("text", )