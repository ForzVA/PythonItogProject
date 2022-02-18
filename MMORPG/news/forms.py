from django.forms import ModelForm, BooleanField, TextInput, Textarea, ChoiceField, CharField, Select
from .models import Post
from ckeditor_uploader.widgets import CKEditorUploadingWidget


class PostForm(ModelForm):
    text = CharField(widget=CKEditorUploadingWidget(),
                     label='Текст'
                     )
    category = ChoiceField(label='Категория',
                           choices=Post.CATEGORY_CHOICES,
                           widget=Select(attrs={'class': 'form-control'})
                           )
    title = CharField(label='Название',
                      widget=TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter the title'})
                      )
    class Meta:
        model = Post
        fields = ['title', 'text', 'category']

