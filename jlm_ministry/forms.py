from django import forms

class ContactForm(forms.Form):
    email = forms.EmailField(required=True,widget=forms.TextInput(attrs={'placeholder': 'Email'}))
    subject = forms.CharField(required=True,widget=forms.TextInput(attrs={'placeholder': 'Subject'}))
    message = forms.CharField(widget=forms.Textarea, required=True)
