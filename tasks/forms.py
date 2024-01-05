from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'important']
        widgets= {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'escribe un titulo'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'escribe una descripcion'}),
            'importan': forms.CheckboxInput(attrs={'class': 'form-check-input m-auto'})
        }