from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from reader.models import BlogPost
from reader.serializers import BlogPostListSerializer

# Create your views here.

@api_view(['GET'])
def readpost(request,pk):
    post = BlogPost.objects.get(id=pk)
    serializer = BlogPostListSerializer(post)
    return Response(serializer.data)
