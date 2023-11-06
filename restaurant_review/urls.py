# w pliku urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login_view, name='login'),
    path('contact/', views.contact_view, name='contact'),
    # inne ścieżki
]
