from django import forms
from .models import Hotel


class HotelForm(forms.ModelForm):
    class Meta:
        model = Hotel
        fields = "__all__"

        widgets = {
            "hotel_name": forms.TextInput(attrs={'class': 'form-control'}),
            "hotel_address": forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            "table_no": forms.NumberInput(attrs={'class': 'form-control'}),
            "no_of_persons": forms.NumberInput(attrs={'class': 'form-control'}),
            "menu_list": forms.TextInput(attrs={'class': 'form-control'}),
            "total_bill": forms.NumberInput(attrs={'class': 'form-control'}),
            "payment_mode": forms.Select(attrs={'class': 'form-control'}),
        }
