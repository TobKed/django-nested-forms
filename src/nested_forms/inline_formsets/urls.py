from django.urls import path
from . import views


urlpatterns = [
    path('inline-formsets/', views.home,  name='inline-formsets'),
]
