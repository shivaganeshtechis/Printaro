from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.ProductAdd.as_view(), name='add-product'),
    path('update/<int:id>/', views.ProductUpdate.as_view(), name='update-product'),
    path('delete/<int:id>/', views.ProductDelete.as_view(), name='delete-product'),
    path('', views.Productist.as_view(), name='list-product'),
]
