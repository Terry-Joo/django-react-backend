from rest_framework import serializers, viewsets

from blog.models import Post


# class PostSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Post
#         fields = ['title', 'writer', 'created_at', 'updated_at', 'content']
#
#
# class PostViewSet(viewsets.ModelViewSet):
#     queryset = Post.objects.filter(is_hidden=False)
#     serializer_class = PostSerializer
