from django.contrib import admin
from django.urls import path
from recommendation_ms.views.user_view import UserDetail
from recommendation_ms.views.user_view import UserList
from recommendation_ms.views.parking_lot_view import Parking_lotDetail
from recommendation_ms.views.parking_lot_view import Parking_lotList
from recommendation_ms.views.user_parking_lot_view import User_Parking_lotDetail
from recommendation_ms.views.user_parking_lot_view import User_Parking_lotList

urlpatterns = [
    path('users/', UserList.as_view()),
    path('users/<int:pk>', UserDetail.as_view()),
    path('parking_lots/', Parking_lotList.as_view()),
    path('parking_lots/<int:pk>', Parking_lotDetail.as_view()),
    path('near-parking-lots/', User_Parking_lotList.as_view()),
    path('near-parking-lots/<int:pk>', User_Parking_lotDetail.as_view()),

]
