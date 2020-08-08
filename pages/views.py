# pages/views.py
from django.http import HttpResponse
from django.views.generic import TemplateView

def homePageView(request):
	template_name = 'home.html'
