from django import forms
from shoes.models import Shoes
class ShoesForm(forms.ModelForm):
    class Meta:
        model = Shoes
        fields = '__all__'
