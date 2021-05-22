
from django import forms


# forms


class mail_form(forms.Form):
    name = forms.CharField(widget=forms.CharField(
        attrs={'class': 'name in-box-input row1','placeholder': 'Name'}), label='')
    email = forms.CharField(widget=forms.EmailInput(
        attrs={'class': 'email-field in-box-input row1','placeholder': 'Email'}), label='')
    number = forms.IntegerField(widget=forms.IntegerField(
        attrs={'class': 'number-field in-box-input row1','placeholder': 'number'}), label='')
    subject = forms.CharField(widget=forms.CharField(
        attrs={'class': 'subject-field in-box-input row1','placeholder': 'Subject'}), label='')
    message = forms.Textarea(widget=forms.Textarea(
        attrs={'class': 'message-field in-box-input row2','placeholder': 'message'}), label='')