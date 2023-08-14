from rest_framework import generics, mixins, viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate
from .models import CustomUser, ReviewSite
from .serializers import SignUpSerializer, LoginSerializer, ProfileSerializer, ReviewSiteSerializer
from .permissions import IsClient, IsOwner, IsAdminUser, IsUnregistered
from .tokens import create_jwt_pair_for_user


class SignUpView(generics.CreateAPIView):
    serializer_class = SignUpSerializer
    permission_classes = [IsUnregistered]


class LoginView(APIView):
    serializer_class = LoginSerializer
    permission_classes = [IsUnregistered]

    def post(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            user = authenticate(email=serializer.validated_data["email"],
                                password=serializer.validated_data["password"])

            if user is not None:
                tokens = create_jwt_pair_for_user(user)

                response = {"message": "Login Successful", "tokens": tokens}
                return Response(data=response, status=status.HTTP_200_OK)
            else:
                return Response(data={"message": "Invalid email or password"}, status=status.HTTP_401_UNAUTHORIZED)
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


class ReviewSiteViewSet(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, viewsets.GenericViewSet):
    queryset = ReviewSite.objects.all()
    serializer_class = ReviewSiteSerializer
    permission_classes = [IsAdminUser]
