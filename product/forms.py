from django import forms
from .models import Review
from django.db import models

class ReviewProduct (forms.ModelForm):
    class Meta:
        model = Review # используемая модель
        fields = ('text',) # требуется заполнить только поле text
        labels = {'text': "Комментарий"} # метка к полю формы text

