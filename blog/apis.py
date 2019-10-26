from rest_framework import generics

from blog.models import Post
from blog.serializers import PostSerializer


class PostAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def get(self, request, *args, **kwargs):
        if request.user.is_superuser:
            self.queryset = Post.objects.all()
        elif request.user.is_staff:
            self.queryset = Post.staff_posts.all()
        else:
            self.queryset = Post.public_posts.all()
        return self.retrieve(request, *args, **kwargs)
