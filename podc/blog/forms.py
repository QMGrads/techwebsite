from django import forms

from .models import Form

class PostForm(forms.ModelForm):
    class Meta:
	    model = Form
	    fields = ('title', 'author', 'article_title')