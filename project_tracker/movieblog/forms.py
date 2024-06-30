from django import forms
from .models import CommentModel
from .models import UserFilmList

class SearchForm(forms.Form):
    query = forms.CharField(max_length=100,
                            widget=forms.TextInput(
                                attrs={
                                    'class': 'form-control me-2 mx-1',
                                    'placeholder': 'Что ищем?',
                                }
                            ))

    def clean_query(self):
        query = self.cleaned_data['query']
        cleaned_query = " ".join(query.split())
        return cleaned_query
    
class CommentForm(forms.ModelForm):  
    content = forms.CharField(  
        widget=forms.Textarea(  
            attrs={  
                "class": "form-control",  
                "placeholder": "Введите текст комментария",  
                "rows": 5  
            }  
        ),  
    )  

    class Meta:  
        model = CommentModel  
        fields = ("content",)

class UserFilmListForm(forms.ModelForm):
    class Meta:
        model = UserFilmList
        fields = ['film', 'list_type']