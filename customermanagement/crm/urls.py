from django.urls import path
from django.contrib.auth import views as auth_views
from .import views


urlpatterns = [
    
    path('registerPage/', views.registerPage, name='registerPage'),
    path('loginPage/', views.loginPage, name='loginPage'),
    path('logoutUser/', views.logoutUser, name='logoutUser'),
    
    path('', views.home, name='home'),
    path('userPage/', views.userPage, name='userPage'),
    path('accountSettings/', views.accountSettings, name='accountSettings'),


    path('products/', views.products, name='products'),
    path('customers/<str:pk>', views.customers, name='customers'),
    
    path('createOrder/<str:pk>', views.createOrder, name='createOrder'),
    path('updateOrder/<str:pk>', views.updateOrder, name='updateOrder'),
    path('deleteOrder/<str:pk>', views.deleteOrder, name='deleteOrder'),
    path('deletecustomer/<str:pk>', views.deletecustomer, name='deletecustomer'),


    path('reset_password/',auth_views.PasswordResetView.as_view(template_name='accounts/password_reset.html'), name='reset_password'),
    path('reset_password_sent/',auth_views.PasswordResetDoneView.as_view(template_name='accounts/password_reset_sent.html') ,name='password_reset_done'),
    #path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name='accounts/password_reset_form.html'), name ='password_reset_confirm'),
    path('reset/<uidb64>/<token>/',
     auth_views.PasswordResetConfirmView.as_view(template_name="accounts/password_reset_form.html"), 
     name="password_reset_confirm"),
    path('reset_password_complete/',auth_views.PasswordResetCompleteView.as_view(template_name='accounts/password_reset_done.html'), name = 'password_reset_complete'),
]