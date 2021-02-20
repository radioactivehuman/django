from django.contrib import admin
from django.urls import path,include
from home import views

urlpatterns = [
    path('',views.home,name="home"),
    path('home',views.home,name="home"),
    path('about',views.about,name="about"),
    path('contact',views.contact,name="contact"),
    path('disclamer',views.disclamer,name="disclamer"),
    path('privicy',views.privicy,name="privicy"),
    path('search', views.search, name="search"),
    path('tech', views.tech, name="tech"),
    path('myst', views.myst, name="myst"),
    path('hacking', views.hacking, name="hacking"),
    path('business', views.business, name="business"),
    path('other', views.other, name="other"),
]