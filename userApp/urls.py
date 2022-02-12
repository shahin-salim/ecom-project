
from django.urls import path

from userApp.forms import add_address
from .import views
from django.conf.urls import url


urlpatterns = [
    path('register', views.register, name='register'),
    path('', views.home, name='home'),
    path('number_field', views.NumberField, name='NumberField'),
    path('enter_otp', views.EnterOtp, name='enter_otp'),
    path('OTP_register', views.OTPRegister, name='OTP_register'),
    path('login', views.login, name='login'),
    path('eachproduct', views.eachproduct, name='eachproduct'),
    path('userlogout', views.UserLogout, name='UserLogout'),
    path('productlist', views.ProductList, name='ProductList'),
    path('addtocart', views.AddToCart, name='Cart'),
    path('mycart', views.myCart, name='myCart'),
    path('changequantity', views.ChangeQuantity, name='changequantity'),
    path('remove_irem_cart', views.removeIremFromCart, name='removeIremFromCart'),
    path('checkout/<id>/', views.Checkout, name='checkout'),
    path('addressForm', views.addressForm, name='addressForm'),
    path('makepayment', views.MakePayment, name='makepayment'),
    path('buynow', views.BuyNow, name='buynow'),  
    path('cancell_order', views.CancellOreturn, name='cancell_order'),   
    path('editprofile', views.EditProfile, name='editprofile'),   
    path('profile', views.Profile, name='profile'),   
    path('changepassword', views.ChangePassword, name='changepassword'), 
    path('editaddress', views.EditAddress, name='editaddress'), 
    path('invoice/<limit>/', views.Invoice, name='invoice'), 
    path('DelAddressFromCheckout/', views.DelAddressFromCheckout, name='DelAddressFromCheckout'), 

    # all  url related to sorting
    path('sortby/', views.SortBy, name='sortby'), 
    path('search', views.Search, name='search'),   

    path('addcoupen', views.AddCoupen, name='AddCoupen'),   

    path('changevariant', views.ChangeVariant, name='changevariant'),   
    path('orderdetails', views.Ordersdetials, name='orderdetails'),

    path('razorpaysetamt', views.RazorpaySetAmt, name='razorpaysetamt'),   


]