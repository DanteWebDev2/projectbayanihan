from django.urls import path
from . import views

urlpatterns = [
	path('', views.Mainpage,),
	path('donation', views.Page, name="donation"),
	]