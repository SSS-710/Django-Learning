from django import forms
from .models import ChaiVarity

class ChaiVarityForn(forms.Form):
    Chai_Varity = forms.ModelChoiceField
    (queryset=ChaiVarity.objects.all(), label="Select chai varity")