from django.urls import path
from MapFunctionality import views

urlpatterns = [
    path('',views.index)
]