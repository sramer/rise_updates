from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('prakasam/<int:prakasam_id>', views.prakasam, name='prakasam'),
    path('gandhi/<int:gandhi_id>', views.gandhi, name='gandhi'),
    path('polytechnic/<int:polytechnic_id>', views.polytechnic, name='polytechnic')

]
