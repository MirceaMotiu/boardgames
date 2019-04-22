from django import forms

class PersonForm(forms.Form):
    nume = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    phonenumber = forms.IntegerField(required=True)
    quantity = forms.DecimalField(required=True)