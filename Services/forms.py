from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(
        max_length=100,
        label='Nom',
        widget=forms.TextInput(attrs={'placeholder': 'Votre nom'})
    )

    email = forms.EmailField(
        label='Email',
        widget=forms.EmailInput(attrs={'placeholder': 'Votre email'})
    )

    subject = forms.CharField(
        max_length=200,
        label='Sujet',
        widget=forms.TextInput(attrs={'placeholder': 'Sujet de votre message'})
    )

    message = forms.CharField(
        label='Message',
        widget=forms.Textarea(attrs={'placeholder': 'Votre message', 'rows': 5})
    )





   