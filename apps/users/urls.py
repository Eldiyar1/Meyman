from rest_framework.routers import DefaultRouter
from django.urls import path

from .views import SignUpView, LoginView, ClientProfileView, OwnerProfileView, AdminProfileView, \
    ClientListView, OwnerListView, AdminListView, ProfileViewSet, ReviewSiteViewSet, LogoutView, VerifyOTP, \
    PasswordResetRequestAPIView, PasswordResetCodeAPIView, PasswordResetNewPasswordAPIView, TokenViewSet

router = DefaultRouter()
router.register('profile', ProfileViewSet)
router.register('review', ReviewSiteViewSet)
router.register('tokens', TokenViewSet, basename='token')

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('verify/', VerifyOTP.as_view(), name='confirm'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path("reset-password-email/", PasswordResetRequestAPIView.as_view(), name="search user and send mail"),
    path("reset-password-code/", PasswordResetCodeAPIView.as_view(), name="write code"),
    path("reset-new-password/<str:code>/", PasswordResetNewPasswordAPIView.as_view(), name="write new password"),
    path('profile/client/', ClientProfileView.as_view(), name='client-profile'),
    path('profile/owner/', OwnerProfileView.as_view(), name='owner-profile'),
    path('profile/admin/', AdminProfileView.as_view(), name='admin-profile'),
    path('client/', ClientListView.as_view(), name='client-list'),
    path('owner/', OwnerListView.as_view(), name='owner-list'),
    path('admin/', AdminListView.as_view(), name='admin-list'),
]

urlpatterns += router.urls
