from django.urls import path 
from .import views 

urlpatterns = [
    path('', views.home, name="home"),
    path('about/', views.about, name="about"),
    path('menu/', views.menu, name="menu"),
    path('book/', views.book, name="book"),
    path('menu/<int:pk>', views.menu, name="menu"),
    path('bookings/', views.bookings, name="bookings"),
]