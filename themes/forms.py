from django import forms
from themes.models import Theme

class ThemeModelForm(forms.ModelForm):
    
    class Meta:
        model = Theme
        exclude = ('id', 'user',)
