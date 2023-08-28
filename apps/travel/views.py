from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from .paginations import StandardResultsSetPagination, TravelLimitOffsetPagination
from .permissions import IsOwnerUserOrReadOnly, IsClientUserOrReadOnly
from .models import HousingReview, HousingReservation, Housing, Room, HistoryReservation, HousingAvailability
from .serializers import HousingReviewSerializer, HousingReservationSerializer, RoomGetSerializer, \
    RoomPostSerializer, HousingGetSerializer, HousingPostSerializer, HistoryReservationSerializer, \
    HousingAvailabilitySerializer
from .filters import HousingFilter, RoomFilter
from django.core.mail import send_mail

from .utils import retrieve_currency, LanguageParamMixin, CurrencyParaMixin, retrieve_housetrans, \
    retrieve_reservationtrans


class HousingViewSet(viewsets.ModelViewSet):
    queryset = Housing.objects.all()
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_class = HousingFilter
    permission_classes = [IsOwnerUserOrReadOnly]
    pagination_class = TravelLimitOffsetPagination
    ordering_fields = ['stars']
    serializer_class = HousingPostSerializer

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return HousingGetSerializer
        return self.serializer_class

    @action(detail=True, methods=['POST'])
    def add_to_favorite(self, request, pk=None):
        instance = self.get_object()
        instance.is_favorite = True
        instance.save()
        return Response('Объект успешно добавлен в избранное!')

    # def retrieve(self, request, *args, **kwargs):
    #     return retrieve_housetrans(self, request, *args, **kwargs)


class HousingReservationViewSet(viewsets.ModelViewSet):
    queryset = HousingReservation.objects.all()
    serializer_class = HousingReservationSerializer
    permission_classes = [IsClientUserOrReadOnly]

    def perform_create(self, serializer):
        instance = serializer.save()
        subject = 'Новое бронирование'
        message = (
            f"Уважаемый {instance.user.firstname}\n\n"
            f"Ваше бронирование на место жительства '{instance.housing}' ваша заявка принята.\n"
            f"Дата заезда: {instance.check_in_date}\n"
            f"Дата выезда: {instance.check_out_date}\n"
            f"Количество взрослых: {instance.adults}\n"
            f"Количество подростков: {instance.teens}\n"
            f"Количество детей: {instance.children}\n"
            f"Количество младенцев: {instance.infants}\n"
            f"Количество домашних животных: {instance.pets}"
        )
        from_email = "abdykadyrovsyimyk0708@gmail.com"
        recipient_email = instance.client_email
        try:
            send_mail(subject, message, from_email, [recipient_email])
        except Exception as e:
            return Response(
                {"error": "Не удалось отправить уведомление на почту"},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
        return Response(serializer.data, status=status.HTTP_201_CREATED)
  
    # def retrieve(self, request, *args, **kwargs):
    #     return retrieve_reservationtrans(self, request, *args, **kwargs)

class History_reservationsViewSet(viewsets.ModelViewSet):
    queryset = HistoryReservation.objects.all()
    serializer_class = HistoryReservationSerializer
    permission_classes = [IsClientUserOrReadOnly]

    def get_queryset(self):
        user = self.request.user
        # Фильтровать только бронирования, сделанные клиентом (пользователем с user_type='клиент')
        return HousingReservation.objects.filter(user=user, user__user_type='client')


class HousingAvailabilityViewSet(viewsets.ModelViewSet):
    queryset = HousingAvailability.objects.all()
    serializer_class = HousingAvailabilitySerializer
    permission_classes = [IsOwnerUserOrReadOnly]

    def availability(self, request, pk=None):
        housing = self.get_object()
        availability = HousingAvailability.objects.filter(housing=housing)
        serializer = HousingAvailabilitySerializer(availability, many=True)
        return Response(serializer.data)


class RoomViewSet(viewsets.ModelViewSet, CurrencyParaMixin):
    queryset = Room.objects.all()
    # permission_classes = [IsOwnerUserOrReadOnly]
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_class = RoomFilter
    ordering_fields = ['price_per_night']
    pagination_class = StandardResultsSetPagination
    serializer_class = RoomPostSerializer

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return RoomGetSerializer
        return self.serializer_class

    def retrieve(self, request, *args, **kwargs):
        return retrieve_currency(self, request, *args, **kwargs)


class ReviewViewSet(viewsets.ModelViewSet):
    queryset = HousingReview.objects.all()
    serializer_class = HousingReviewSerializer
    permission_classes = [IsOwnerUserOrReadOnly]
