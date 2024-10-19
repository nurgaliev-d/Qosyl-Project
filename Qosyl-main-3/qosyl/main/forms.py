from django import forms

# from users.models import Profile
from .models import  Comment


# class PostForm(forms.ModelForm):
#     class Meta:
#         model = Post
#         fields = ['title', 'content']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']


# class ProfileForm(forms.ModelForm):
#     class Meta:
#         model = Profile
#         fields = ['bio', 'profile_pic']
