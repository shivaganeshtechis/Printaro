from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.TshirtAdd.as_view(), name='add-tshirt'),
    path('update/<int:id>/', views.TshirtUpdate.as_view(), name='update-tshirt'),
    path('delete/<int:id>/', views.TshirtDelete.as_view(), name='delete-tshirt'),
    path('', views.Tshirtist.as_view(), name='list-tshirt'),
]
