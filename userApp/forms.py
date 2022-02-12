from django.contrib.auth.forms import UserCreationForm
from django.db.models import fields 
from .models import CustomUser, address
from django import forms
import os
from twilio.rest import Client

class RegistrationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ("first_name", "last_name", "username",'email' , 'number')

    def clean(self):
        cleaned_data = super(RegistrationForm, self).clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")
        username = cleaned_data.get("username")
        email = cleaned_data.get("email")
        firstname = cleaned_data.get("first_name")
        lastname = cleaned_data.get("last_name")
        number = cleaned_data.get("number")


        if CustomUser.objects.filter(username=username).exists():
            a = CustomUser.objects.get(username=username)
            if a.is_active == 0:
                CustomUser.objects.get(username=username).delete()
            
        if number != None and len(number) < 10:
            self.add_error('number', "Minimum length is 10")
        elif  number != None and   len(number) > 10:
            self.add_error('number', "maximum length is 10")

        if password != confirm_password:
            self.add_error('confirm_password', "Password does not match")

        if firstname == "":
            self.add_error('first_name', "This field is required")
        
        if lastname == "":
            self.add_error('last_name', "This field is required")

        if CustomUser.objects.filter(username=username).exists():
            self.add_error('username', "username alredy exist")

        if CustomUser.objects.filter(email=email).exists():
            self.add_error('email', "email alredy exist")
    
        return cleaned_data

class logForm(forms.Form):
    username = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control mt-2 mb-2'}))
    password = forms.CharField(max_length=50, widget=forms.PasswordInput(attrs={'class': 'form-control mt-2 mb-2'}))


class NumberOnly(forms.Form):
    mobile_number = forms.CharField(max_length=50, widget=forms.NumberInput(attrs={'class': 'form-control mt-2 mb-2'}))

    def clean(self):
        cleaned_data = super(NumberOnly, self).clean()
        num = cleaned_data.get("mobile_number")
        print(num)

   
        if num and len(num) < 10:
            self.add_error('mobile_number', "minimum length is 10")
        elif num and len(num) > 10:
            self.add_error('mobile_number', "maximum legth is 10")
        elif num   and  CustomUser.objects.filter(number=num).exists() == False:
            self.add_error('mobile_number', "number not registered")



class OTPField(forms.Form):
    OTP = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control mt-2 mb-2  col-12' , 'id': 'otpField'}))

    def clean(self):
        cleaned_data = super(OTPField, self).clean()
        OTP = cleaned_data.get("OTP")

        # if not OTP.isdigit():
        #     self.add_error('OTP', "only contain number")
        if OTP and len(OTP) < 4:
            self.add_error('OTP', "minimum legth is 4")
        elif OTP and len(OTP) > 4:
            self.add_error('OTP', "maximum legth is 4")

        return cleaned_data


class add_address(forms.ModelForm):
    class Meta:
        model = address
        exclude = ('user_id',)

    def clean(self):
        cleaned_data = super(add_address, self).clean()
        full_name = cleaned_data.get("full_name")
        city = cleaned_data.get("city")
        mobile_number = cleaned_data.get("mobile_number")
        zipcode = cleaned_data.get("zipcode")
        address = cleaned_data.get("address")

        # if mobile_number !=None and mobile_number.isdecimal():
        #     self.add_error('mobile_number', "mobile number should only contain numbers")
        if mobile_number !=None and len(mobile_number) < 10:
            self.add_error('mobile_number', "minmum length is 10") 

        if zipcode !=None and len(zipcode) < 6:
            self.add_error('zipcode', "minmum length is 6") 

        return cleaned_data



        