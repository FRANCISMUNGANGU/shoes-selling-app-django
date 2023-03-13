from django import forms
from shoes.models import Shoes
class ShoesForm(forms.ModelForm):
    class Meta:
        model = Shoes
        fields = '__all__'

# class PersonsForms(forms.ModelForm):
#     class Meta:
#         model = Persons
#         fields = '__all__'
