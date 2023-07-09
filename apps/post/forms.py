from django import forms
from .models import PostModel, CommentsModel


class PostForm(forms.ModelForm):

    class Meta:
        model = PostModel
        fields = '__all__'

class CommentsForm(forms.ModelForm):

    class Meta:
        model = CommentsModel
        fields = '__all__'
        widgets = {
            'post': forms.HiddenInput()
        }