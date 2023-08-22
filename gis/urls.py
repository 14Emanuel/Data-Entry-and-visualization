from django.urls import path
from . import views

app_name = 'gis'

urlpatterns = [
    path('', views.data_entry_view, name='data_entry'),
    path('data-entry/', views.data_entry_view, name='data_entry'),
    path('status_update/<str:unique_id>/', views.status_update_view, name='status_update'),
    #path('status_update/', views.status_update_view, name='status_update'),
    path('map/', views.map_view, name='map'),
]
