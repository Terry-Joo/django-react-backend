from ckeditor.widgets import CKEditorWidget
from django import forms
from django.contrib import admin

from blog.models import Post, Menu


class PostForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = Post
        fields = ['title', 'scope', 'allow_reply', 'writer', 'content']


class PostAdmin(admin.ModelAdmin):
    form = PostForm


class MenuAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'super_menu', 'index', 'updated_at']


admin.site.register(Post, PostAdmin)
admin.site.register(Menu, MenuAdmin)
