
from rest_framework import viewsets
from rest_framework.response import Response
from blogs.models import User, Comment, Post, Category
from blogs.serializers import UserSerializer, CommentSerializer, PostSerializer, CategorySerializer

class  CategoryModelViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class=CategorySerializer

class  UserModelViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class=UserSerializer

class  PostModelViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class=PostSerializer

class  CommentModelViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class=CommentSerializer











