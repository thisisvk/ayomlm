from django import forms
from testapp.models import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=True)
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({
            "type":"text",
            "class":"form-control", 
            "name":"name", 
            'placeholder':"Enter username",
            'required':'',
            'id':'username',
        })
        self.fields['email'].widget.attrs.update({
            "type":"text",
            "class":"form-control", 
            "name":"mail", 
            'placeholder':"Enter email address",
            'required':''
        })
        self.fields['password1'].widget.attrs.update({
            "type":"password",
            "class":"form-control pe-5 password-input", 
            "name":"pass1", 
            'placeholder':"Password",
            'required':'',
            'aria-describedby':"passwordInput",
            'id':'password-input',
            'onpaste':'return false',
            'pattern':"(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{8,}",
        })
        self.fields['password2'].widget.attrs.update({
            "type":"password",
            "class":"form-control pe-5 password-input", 
            "name":"pass2", 
            'placeholder':"Confirm Password",
            'required':'',
            'aria-describedby':"passwordInput",
            'id':'password-input',
            'onpaste':'return false',
            'pattern':"(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{8,}",
        })
    class Meta:
        model = User
        fields = ['username','email','password1','password2']
    def save(self, commit=True):
        user = super(SignUpForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user
class LeftForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = Left
        fields = ['firstname', 'lastname','email','phone','city','state','country','referal','password','package']
        
class RightForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = Right
        fields = ['firstname', 'lastname','email','phone','city','state','country','referal','password','package']

