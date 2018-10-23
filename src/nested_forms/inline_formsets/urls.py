from django.urls import path
from . import views


urlpatterns = [
    path('inline-formsets/', views.home,  name='inline-formsets'),
    path('manage_children/<int:parent_id>/', views.manage_children,  name='manage_children'),
]
