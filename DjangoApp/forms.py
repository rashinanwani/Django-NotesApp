from django import forms
from django.forms.widgets import TextInput
from DjangoApp.models import viewnotes
from django.contrib.auth.forms import UserCreationForm

class NotesForm(forms.ModelForm):
    notes = forms.CharField(widget=forms.Textarea(attrs={'cols': 25, 'rows': 8}))
    class Meta:
        model = viewnotes
        fields = ['notes']
        # widgets = {
        #            'color': TextInput(attrs={'type': 'notes'}),
        # }

class SignUpForm(UserCreationForm):
    username = forms.CharField(
        label='',
        widget=forms.TextInput(attrs={'placeholder': 'Enter UserName'}),
        strip=False
    )

    password1 = forms.CharField(
        label='',
        strip=False,
        widget=forms.PasswordInput(attrs={'placeholder': 'Enter Password'}),
    )
    password2 = forms.CharField(
        label='',
        widget=forms.PasswordInput(attrs={'placeholder': 'Enter Confirm Password'}),
        strip=False,
    )

    # email = forms.CharField(
    #     label='',
    #     widget=forms.TextInput(attrs={'placeholder': 'Enter Email'}),
    #     strip=False,
    # )
    # class Meta(UserCreationForm.Meta):
    #     fields = ("username", "email")
