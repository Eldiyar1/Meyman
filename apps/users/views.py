from rest_framework import mixins, viewsets

from .models import Profile, CarReservation, AccommodationReservation
from .serializers import ProfileSerializer, CarReservationSerializer, AccommodationReservationSerializer
from rest_framework.permissions import IsAuthenticated


class ProfileViewSet(mixins.ListModelMixin,
                     mixins.CreateModelMixin,
                     mixins.RetrieveModelMixin,
                     mixins.UpdateModelMixin,
                     mixins.DestroyModelMixin,
                     viewsets.GenericViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'user__username'


class CarReservationViewSet(mixins.UpdateModelMixin,
                            mixins.CreateModelMixin,
                            viewsets.GenericViewSet):
    queryset = CarReservation.objects.all()
    serializer_class = CarReservationSerializer
    permission_classes = [IsAuthenticated]


class AccommodationReservationViewSet(mixins.UpdateModelMixin,
                                      mixins.CreateModelMixin,
                                      viewsets.GenericViewSet):
    queryset = AccommodationReservation.objects.all()
    serializer_class = AccommodationReservationSerializer
    permission_classes = [IsAuthenticated]

