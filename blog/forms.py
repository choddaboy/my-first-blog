"""Django Forms:
can: define one from scatch, or crate a ModelForm which will save
the result of the form to the model.


Lets create a form for our Post model. begin by creating this file (forms.py)"""

from django import forms  #imort forms model from Django

from .models import Post #import Post model from models

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'text',)

        """Here we have:
        1. PostForm(forms.ModelForm):
            created a model called PostForm which is a ModelForm (forms.ModelForm)

        2. Class Meta:
            Meta tells Django which model should be used (Post) to create this form (PostForm)

        3. field = ('title','text',):
            this says which fields (title and text) must enter PostForm. """
