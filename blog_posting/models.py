from django.db import models


class Tag(models.Model):
    text = models.CharField(max_length=64)


class Post(models.Model):
    title = models.CharField(max_length=280)
    abstract = models.TextField()
    published = models.BooleanField(default=False)
    created_at = models.DateTimeField()
    modified_at = models.DateTimeField()


class PostContent(models.Model):
    class Meta:
        unique_together = (("post", "order",),)

    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    content_type = models.CharField(max_length=16, choices=[])
    tags = models.ManyToManyField(Tag)
    order = models.IntegerField(default=0)


class TextContent(PostContent):
    text = models.TextField()


class ImageContent(PostContent):
    image = models.ImageField()
    alt = models.CharField(max_length=64)


class CodeContent(PostContent):
    code = models.TextField()
    language = models.CharField(max_length=32)
