from cgitb import lookup
from pyexpat import model
from tkinter import Widget
from turtle import width
from unittest import mock
from django_filters import FilterSet, DateTimeFilter, BooleanFilter, CharFilter, ChoiceFilter
from .models import Comment
from django.forms import ModelForm, BooleanField, TextInput, Textarea, ChoiceField, CharField, Select, DateInput
from django.forms import DateInput


class ResponseFilter(FilterSet):  
    time_comment = DateTimeFilter(widget=DateInput(attrs={'type': 'date', 'style': 'border: 2px solid orange; border-radius: 15px'}),
                                     lookup_expr='gte', label='Дата создания(>= сегодня)')
    status_comment = BooleanFilter(label='Статус комментария')
    text_comment = CharFilter(lookup_expr='icontains', label='Текст комментария',widget=TextInput(attrs={'style': 'border: 2px solid orange; border-radius: 15px', 'placeholder': 'Введите текст'}))


    class Meta:
        model = Comment
        fields = {'text_comment',
                'time_comment',
                'status_comment',
        }