from django import forms
from django.db.models import fields
from .models import *
from PIL import Image
from django.core.files import File
from django.core.validators import MinValueValidator
import re

class CategoriesForm(forms.ModelForm):
    # id = forms.IntegerField(widget=forms.NumberInput(
    #     attrs={'class': 'form-control mt-2 mb-2'}), label='category')

    class Meta:
        model = Category
        fields = ["category"]

    # def __init__(self, *args, **kwargs):
    #     super(CategoriesForm, self).__init__(*args, **kwargs)
    #     self.fields['id'].widget.attrs['readonly'] = True
    #     self.fields['id'].widget.attrs['hidden'] = True

class SubCategoriesForm(forms.ModelForm):
    id = forms.IntegerField(widget=forms.NumberInput(
        attrs={'class': 'form-control mt-2 mb-2'}), label='')

    class Meta:
        model = SubCategory
        fields = "__all__"

        # widgets = {
        #        'img1': 'class'
        #        'comment': form.Textarea(attrs={'cols': 100, 'rows': 40})
        # }

    def __init__(self, *args, **kwargs):
        super(SubCategoriesForm, self).__init__(*args, **kwargs)
        self.fields['id'].widget.attrs['readonly'] = True
        self.fields['id'].widget.attrs['hidden'] = True
        # self.fields['img1'].widget.attrs.update({'class': 'images'})


class ProductForm(forms.ModelForm):
    
    class Meta:
        model = products
        exclude = ('date', 'offer',)
    
    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)
        self.fields['img1'].widget.attrs['class'] = "image"
        self.fields['brand_id'].label = "brand name"


class VariantForm(forms.ModelForm):
    class Meta:
        model = VariantAndPrice
        exclude = ("product_id", 'final_price')
    def __init__(self, *args, **kwargs):
        super(VariantForm, self).__init__(*args, **kwargs)
        self.fields['variant'].label = "varaint 1(ram)"
        self.fields['price'].label = "varaint 1(price)"
        self.fields['quantity'].label = "varaint 1(quantity)"



        


class VariantForm2(forms.Form):
    nameOfVariant = forms.CharField(label='varaint 2(ram)')
    priceOfVariant = forms.IntegerField(label="varaint 2(price)")
    quantity_2 = forms.IntegerField(label="varaint 2(quantity)" )

    def clean(self):
        cleaned_data = super(VariantForm2, self).clean()
        nameOfVariant = cleaned_data.get("nameOfVariant")
        priceOfVariant = cleaned_data.get("priceOfVariant")
        quantity_2 = cleaned_data.get("quantity_2")

        if nameOfVariant != None and  int(nameOfVariant) < 1:
            self.add_error('nameOfVariant', "value must greater that 0") 
        elif str(nameOfVariant).isdigit() == False:
            self.add_error('nameOfVariant', "only numbers are allowded") 

        if priceOfVariant != None and  int(priceOfVariant) < 1:
            self.add_error('priceOfVariant', "value must greater that 0") 
        elif str(priceOfVariant).isdigit() == False:
            self.add_error('priceOfVariant', "only numbers are allowded") 

        if quantity_2 != None and  int(quantity_2) < 1:
            self.add_error('quantity_2', "value must greater that 0") 
        elif str(quantity_2).isdigit() == False:
            self.add_error('quantity_2', "only numbers are allowded") 

        return cleaned_data





class BannerForm(forms.ModelForm):
    class Meta:
        model = Banner
        fields = "__all__"

class CoupenForm(forms.ModelForm):
    class Meta:
        model = Coupen
        fields = "__all__"

    def clean(self):
        cleaned_data = super(CoupenForm, self).clean()
        coupen_offer = cleaned_data.get("coupen_offer")
        if coupen_offer != None and  coupen_offer < 1:
            self.add_error('coupen_offer', "coupen offer must greater that 0") 
        elif coupen_offer != None and coupen_offer > 99:
            self.add_error('coupen_offer', "coupen offer must less that 100") 
        return cleaned_data

