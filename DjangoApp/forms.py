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
        label="Username",
        strip=False
    )

    password1 = forms.CharField(
        label="Password",
        strip=False,
        widget=forms.PasswordInput,
    )
    password2 = forms.CharField(
        label="Confirm Password",
        widget=forms.PasswordInput,
        strip=False,
    )
    # class Meta(UserCreationForm.Meta):
    #     fields = ("username", "email")
