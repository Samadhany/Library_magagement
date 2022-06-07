from django.core import validators
from django import forms
from .models import User



class BookRegistration(forms.ModelForm):
 class Meta:
  model = User
  fields = ['Book_Name', 'title','author', 'summary','language','total_copies','available_copies']
  widgets = {
   'Book_Name': forms.TextInput(attrs={'class':'form-control'}),
   'title': forms.TextInput(attrs={'class':'form-control'}),
   'author': forms.TextInput(attrs={'class':'form-control'}),
   'summary': forms.TextInput(attrs={'class':'form-control'}),
   'language': forms.TextInput(attrs={'class':'form-control'}),
   'total_copies': forms.TextInput(attrs={'class':'form-control'}),
   'available_copies': forms.Select(attrs={'id':'COMP_CHOICES'}),
   
  }