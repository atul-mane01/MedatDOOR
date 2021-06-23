from django.urls import path
from . import views

urlpatterns = [
    path('showcategory/',views.showCategory,name = 'showcategory'),
    path('addcategory/',views.addCategory,name = 'addcategory'),
 ]