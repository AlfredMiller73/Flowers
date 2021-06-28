from django import forms
from .models import Comment
from django.db import models
from .models import Blog

class CommentForm (forms.ModelForm):
    class Meta:
        model = Comment # используемая модель
        fields = ('text',) # требуется заполнить только поле text
        labels = {'text': "Комментарий"} # метка к полю формы text
        
class BlogForm (forms.ModelForm):
    image = forms.FileField(label="Изображение")
    title = forms.CharField(label="Заголовок новости", widget=forms.TextInput(attrs={'class':'form-control require', 'placeholder':'Заголовок'}))
    description = forms.CharField(label="Краткое описание", widget=forms.Textarea(attrs={'class':'form-control', 'placeholder':'Краткое описание'}))
    content = forms.CharField(label="Полное содержание", widget=forms.Textarea(attrs={'class':'form-control', 'placeholder':'Полное содержание'}))
    class Meta:
        model = Blog #используемая модель
        fields = ('title', 'description', 'content', 'posted', 'author', 'image',)
        labels = {'title':"Заголовок",'description':"Краткое описание", 'content':"Содержание", 'posted':"Дата", 'author':"Автор", 'image':"Изображение",}