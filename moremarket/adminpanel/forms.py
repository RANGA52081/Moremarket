from django import forms
from products.models import Product, ProductImage
from customer.models import Banner
from utils.supabase_storage import upload_image_to_supabase


# ==========================
# PRODUCT FORM
# ==========================

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ["name", "description", "category", "is_featured", "is_active"]

        widgets = {
            "name": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Enter product name"
            }),
            "description": forms.Textarea(attrs={
                "class": "form-control",
                "rows": 4,
                "placeholder": "Enter product description"
            }),
            "category": forms.Select(attrs={
                "class": "form-select"
            }),
            "is_featured": forms.CheckboxInput(attrs={
                "class": "form-check-input"
            }),
            "is_active": forms.CheckboxInput(attrs={
                "class": "form-check-input"
            }),
        }


# ==========================
# BANNER FORM
# ==========================

class BannerForm(forms.ModelForm):
    class Meta:
        model = Banner
        fields = ["title", "subtitle", "image", "is_active"]
        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control"}),
            "subtitle": forms.TextInput(attrs={"class": "form-control"}),
            "image": forms.ClearableFileInput(attrs={"class": "form-control"}),
            "is_active": forms.CheckboxInput(attrs={"class": "form-check-input"}),
        }


# ==========================
# PRODUCT IMAGE FORM (SUPABASE)
# ==========================

class ProductImageForm(forms.ModelForm):
    image_file = forms.ImageField(required=False)

    class Meta:
        model = ProductImage
        fields = []

    def save(self, commit=True):
        instance = super().save(commit=False)
        image_file = self.cleaned_data.get("image_file")

        if image_file:
            image_url = upload_image_to_supabase(image_file)
            instance.image = image_url

        if commit:
            instance.save()

        return instance