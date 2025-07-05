from django import forms
from . models import Item, Category, Order, OrderItem

class ProductForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['name', 'description', 'price', 'image', 'category']

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['address']
        widgets = {
            'address': forms.TextInput(attrs={'class': 'form-control'}),
        }

class OrderStateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['state']

class ReviewForm(forms.ModelForm):
    class Meta:
        model = OrderItem
        fields = ['review_star', 'review_text']
        widgets = {
            'review_star': forms.NumberInput(attrs={'min': 1, 'max': 5, 'class': 'form-control'}),
            'review_text': forms.Textarea(attrs={'rows': 3, 'class': 'form-control'}),
        }