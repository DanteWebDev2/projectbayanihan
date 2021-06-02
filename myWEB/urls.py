from django.urls import path
from . import views

urlpatterns = [
	path('', views.firstpage),
	path('success', views.sponsor, name="success"),
	#path('person', views.mydonors, name="person"),
	# path('success', views.Nextpage, name="success"),
	#path('success', views.option, name="success"),
]
