from django.urls import path
from . import views

urlpatterns = [
    path('user/', views.user, name='user'),
    path('usersignup/', views.user_signup, name='usersignup'),
    path('userlogin/', views.user_login, name='userlogin'),
    path('userdashboard/', views.user_dashboard, name='userdashboard'),
    
    path('userenquiry/', views.user_enquiry, name='userenquiry'),
    path('querysubmit/', views.query_submit, name='querysubmit'),
]
