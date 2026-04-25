from django.urls import path
from . import views


urlpatterns = [
    path('found/', views.found_items_list, name='found_list'),
    path('found/new/', views.create_found_item, name='create_found'),
]