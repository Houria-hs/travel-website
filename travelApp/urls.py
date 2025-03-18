from django.urls import path
from . import views

urlpatterns = [
    path('', views.home , name='home'),
    path('Register/', views.Register , name='Register' ),
    path('Login/', views.login_view , name='login' ),
    path('Logout/', views.logout_view , name='logout' ),
    path('trip/<int:pk>', views.trip , name='trip' ),
]