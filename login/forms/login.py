from django import forms

class LoginForm(forms.ModelForm):
    username = forms.CharField(label='Gebruikersnaam', max_length=100)
    password = forms.CharField(label='Wachtwoord', max_length=100, widget=forms.PasswordInput)