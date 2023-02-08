from django import forms

from .models import Comment

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        exclude = ["post"]
        labels = {
            "user_name": "Your name",
            "user_email": "Your email",
            "comment_text": "Your comment",
        }
        error_messages = {
            "user_name": {
                "max_length": "Please enter a shorter name",
            },
            "comment_text": {
                "max_length": "Please enter a shorter comment",
            }
        
        }
