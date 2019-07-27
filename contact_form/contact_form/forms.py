from django import forms

class FormContact(forms.Form):
    name = forms.CharField(label='Your name', max_length=100)
    message = forms.CharField(widget=forms.Textarea)
    sender = forms.EmailField()
    cc_myself = forms.BooleanField(required=False)
    subject = forms.CharField(widget=forms.Textarea)