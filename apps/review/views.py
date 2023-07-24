from rest_framework import mixins, viewsets

from apps.review.models import Review
from apps.review.permissions import IsAdminUserOrReadOnly
from apps.review.serializers import ReviewSerializer


class ReviewViewSet(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.DestroyModelMixin,
                  viewsets.GenericViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsAdminUserOrReadOnly]

