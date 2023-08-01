from rest_framework import mixins, viewsets

from .models import Profile, CarReservation, AccommodationReservation, AdminReview
from .serializers import ProfileSerializer, CarReservationSerializer, AccommodationReservationSerializer, \
    AdminReviewSerializer
from rest_framework.permissions import IsAuthenticated
from .permissions import IsAdminUserOrReadOnly


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


class AdminReviewViewSet(mixins.ListModelMixin,
                         mixins.CreateModelMixin,
                         viewsets.GenericViewSet):
    queryset = AdminReview.objects.all()
    serializer_class = AdminReviewSerializer
    permission_classes = [IsAdminUserOrReadOnly]


class AdminReviewDetailViewSet(mixins.RetrieveModelMixin,
                               mixins.UpdateModelMixin,
                               mixins.DestroyModelMixin,
                               viewsets.GenericViewSet):
    queryset = AdminReview.objects.all()
    serializer_class = AdminReviewSerializer
    permission_classes = [IsAdminUserOrReadOnly]
