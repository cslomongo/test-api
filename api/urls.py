from django.urls import path

from . import views

urlpatterns = [
    path('item/',views.ItemList.as_view()),
    path('item/<int:pk>',views.ItemDetails.as_view()),
    path('location/',views.LocationList.as_view()),
    path('location/<int:pk>',views.LocationDetails.as_view()),

]