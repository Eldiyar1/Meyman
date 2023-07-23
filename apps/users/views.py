from rest_framework import mixins, viewsets
from django_filters.rest_framework import DjangoFilterBackend
from .models import Profile, CarReservation, AccommodationReservation
from .serializers import ProfileSerializer, CarReservationSerializer, AccommodationReservationSerializer
from rest_framework.permissions import IsAuthenticated
from .filters import AccommodationReservationFilter


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


class AccommodationReservationViewSet(mixins.ListModelMixin,
                     mixins.CreateModelMixin,
                     mixins.RetrieveModelMixin,
                     mixins.UpdateModelMixin,
                     mixins.DestroyModelMixin,
                                      viewsets.GenericViewSet):
    queryset = AccommodationReservation.objects.all()
    serializer_class = AccommodationReservationSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_class = AccommodationReservationFilter
