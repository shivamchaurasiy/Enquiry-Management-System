from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('adminuser/', views.admin_user, name='adminuser'),
    path('adminsignup/', views.admin_signup, name='adminsignup'),
    path('adminsignusubmit/', views.adminsignup_submit, name='adminsignusubmit'),
    path('adminlogin/', views.admin_login, name='adminlogin'),
    
    path('admindashboard/', views.admin_dashboard, name='admindashboard'),
    path('showenquiry/', views.show_enquiry, name='showenquiry'),
    path('delete/<int:id>/', views.delete, name='delete'),
    # path('update/<int:id>/', views.update, name='update'),
    
]
