from django import forms
from.models import ReviewRating, Product
from category.models import Category

class ReviewForm(forms.ModelForm):
    class Meta:
        model = ReviewRating
        fields = ['subject', 'review','rating']
        
        
        
class ProductForm(forms.ModelForm):
    images = forms.ImageField(required=False, error_messages= {"invalid": ("Image files only")}, widget=forms.FileInput)
    category = forms.ModelChoiceField(queryset=Category.objects.all(), required=True, widget=forms.Select(attrs={"class": "form-control"}))
    is_available = forms.BooleanField(required=False, initial=True, widget=forms.CheckboxInput())
    stock = forms.IntegerField(widget=forms.NumberInput(attrs={"class": "form-control"}))
    class Meta:
        model = Product
        fields = ["product_name", "slug", "description", "price","images", "stock", "is_available","category"]
        
    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] ="form-control" 


