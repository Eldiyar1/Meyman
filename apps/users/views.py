from rest_framework import mixins, viewsets
from django_filters.rest_framework import DjangoFilterBackend
from .models import CarReservation, AccommodationReservation, User
from .serializers import CarReservationSerializer, AccommodationReservationSerializer, UserSerializer, UserRegisterSerializer
from rest_framework.permissions import IsAuthenticated
from .filters import AccommodationReservationFilter


class UserViewSet(mixins.ListModelMixin,
                     mixins.CreateModelMixin,
                     mixins.RetrieveModelMixin,
                     mixins.UpdateModelMixin,
                     mixins.DestroyModelMixin,
                     viewsets.GenericViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'user__username'

    def get_serializer_class(self):
        if self.action == "create":
            return UserRegisterSerializer
        return UserSerializer


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


