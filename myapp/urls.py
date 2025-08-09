
from django.urls import path
from .import views
urlpatterns = [
 path('',views.home,name='home'),
path('about/',views.about,name='about'),
path('add/', views.add_blog, name='add_blog'),
path('dashboard/',views.dashboard,name='dashboard'),
path('contact/',views.contact,name='contact'),
path('signuppage/',views.signuppage,name='signuppage'),
path('loginpage/',views.loginpage,name='loginpage'),
path('thank/',views.thank, name='thank'),
path('logoutpage/',views.logoutpage, name='logoutpage'),
path('readmore/<int:blog_id>',views.readmore,name='readmore'),
]
