from django.urls import path
from accounts import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('register/', views.register_view, name = 'register'),
    path('login/', views.login, name = 'login'),
    path('logout/', LogoutView.as_view(), name = 'logout'),
]