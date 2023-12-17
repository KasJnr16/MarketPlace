from django import forms
from .models import Address


INPUT_CLASSES = "w-full py-4 px-6 rounded-xl border"

class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = ("street", "city", "region", "zip_code")

        widgets = {
            "street": forms.TextInput(attrs={"class": INPUT_CLASSES}),
            "city": forms.TextInput(attrs={"class": INPUT_CLASSES}),
            "region": forms.TextInput(attrs={"class": INPUT_CLASSES}),
            "zip_code": forms.TextInput(attrs={"class": INPUT_CLASSES}),
        }
