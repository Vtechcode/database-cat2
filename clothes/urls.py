from django.urls import path
from . import views
from .views import ClothesList, ClothesDetails, ClothesCreate, ClothesUpdate, ClothesDelete

urlpatterns = [
    path('', ClothesList.as_view(), name='clad'),
    path('<int:pk>/clothes_detail', ClothesDetails.as_view(), name='clad_detail'),
    path('create-clothes', ClothesCreate.as_view(), name='create'),
    path('<int:pk>/update-clothes', ClothesUpdate.as_view(), name='update'),
    path('<int:pk>/delete-clothes', ClothesDelete.as_view(), name='delete'),
]