from django.urls import path
from django.urls import include
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('brands/', include('Brands.urls')),
]