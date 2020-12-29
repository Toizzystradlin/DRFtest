from django_filters import rest_framework as filters
from .models import Booking

class BookingFilter(filters.FilterSet):
    datetime1date = filters.DateFromToRangeFilter()

    class Meta:
        model = Booking
        fields = ['room']