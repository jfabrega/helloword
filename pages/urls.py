# pages/urls.py
from django.urls import path
from pages.views import HomePageView,AboutPageView

urlpatterns = [
	path('', HomePageView, name='home'),
	path('about/', AboutPageView, name='about'),
]
