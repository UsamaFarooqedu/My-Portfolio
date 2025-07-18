from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('projects/', views.projects, name='projects'),
    path('contact/', views.contact, name='contact'),
    path('add-client/', views.add_client, name='add_client'),
    path('submit-contact/', views.submit_contact, name='submit_contact'),

]