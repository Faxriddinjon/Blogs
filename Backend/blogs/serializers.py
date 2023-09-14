from rest_framework import serializers
from blogs.models import Category, Post, Comment, User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['username','email','password']


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=Category
        fields=['name']

class PostSerializer(serializers.ModelSerializer):
    user=UserSerializer(many=False)
    category=CategorySerializer(many=False)
    class Meta:
        model=Post
        fields=['title','user','body','category']

class CommentSerializer(serializers.ModelSerializer):
    post=PostSerializer(many=False)
    class Meta:
        model=Comment
        fields=['body','post']

