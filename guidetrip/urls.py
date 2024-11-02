from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_trips, name='alltrips'),
    path('<int:trips_id>/', views.det_trips_view, name='det_trips_view' ),
    path('add/', views.add_product, name='add_product'),
]