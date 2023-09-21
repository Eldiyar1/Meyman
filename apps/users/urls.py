from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenRefreshView

from django.urls import path

from .views import SignUpView, LoginView, ProfileViewSet, ReviewSiteViewSet, LogoutView, VerifyOTP, \
    PasswordResetRequestAPIView, PasswordResetCodeAPIView, PasswordResetNewPasswordAPIView, \
    CustomUserView, ChangePasswordView, UpdateUserTypeView

router = DefaultRouter()
router.register('profile', ProfileViewSet)
router.register('review', ReviewSiteViewSet)

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('verify/', VerifyOTP.as_view(), name='confirm'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('update_user_type/', UpdateUserTypeView.as_view(), name='update_user_type'),
    path("reset-password-email/", PasswordResetRequestAPIView.as_view(), name="search user and send mail"),
    path("reset-password-code/", PasswordResetCodeAPIView.as_view(), name="write code"),
    path("reset-new-password/<str:code>/", PasswordResetNewPasswordAPIView.as_view(), name="write new password"),
    path('customusers/', CustomUserView.as_view(), name='users-list'),
    path('change-password/', ChangePasswordView.as_view(), name='change-password'),

]

urlpatterns += router.urls
