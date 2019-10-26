from rest_framework import serializers, viewsets, generics

from blog.models import Post


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['title', 'writer', 'scope', 'created_at', 'updated_at', 'content']
