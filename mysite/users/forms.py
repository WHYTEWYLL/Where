from django import forms 
from django.contrib.auth.forms import UserCreationForm
from .models import Middlepoint , MyUsers

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = MyUsers
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', 'localitation')

class New_middlepoint(forms.ModelForm):
    class Meta:
        model = Middlepoint
        fields = [
            'point_1',
            'point_2',
            'type_of_point'
        ]