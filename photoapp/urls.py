from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('profile/', views.profile, name='profile'),
    path('profile/edit/', views.edit_profile, name='edit_profile'),
    path('photo/<int:id>/', views.photo_detail, name='photo_detail'),
    path('photo/<int:id>/react/', views.react_to_photo, name='react_to_photo'
    ),
]