from django.urls import path

from tree.views import RestaurantView

urlpatterns = [
    path('restaurants/', RestaurantView.as_view(), name='restaurants'),
    path('restaurant/<str:slug>/', RestaurantView.as_view(), name='restaurant-detail')
]