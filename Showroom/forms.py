from django import forms
from .models import *
from django.core.validators import EmailValidator
from django.core.exceptions import ValidationError

def emailx(email):
    if email.split('@')[1].split('.')[0].lower()=='hotmail':
        raise ValidationError("Email not acceptible")
    

class contactform(forms.Form):
    name= forms.CharField(max_length=123)
    email =forms.CharField(validators=[EmailValidator(),emailx])
    verify = forms.CharField(label='Verify Email')
    text= forms.CharField(widget=forms.Textarea)

    def clean(self):
        cleaned_data = super().clean() 
        
        cleaned_data['email'] = cleaned_data.get('email')
        cleaned_data['verify'] = cleaned_data.get('verify')
        
        
        if cleaned_data.get('email') != cleaned_data.get('verify'):
            raise forms.ValidationError("email mismatch")
        return cleaned_data
    
class AddNewProfile(forms.ModelForm):
    class Meta:
        model = brand
        fields = '__all__'

            
class AddNewBrand(forms.ModelForm):
    class Meta:
        model = model
        fields = '__all__'

class filters_models(forms.Form):
    brand = forms.ModelChoiceField(queryset=brand.objects.all(), required=False)
    min_price = forms.DecimalField(min_value=0, required=False)
    max_price = forms.DecimalField(min_value=0, required=False)
    year = forms.IntegerField(min_value=1900, max_value=9999, required=False)