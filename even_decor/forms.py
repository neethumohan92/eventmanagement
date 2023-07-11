from . models import *
from django import forms

class Pforms(forms.ModelForm):
    class Meta:
        model = Product
        fields =  ['Name','Desc','Price','Image','Category']

class Bforms(forms.ModelForm):
    class Meta:
        model = Decor_DB
        fields =  ['Username','Businessname','Number','Email','Place','Password','Experience']