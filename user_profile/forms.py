from django import forms
from .models import User


class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email', 'name', 'surname', 'birthday', 'avatar']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exclude(pk=self.instance.pk).exists():
            raise forms.ValidationError('Этот адрес электронной почты уже используется.')
        return email
