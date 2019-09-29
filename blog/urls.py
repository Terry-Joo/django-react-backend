from django.urls import path
from django.views.generic import TemplateView

url_patterns = [
    path('', TemplateView.as_view(template_name='blog/index.html'))
]