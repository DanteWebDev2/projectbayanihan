from django import forms  
from .models import Sponsor 
    
class Donates(forms.ModelForm):  
    class Meta:  
        model = Sponsor  
        fields = "__all__"  