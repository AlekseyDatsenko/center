from django.forms import ModelForm
from .models import Comments, Post
from django.db import models

class CommentForm(ModelForm):
    class Meta:
        model = Comments
        fields = ('text',)
        
class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'text',)
