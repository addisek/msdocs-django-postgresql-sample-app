from django.db.models import Avg, Count
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt

from restaurant_review.models import Restaurant, Review

# Create your views here.

# w pliku views.py
from django.shortcuts import render, redirect

def index(request):
    return render(request, 'index.html')

def login_view(request):
    # Tutaj logika logowania
    return render(request, 'login.html')

def contact_view(request):
    # Tutaj logika kontaktu
    return render(request, 'contact.html')
