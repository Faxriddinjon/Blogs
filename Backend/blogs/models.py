from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name=models.CharField(max_length=45)

    def __str__(self):
        return f"{self.name}"

class Post(models.Model):
    title=models.CharField(max_length=45)
    user=models.ForeignKey(User,related_name='user', on_delete=models.CASCADE)
    body=models.TextField()
    category=models.ForeignKey(Category,related_name='category', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title}"

class Comment(models.Model):
    body=models.TextField()
    post=models.ForeignKey(Post,related_name='post', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.post.title}"