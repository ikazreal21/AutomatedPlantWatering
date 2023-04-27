from django.urls import path
from . import views

urlpatterns = [
    # User
    path('register/', views.registerPage, name='register'),
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutPage, name='logout'),

    # Admin
    path('', views.Index, name='dashboard'),
]