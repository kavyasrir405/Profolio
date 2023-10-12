from django import forms
from django.db import models
from django.contrib.auth.models import User

# models.py
from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField(default='email@example.com')
    name = models.CharField(max_length=15, default='Default_name')
    title = models.TextField(max_length=255, default='Ex:- Instagram, Linked-in')
    bio = models.TextField(max_length=255, default='Tell us about yourself')
    avatar = models.ImageField(default='images/def.jpg',upload_to='avatars/', null=True, blank=True)

    def __str__(self):
        return f"{self.user.username}'s profile"
class AvatarUploadForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['avatar']