from rest_framework import serializers

from .models import Room, Booking

class RoomSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=40)
    id = serializers.IntegerField()

    def create(self, validated_data):
        return Room.objects.create(**validated_data)


class BookingSerializer(serializers.Serializer):
    room = serializers.SlugRelatedField(slug_field="id", queryset=Room.objects.all())
    datetime1 = serializers.DateTimeField()
    datetime2 = serializers.DateTimeField()

    def create(self, validated_data):
        return Booking.objects.create(**validated_data)

