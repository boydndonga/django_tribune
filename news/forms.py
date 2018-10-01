from django import forms
from .models import Article

class NewArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        exclude = ['editor', 'pub_date']
        widgets = {
            'tags': forms.CheckboxSelectMultiple(),
        }