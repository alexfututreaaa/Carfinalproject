from django.urls import path, include
from rest_framework.routers import DefaultRouter
from cars import views
from cars.views import CarViewSet

router = DefaultRouter()
router.register(r'cars', views.CarViewSet)
urlpatterns = [
      path('', views.home, name='car-home'),
      path('my_about/', views.about, name='about'),
      path('api/', include(router.urls)),
    path('car/<int:car_id>/edit/', views.edit_car, name='edit-car'),
    path ('cars/', views.cars_view, name ='cars'),
path('cars/', views.car_view_simple, name='car_view_simple'),
    path('user/<int:user_id>/cars', views.cars_by_type, name="cars_by_tipe"),
    path('car/<int:car_id>/edit/', views.cars_delete, name='car_delete')

  ]