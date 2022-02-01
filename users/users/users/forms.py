from django import forms



class SendEmailFrom(forms.Form):
    subject = forms.CharField(max_length=30)
    message = forms.CharField(max_length=1000, widget=forms.TextInput(attrs={"class":"message"}))
    