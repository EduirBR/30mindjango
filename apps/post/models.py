from django.db import models

# Create your models here.

class PostModel(models.Model):

    title = models.CharField(max_length=70, unique=True)
    author = models.CharField(max_length=20)
    description = models.TextField()

class CommentsModel(models.Model):

    author = models.CharField(max_length=20)
    description = models.TextField()
    post = models.ForeignKey(PostModel, on_delete=models.CASCADE)
