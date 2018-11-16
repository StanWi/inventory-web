from django import forms
from .models import Vendor

class PostForm(forms.ModelForm):

    class Meta:
        model = Vendor
        fields = ('name', 'country',)
