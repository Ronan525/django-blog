from django import forms
from .models import Comment



class CommentForm(forms.ModelForm):
    """
    A form for users to submit comments on a :model:`blog.Post`.
    """
    class Meta:
        model = Comment
        fields = ('body',)