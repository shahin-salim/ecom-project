from .import views
from django.urls import path

urlpatterns = [
    path('admin_login/', views.AdminLogin, name='AdminLogin'),
    path('admin_logout/', views.AdminLogout, name='AdminLogout'),

    path('', views.Dashboard, name='Dashboard'),
    path('user', views.UserManagement, name='UserManagement'),
    path('block/', views.BlockAndUnblock, name='blockandunbock'),

    path('category/', views.CategoryAndSubCategory, name='CategoryAndSubCategory'),
    path('addcategory/', views.AddCategory, name='AddCategory'),
    path('updatecategory/', views.UpdateCategory, name='updatecategory'),
    path('deletecategory/', views.DeleteCategory, name='deletecategory'),

    path('addsubcategory/', views.AddSubCategory, name='AddCategory'),
    path('updatesubcategory/', views.UpdateSubCategory, name='updatecategory'),
    path('deletesubcategory/', views.DeleteSubCategory, name='deletecategory'),

    path('allproducts/', views.AllProducts, name='allproducts'),
    path('addproducts/', views.AddProducts, name='AddProducts'),
    path('delproduct/', views.DelProduct, name='DelProduct'),
    path('updateproduct/', views.UpdateProduct, name='DelProduct'),

    path('order/', views.ViewOrder, name='order'),
    path('changeorderstatus/', views.OrderStatus, name='OrderStatus'),

    path('setbanner/', views.Setbanner, name='setbanner'),
    path('bannertable/', views.BannerTable, name='bannerTable'),
    path('delbanner/', views.DelBanner, name='DelBanner'),

    path('productoffer/', views.ProductOffer, name='productoffer'),
    path('categoryoffer/', views.CategoryOffer , name='categoryoffer'),

    path('addproductoffer/', views.AddProductOffer, name='addproductoffer'),
    path('addcategoryoffer/', views.AddCategoryOffer, name='addcategoryoffer'),

    path('coupenmanagement/', views.CoupenManagement, name='coupenmanagement'),
    path('addcoupen/', views.AddCoupen, name='addcoupen'),

    path('salesreport/', views.SalesReport, name='salesreport'),

    path('excel/', views.Excel, name='excel'),   

]
