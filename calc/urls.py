from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
	path('<str:operation>/<int:op1>/<int:op2>', views.calcular),
    ]
