from django.urls import path
from . import views

urlpatterns = [
	path('', views.main),
	path('hehe', views.firstpage, name="hehe"), 
	path('success', views.sponsor, name="success"), 
	path('done', views.secondpage, name="done"),
	path('nice', views.donation, name="nice"),
	#path('person', views.mydonors, name="person"),
	# path('success', views.Nextpage, name="success"),
	#path('success', views.option, name="success"),
]
