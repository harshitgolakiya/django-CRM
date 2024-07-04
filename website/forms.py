from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Record
from .choices import COUNTRY_CHOICES
# from django.forms import ModelForm


class RegisterForm(UserCreationForm):
    email = forms.EmailField(max_length=254,label="", widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Email Address'}) )

    first_name = forms.CharField(label="",max_length=30, widget=forms.TextInput(attrs={'class':'form-control','placeholder':'First Name'}))

    last_name = forms.CharField(label="",max_length=30, widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Last Name'}))

    username = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'class':'form-control','placeholder':'User Name'}))
    username.label = ''
    username.help_text =  '<span class="form-text text-muted"><small>Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.</small></span>'

    password1 = forms.CharField(label="",widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Password'}))
    password1.help_text = '<ul class="form-text text-muted small"><li>Your password can\'t be too similar to your other personal information.</li><li>Your password must contain at least 8 characters.</li><li>Your password can\'t be a commonly used password.</li><li>Your password can\'t be entirely numeric.</li></ul>'

    password2 = forms.CharField(label="",widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Confirm Password'}))
    password2.help_text = '<span class="form-text text-muted"><small>Enter the same password as before, for verification.</small></span>'	


    class meta:
        model = User
        fields = ('username','first_name','last_name','email','password1','password2')

class RecordForm(forms.ModelForm):
    class Meta:
        model = Record
        fields = ['first_name', 'last_name', 'email', 'phone', 'address', 'city', 'state', 'country']

    def __init__(self, *args, **kwargs):
        super(RecordForm, self).__init__(*args, **kwargs)
        self.fields['country'].choices = COUNTRY_CHOICES
        self.fields['first_name'].widget.attrs['class'] = 'form-control'
        self.fields['last_name'].widget.attrs['class'] = 'form-control'
        self.fields['email'].widget.attrs['class'] = 'form-control'
        self.fields['phone'].widget.attrs['class'] = 'form-control'
        self.fields['address'].widget.attrs['class'] = 'form-control'
        self.fields['city'].widget.attrs['class'] = 'form-control'
        self.fields['state'].widget.attrs['class'] = 'form-control'
        self.fields['country'].widget.attrs['class'] = 'form-control'


