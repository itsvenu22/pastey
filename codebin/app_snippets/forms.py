from django import forms
from .models import Snippet

class SnippetForm(forms.ModelForm):
    class Meta:
        model = Snippet
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={'placeholder': 'Paste your code or text here', 'rows': 10, 'cols': 80}),
        }
