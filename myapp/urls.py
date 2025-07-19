from django.urls import path
from .import views
urlpatterns = [
path('',views.home,name='home'),
path('about/',views.about,name='about'),
path('services/',views.services,name='services'),
path('languages/',views.languages,name='languages'),
path('contact/',views.contact,name='contact'),
path('signuppage/',views.signuppage,name='signuppage'),
path('loginpage/',views.loginpage,name='loginpage'),
path('readmore/<int:blog_id>',views.readmore,name='readmore'),
]
