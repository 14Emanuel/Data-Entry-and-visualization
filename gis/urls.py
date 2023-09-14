from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = 'gis'

urlpatterns = [
    path('', views.data_entry_view, name='data_entry'),
    path('data-entry/', views.data_entry_view, name='data_entry'),
    path('status_update/<str:unique_id>/', views.status_update_view, name='status_update'),
    path('map/', views.map_view, name='map'),
    path('popup/<str:unique_id>/', views.popup_view, name='popup'),
    path('navigation-pane/<str:unique_id>/', views.navigation_pane_view, name='navigation_pane'),  # Add this line
    path('update-navigation-entry/<int:navigation_entry_id>/', views.update_navigation_entry, name='update_navigation_entry'),
]

# Serve media files during development
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
