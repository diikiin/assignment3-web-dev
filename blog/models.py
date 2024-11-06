from django.db import models


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Post(models.Model):
    author = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    content = models.TextField(max_length=1024)
    published_at = models.DateTimeField(auto_now_add=True)
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)
    categories = models.ManyToManyField(Category, related_name='posts')

    def __str__(self):
        return f'Author: {self.author}, Title: {self.title}'


class Comment(models.Model):
    author = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')

    def __str__(self):
        return f'Author: {self.author}, Post: {self.post}'
