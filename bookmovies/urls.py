"""bookmovies URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from shows import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name="indexpage"),
    path('users', views.UsersAPI.as_view(), name="usersapi"),
    path('shows', views.ShowsAPI.as_view(), name="showsapi"),
    path('bookings', views.BookingsAPI.as_view(), name='bookingsapi'),
    path('newscreen', views.NewScreenAPI.as_view(), name="newscreenapi"),
    path('newbooking', views.NewBooking.as_view(), name="newbookingapi"),
    path('bookingform', views.BookingForm.as_view(), name="bookingformapi"),
    path('sendemail', views.SendEmailAPI.as_view(), name="sendemail")
]
