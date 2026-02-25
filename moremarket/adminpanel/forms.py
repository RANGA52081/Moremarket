from django import forms
from customer.models import Banner

class BannerForm(forms.ModelForm):
    class Meta:
        model = Banner
        fields = ["title", "subtitle", "image", "is_active"]