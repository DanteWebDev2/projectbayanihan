from django.urls import path
from . import views

urlpatterns = [
	path('', views.main),
	path('hehe', views.firstpage, name="hehe"), 
	path('success', views.sponsor, name="success"), 
	path('done', views.secondpage, name="done"),
	path('summary', views.donation, name="summary"),
	path('good', views.paper, name="good"),
	path('edit/<int:id>', views.edit),
	path('update/<int:id>', views.update),
	path('delete/<int:id>', views.destroy),
	
	
	
	
]
