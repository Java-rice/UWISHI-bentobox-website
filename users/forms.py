from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class RegisterUserForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'class':'form-control',
        'style': 'border: 4px solid #703C22; color:#1A120B;  padding: 5px; height: 50px; background: transparent; font-size: 16px; width: 100%;',}))
    first_name = forms.CharField(max_length=50,widget=forms.TextInput(attrs={
        'class':'form-control',
        'style': 'border: 4px solid #703C22; color:#1A120B;  padding: 5px; height: 50px; background: transparent; font-size: 16px; width: 100%;',}))
    last_name = forms.CharField(max_length=50,widget=forms.TextInput(attrs={'class':'form-control',
        'style': 'border: 4px solid #703C22; color:#1A120B;  padding: 5px; height: 50px; background: transparent; font-size: 16px; width: 100%;', }))
    address = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class':'form-control',
        'style': 'border: 4px solid #703C22; color:#1A120B;  padding: 5px; height: 50px; background: transparent; font-size: 16px; width: 100%;',}))
    contact = forms.CharField(max_length=50,widget=forms.TextInput(attrs={'class':'form-control',
        'style': 'border: 4px solid #703C22; color:#1A120B;  padding: 5px; height: 50px; background: transparent; font-size: 16px; width: 100%;',}))
    
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', 'address', 'contact')
        
    def __init__(self, *args, **kwargs):
        super(RegisterUserForm, self).__init__(*args, **kwargs)
        style = 'border: 4px solid #703C22; color: #1A120B; padding: 5px; height: 50px; background: transparent; font-size: 16px; width: 100%;'
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['style'] = style
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['style'] = style
        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['style'] = style