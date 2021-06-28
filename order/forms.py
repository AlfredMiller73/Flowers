from django import forms
from .models import Order


class OrderCreateForm(forms.ModelForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'ИМЯ *'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'ФАМИЛИЯ *'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'ЭЛЕКТРОННЫЙ АДРЕС *'}))
    address = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'АДРЕС *'}))
    postal_code = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'ПОЧТОВЫЙ ИНДЕКС *'}))
    city = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'ГОРОД *'}))
    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'email', 'address', 'postal_code',
                  'city']

