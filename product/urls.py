from django.urls import path
from . import views

urlpatterns = [
    path('showproduct/',views.showProduct,name = 'showproduct'),
    path('addproduct/',views.addProduct,name = 'addproduct'),

]