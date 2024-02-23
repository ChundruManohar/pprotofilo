from . import views
from django.urls import path

urlpatterns = [
    path('',views.home,name='home'),
    path('about/',views.about,name='about'),
    path('skill/',views.skill,name='skill'),
    path('work/',views.work,name='work'),
    path('contact/',views.contact,name='contact'),
]