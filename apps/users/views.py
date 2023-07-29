from rest_framework import mixins, viewsets
from django_filters.rest_framework import DjangoFilterBackend
from .models import CarReservation, AccommodationReservation, CustomUser
from .serializers import CarReservationSerializer, AccommodationReservationSerializer
from .filters import AccommodationReservationFilter
from django.contrib.auth import authenticate
from rest_framework import generics, status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import SignUpSerializer, CustomUserSerializer
from .permissions import IsAdminUser, IsOwnerOrReadOnly, IsClientOrReadOnly
from rest_framework.permissions import IsAuthenticated


# Create your views here.

class ClientView(generics.ListCreateAPIView):
    queryset = CustomUser.objects.filter(user_type='client')
    serializer_class = CustomUserSerializer
    permission_classes = (IsClientOrReadOnly,)


class OwnerView(generics.ListCreateAPIView):
    queryset = CustomUser.objects.filter(user_type='owner')
    serializer_class = CustomUserSerializer
    permission_classes = (IsOwnerOrReadOnly,)


class SignUpView(generics.GenericAPIView):
    serializer_class = SignUpSerializer
    permission_classes = [IsAdminUser, IsAuthenticated]

    def post(self, request: Request):
        data = request.data

        serializer = self.serializer_class(data=data)

        if serializer.is_valid():
            serializer.save()

            response = {"message": "User Created Successfully", "data": serializer.data}

            return Response(data=response, status=status.HTTP_201_CREATED)

        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginView(APIView):
    serializer_class = SignUpSerializer

    def post(self, request):
        email = request.data.get("email")
        password = request.data.get("password")

        user = authenticate(request, email=email, password=password)

        if user is not None:
            response = {"message": "Login Successful"}
            return Response(data=response, status=status.HTTP_200_OK)
        else:
            return Response(data={"message": "Invalid email or password"}, status=status.HTTP_401_UNAUTHORIZED)


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
