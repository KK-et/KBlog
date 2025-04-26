from django.urls import path
from . import views

 
urlpatterns=[
    path("", views.index, name='home'), #the name .. helps when using it in the base.html call for <a>
    path('det/<int:id>', views.details, name='det'),


]