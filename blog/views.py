from django.shortcuts import render

from blog.models import Menu, Post


def index(request):
    return render(request, 'blog/index.html')


def home(request):
    response = {'user': request.user}
    if request.user.is_superuser:
        response.update(posts=Post.objects.all())
    elif request.user.is_staff:
        response.update(posts=Post.staff_posts.all())
    else:
        response.update(posts=Post.public_posts.all())
    return render(request, 'blog/home.html', response)
