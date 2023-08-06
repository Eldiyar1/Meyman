from rest_framework import mixins, viewsets
from rest_framework.response import Response
from apps.review.models import Review
from apps.review.permissions import IsRegisteredUserOrReadOnly
from apps.review.serializers import ReviewSerializer
from googletrans import Translator
from django.db.models import Avg

translator = Translator()


class LanguageParamMixin:
    def get_language(self):
        return self.request.query_params.get('lang', 'ru')


class ReviewViewSet(LanguageParamMixin, mixins.ListModelMixin,
                    mixins.CreateModelMixin,
                    mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    viewsets.GenericViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsRegisteredUserOrReadOnly]



    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response({
            'reviews': serializer.data,
            'average_stars': self.get_average_stars(queryset),
            'total_reviews': queryset.count(),
        })

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        lang = self.get_language()

        instance.news = translator.translate(instance.news, dest=lang).text
        instance.content = translator.translate(instance.content, dest=lang).text
        instance.comment = translator.translate(instance.comment, dest=lang).text
        serializer = self.get_serializer(instance)
        return Response(serializer.data)
