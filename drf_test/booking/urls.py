from django.urls import path, include

from .views import RoomView, BookingView, BookingOnRoomId


app_name = "booking"

urlpatterns = [
    path('rooms/', RoomView.as_view()),
    path('all_bookings/', BookingView.as_view()),
    path('id_bookings', BookingOnRoomId.as_view()),
    path('rest-auth/', include('rest_auth.urls')),
]