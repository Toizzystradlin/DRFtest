from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Room, Booking
from .serializers import RoomSerializer, BookingSerializer

from django.db.models import Q

# Create your views here.

class RoomView(APIView):
    def get(self, request):
        rooms = Room.objects.all()
        serializer = RoomSerializer(rooms, many=True)
        return Response({'rooms': serializer.data})

    def post(self, request):
        room = request.data.get('room')
        serializer = RoomSerializer(data=room)
        if serializer.is_valid(raise_exception=True):
            room_saved = serializer.save()
        return Response({"success": "New room '{}' created".format(room_saved.name)})


class BookingView(APIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

    def get_queryset(self, datetime_from, datetime_to):
        return Booking.objects.exclude(Q(datetime1__range=(datetime_from, datetime_to)) | Q(datetime2__range=(datetime_from, datetime_to)) | Q(datetime1__lt=datetime_from, datetime2__gt=datetime_to))

    def get(self, request):
        try:
            datetime_from = request.GET['datetime_from']
            datetime_to = request.GET['datetime_to']
            bookings = self.get_queryset(datetime_from, datetime_to)
        except:
            bookings = Booking.objects.all()
        serializer = BookingSerializer(bookings, many=True)
        return Response({'bookings': serializer.data})

    def post(self, request):
        booking = request.data
        serializer = BookingSerializer(data=booking)
        if serializer.is_valid(raise_exception=True):
            booking_saved = serializer.save()
        return Response({"Success: New booking '{}' done!".format(booking_saved.room)})


class BookingOnRoomId(APIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    def get_queryset(self, room_id):
        return Booking.objects.filter(room_id=room_id)
    def get(self, request):
        try:
            room_id = request.GET['room_id']
            bookings = self.get_queryset(room_id)
        except:
            bookings = Booking.objects.all()
        serializer = BookingSerializer(bookings, many=True)
        return Response({'bookings': serializer.data})
