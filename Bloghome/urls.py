from django.urls import path
from .import views
urlpatterns = [
    path('', views.home, name='home'),
    path('contact', views.contact, name='contact'),
    path('about', views.about, name='about'),
    path('login', views.handle_login, name='handle_login'),
    path('logout', views.handle_logout, name='handle_logout')
]
