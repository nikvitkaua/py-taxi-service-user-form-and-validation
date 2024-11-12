from django import forms
from django.contrib.auth import get_user_model

from taxi.models import Driver, Car


class DriverLicenseUpdateForm(forms.ModelForm):
    class Meta:
        model = Driver
        fields = ("license_number",)


class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ("model", "manufacturer", "drivers",)

    drivers = forms.ModelMultipleChoiceField(
        queryset=get_user_model().objects.all(),
        required=False,
        widget=forms.CheckboxSelectMultiple()
    )
