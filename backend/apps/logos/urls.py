from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.LogoAdd.as_view(), name='add-logo'),
    path('update/<int:id>/', views.LogoUpdate.as_view(), name='update-logo'),
    path('delete/<int:id>/', views.LogoDelete.as_view(), name='delete-logo'),
    path('', views.LogoList.as_view(), name='list-logo'),
]
