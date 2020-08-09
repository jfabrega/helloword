# pages/views.py
from django.shortcuts import render


def HomePageView(request):
	return render( request, 'home.html')

def AboutPageView(request):
	return render( request, 'about.html')
