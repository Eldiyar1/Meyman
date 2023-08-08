# from rest_framework.routers import DefaultRouter
# from django.urls import path
# from .views import SignUpView, LoginView, ClientProfileView, OwnerProfileView, AdminProfileView, \
#     ClientListView, OwnerListView, AdminListView, ProfileViewSet
#
# router = DefaultRouter()
# router.register(r'profile', ProfileViewSet)
#
# urlpatterns = [
#     path('signup/', SignUpView.as_view(), name='signup'),
#     path('login/', LoginView.as_view(), name='login'),
#     path('profile/client/', ClientProfileView.as_view(), name='client-profile'),
#     path('profile/owner/', OwnerProfileView.as_view(), name='owner-profile'),
#     path('profile/admin/', AdminProfileView.as_view(), name='admin-profile'),
#     path('users/client/', ClientListView.as_view(), name='client-list'),
#     path('users/owner/', OwnerListView.as_view(), name='owner-list'),
#     path('users/admin/', AdminListView.as_view(), name='admin-list'),
# ]
#
# urlpatterns += router.urls