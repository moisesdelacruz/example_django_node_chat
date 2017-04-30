from django import forms
from publishings.models import Publishing

class PublishingModelForm(forms.ModelForm):

    class Meta:
        model = Publishing
        exclude = ('id', 'user',)
