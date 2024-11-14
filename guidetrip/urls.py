from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_trips, name='alltrips'),
    path('<int:trips_id>/', views.det_trips_view, name='det_trips_view'),
    path('add/', views.add_product, name='add_product'),
    path('edit/<int:product_id>/', views.edit_product, name='edit_product'),
    path('delete/<int:product_id>/', views.delete_product,
         name='delete_product'),
]
