from django.contrib import admin
from .models import *
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget


class PostAdminForm(forms.ModelForm):
    text = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = Post
        fields = ('title', 'text', 'author', 'category')


class PostAdmin(admin.ModelAdmin):
    form = PostAdminForm


class CommentAdminForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('user_comment', 'text_comment', 'post_comment',)


class CommentAdmin(admin.ModelAdmin):
    form = CommentAdminForm


admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)

