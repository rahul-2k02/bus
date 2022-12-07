from django.urls import path
from . import views
app_name = 'booking_app'
urlpatterns = [
    path('', views.index, name='index'),
    path('tickets/', views.ticketsView, name='tickets'),
    path('booking/', views.book,name='book'),
    path('add/',views.addTicketsView), 
    path('delete/<int:i>/', views.deleteTicketsView), 
]