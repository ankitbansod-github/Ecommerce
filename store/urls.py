from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', views.store, name='store'),
    path('<int:product_id>/',views.product_detail,name='product_detail'),
    path('cart/', views.cart, name='cart'),

    path('register/', views.registerPage, name='register'),
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name='logout'),

    path('checkout/', views.checkout, name='checkout'),
    path('update_item/', views.updateItem, name='update_item'),
    path('process_order/', views.processOrder, name='process_order'),

    path('password_reset/',
         auth_views.PasswordResetView.as_view(template_name='store/password_reset.html'),
         name='password_reset'),
    path('reset_password_sent/',
         auth_views.PasswordResetDoneView.as_view(template_name='store/reset_password_sent.html'),
         name='password_reset_done'),
    path('reset/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name='store/password_reset_form.html'),
         name='password_reset_confirm'),
    path('reset_password_complete/',
         auth_views.PasswordResetCompleteView.as_view(template_name='store/reset_password_complete.html'),
         name='password_reset_complete'),

]