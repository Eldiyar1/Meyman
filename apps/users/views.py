from rest_framework import generics, mixins, viewsets
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import CustomUser, ReviewSite
from .serializers import SignUpSerializer, LoginSerializer, ProfileSerializer, ReviewSiteSerializer, VerifySerializer
from .permissions import IsClient, IsOwner, IsAdminUser, IsUnregistered, IsOwnerAndClient
from .utils import login_user
from .paginations import ReviewPagination
from .service import VerifyService, RegisterService


class SignUpView(generics.CreateAPIView):
    serializer_class = SignUpSerializer
    permission_classes = [IsUnregistered]

    def post(self, request, *args, **kwargs):
        return RegisterService.create_user(self.serializer_class(data=request.data), request)
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(data={'errors': 'User already exist'}, status=status.HTTP_400_BAD_REQUEST)


class VerifyOTP(APIView):
    serializer_class = VerifySerializer
    permission_classes = [IsUnregistered]


    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        return VerifyService.verify_code(serializer)


class LoginView(APIView):
    serializer_class = LoginSerializer
    permission_classes = [IsUnregistered]

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            return login_user(serializer)
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ClientProfileView(generics.RetrieveUpdateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [IsClient]

    def get_object(self):
        return self.request.user


class OwnerProfileView(generics.RetrieveUpdateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [IsOwner]

    def get_object(self):
        return self.request.user


class AdminProfileView(generics.RetrieveUpdateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [IsAdminUser]

    def get_object(self):
        return self.request.user


class ClientListView(generics.ListAPIView):
    queryset = CustomUser.objects.filter(user_type='client')
    serializer_class = ProfileSerializer
    permission_classes = [IsAdminUser]


class OwnerListView(generics.ListAPIView):
    queryset = CustomUser.objects.filter(user_type='owner')
    serializer_class = ProfileSerializer
    permission_classes = [IsAdminUser]


class AdminListView(generics.ListAPIView):
    queryset = CustomUser.objects.filter(user_type='admin')
    serializer_class = ProfileSerializer
    permission_classes = [IsAdminUser]


class ProfileViewSet(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, viewsets.GenericViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [IsClient | IsOwner | IsAdminUser]

    def get_object(self):
        return self.request.user


class ReviewSiteViewSet(ModelViewSet):
    queryset = ReviewSite.objects.all()
    serializer_class = ReviewSiteSerializer
    permission_classes = [IsOwnerAndClient]
    pagination_class = ReviewPagination


class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        request.auth.delete()
        return Response({"message": "Logout Successful"}, status=status.HTTP_200_OK)
