from django import forms
from . import models

class CreatePost(forms.ModelForm):
    class Meta:
        model = models.Match
        fields = ['title','body','slug','thumb']
        
class Comment(forms.ModelForm):
    class Meta:
        model = models.Comment
        fields = ['comment']