from django.urls import path
from . import views


urlpatterns = [
    path('found/', views.item_list, {'post_type': 'found'}, name='found_list'),
    path('lost/', views.item_list, {'post_type': 'lost'}, name='lost_list'),

    path('found/create/', views.create_item, {'post_type': 'found'}, name='create_found'),
    path('lost/create/', views.create_item, {'post_type': 'lost'}, name='create_lost'),

    path('confirmations/', views.confirmations, name='confirmations'),
    path('<int:item_id>/resolve/', views.resolve_item, name='resolve_item'),
    path('<int:item_id>/claim/', views.claim_item, name='claim_item'),
]