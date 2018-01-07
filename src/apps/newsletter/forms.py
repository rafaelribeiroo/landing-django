from django import forms
from .models import Unir


class UnirForm(forms.ModelForm):
    name = forms.CharField(label='Nome', max_length=20)
    email = forms.EmailField(label='E-mail')

    class Meta:
        model = Unir
        fields = ['name', 'email']

    def clean_email(self, *args, **kwargs):
        name = self.cleaned_data.get('name')
        email = self.cleaned_data.get('email')
        us = Unir.objects.filter(email__iexact=email)
        if us.exists():
            print('Existente')
            raise forms.ValidationError('Esse e-mail já existe')
        return email
