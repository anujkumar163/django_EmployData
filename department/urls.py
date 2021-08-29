from django.urls import path
from . import views

urlpatterns = [
	path('add_dept/', views.add_dept)
]