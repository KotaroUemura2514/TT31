from django import forms
from .models import book

class BookForm(forms.ModelsForm):
    class Meta:
        models=book
        fields=('title','text')

        widget={
            'title':forms.TextInput(attrs={'class':'bookTitle'}),#タイトル
            'text':forms.TextInput(attrs={'class':'bookText'}),#コメント
    
        }