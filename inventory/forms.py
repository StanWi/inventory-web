from django import forms
from .models import Vendor, Country

class PostForm(forms.ModelForm):

    class Meta:
        model = Vendor
        fields = ('name', 'country',)

class SearchForm(forms.Form):
    country = forms.ModelChoiceField(
            queryset=Country.objects.values_list('name'),
            empty_label='Not Specified',
            widget=forms.Select(attrs={
                "onChange":'getCity()'})
            )
    
    city = forms.ModelChoiceField(
            queryset=Country.objects.values_list('capital'),
            empty_label='Not Specified'
            )

