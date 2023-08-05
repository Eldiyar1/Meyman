# from rest_framework import generics
# from .models import CustomUser
# from .serializers import CustomUserSerializer
# from django_filters.rest_framework import DjangoFilterBackend
# from django.contrib.auth import authenticate
# from rest_framework import generics, status
# from rest_framework.request import Request
# from rest_framework.response import Response
# from rest_framework.views import APIView
# from .serializers import SignUpSerializer, CustomUserSerializer
# from .permissions import IsAdminUser, IsOwnerOrReadOnly, IsClientOrReadOnly
# from .tokens import create_jwt_pair_for_user
# from rest_framework.permissions import IsAuthenticated
# from rest_framework.permissions import IsAuthenticatedOrReadOnly
#
#

#
#
# class OwnerView(generics.ListCreateAPIView):
#     queryset = CustomUser.objects.filter(user_type='owner')
#     serializer_class = CustomUserSerializer
#     permission_classes = (IsOwnerOrReadOnly,)
#
#
# class SignUpView(generics.GenericAPIView):
#     serializer_class = SignUpSerializer
#     permission_classes = [IsAdminUser, IsAuthenticated]
#
#     def post(self, request: Request):
#         data = request.data
#
#         serializer = self.serializer_class(data=data)
#
#         if serializer.is_valid():
#             serializer.save()
#
#             response = {"message": "User Created Successfully", "data": serializer.data}
#
#             return Response(data=response, status=status.HTTP_201_CREATED)
#
#         return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#
# class LoginView(APIView):
#     serializer_class = SignUpSerializer
#     permission_classes = [IsAdminUser, IsAuthenticated]
#
#     def post(self, request: Request):
#         email = request.data.get("email")
#         password = request.data.get("password")
#
#         user = authenticate(email=email, password=password)
#
#         if user is not None:
#
#             tokens = create_jwt_pair_for_user(user)
#
#             response = {"message": "Login Successfull", "tokens": tokens}
#             return Response(data=response, status=status.HTTP_200_OK)
#
#         else:
#             return Response(data={"message": "Invalid email or password"})
#
#     def get(self, request: Request):
#         content = {"user": str(request.user), "auth": str(request.auth)}
#
#         return Response(data=content, status=status.HTTP_200_OK)
#
#
# class ProfileViewSet(mixins.ListModelMixin,
#                      mixins.CreateModelMixin,
#                      mixins.RetrieveModelMixin,
#                      mixins.UpdateModelMixin,
#                      mixins.DestroyModelMixin,
#                      viewsets.GenericViewSet):
#     queryset = Profile.objects.all()
#     serializer_class = ProfileSerializer
#     permission_classes = [IsAuthenticatedOrReadOnly]
#     lookup_field = 'user__username'
#
#
# class AdminReviewViewSet(mixins.ListModelMixin,
#                          mixins.CreateModelMixin,
#                          viewsets.GenericViewSet):
#     queryset = AdminReview.objects.all()
#     serializer_class = AdminReviewSerializer
#     permission_classes = [IsAuthenticatedOrReadOnly]
#
#
# class AdminReviewDetailViewSet(mixins.RetrieveModelMixin,
#                                mixins.UpdateModelMixin,
#                                mixins.DestroyModelMixin,
#                                viewsets.GenericViewSet):
#     queryset = AdminReview.objects.all()
#     serializer_class = AdminReviewSerializer
#     permission_classes = [IsAuthenticatedOrReadOnly]
