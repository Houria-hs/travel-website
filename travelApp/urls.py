from django.urls import path
from . import views

urlpatterns = [
    path('', views.home , name='home'),
    path('Register/', views.Register , name='Register' ),
    path('Login/', views.login_view , name='login' ),
    path('Logout/', views.logout_view , name='logout' ),
    path('trip/<int:pk>', views.trip , name='trip' ),
    path('Newsletter/', views.Newsletter_view , name='Newsletter_view' ),
    path('ThankYou/', views.ThankYou , name='ThankYou' ),
    path('bookingSummary/<int:trip_id>/', views.bookingSummary , name='bookingSummary' ),
]