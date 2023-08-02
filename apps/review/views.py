from rest_framework import mixins, viewsets
from rest_framework.response import Response
from apps.review.models import Review
from apps.review.permissions import IsAdminUserOrReadOnly
from apps.review.serializers import ReviewSerializer
from googletrans import Translator

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
    permission_classes = [IsAdminUserOrReadOnly]

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        lang = self.get_language()

        instance.news = translator.translate(instance.news, dest=lang).text
        instance.content = translator.translate(instance.content, dest=lang).text
        instance.comment = translator.translate(instance.comment, dest=lang).text

        serializer = self.get_serializer(instance)
        return Response(serializer.data)

