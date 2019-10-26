from django.urls import path
from django.views.generic import TemplateView

from blog import views, apis

urlpatterns = [
    path('', views.home),
    path('posts/<str:pk>/', apis.PostAPI.as_view())
]
