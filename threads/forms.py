from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('name', 'message')

class AbcForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('name', 'message', 'quote')
        widgets = {
            'name' : forms.TextInput(attrs={'size': 40}),
            'message' : forms.TextInput(attrs={'size': 40}),
            # 'message' : forms.TextInput(attrs={'cols': 80, 'rows': 20 }),
            'quote' : forms.HiddenInput(),
        }