from django.conf import urls
from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from medical import views
urlpatterns = [
   path("", views.index, name='index'),
   path("signup/", views.signup, name='signup'),
   path("login/", views.login, name='login'),
   path("dashboard/", views.dashboard, name='dashboard'),
   path("upload-prescription/", views.uploadprescription, name='uploadprescription'),
   path("map/", views.map, name='map'),
   path("maps/", views.maps, name='maps'),
   path("lab-test/", views.labtest, name='labtest'),
   path("rtl/", views.rtl, name='rtl'),
   path("tables/", views.tables, name='tables'),
   path("appointment/", views.appointment, name='appointment'),
   path("upgrade/", views.upgrade, name='upgrade'),
   path("user/", views.user, name='user'),

]
