# sendemail/forms.py
from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={"placeholder": "Your name"}))
    
    email = forms.EmailField(widget=forms.TextInput(attrs={"placeholder": "Your email"}))

    message = forms.CharField(
        widget=forms.Textarea(attrs={'name': "", 
        'id': '', 'cols': '30', 'rows': '10',
        "placeholder": "Your message"}))