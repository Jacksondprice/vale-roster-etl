from rest_framework import viewsets

from .models import Booking
from .serializers import BookingSerializer


class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.order_by("id")
    serializer_class = BookingSerializer
