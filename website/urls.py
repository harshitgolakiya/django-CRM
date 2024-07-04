
from django.urls import path
from . import views

urlpatterns = [
    path('',views.homeview,name='home'),
    path('logout/',views.logoutview ,name='logout'),
    path('register/',views.registerview ,name='register'),
    path('recordview/<int:pk>/',views.recordview ,name='recordview'),
    path('deleterecord/<int:pk>/',views.deleterecord ,name='deleterecord'),
    path('updaterecord/<int:pk>/',views.updaterecord ,name='updaterecord'),
    path('addrecord/',views.addrecord ,name='addrecord'),
]
