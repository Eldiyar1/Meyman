from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import News
from .permissions import IsAdminUserOrReadOnly
from .serializers import NewsSerializer
from .filters import NewsFilter
from .utils import retrieve_trans
from ..travel.utils import LanguageParamMixin


class NewsViewSet(viewsets.ModelViewSet, LanguageParamMixin):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    permission_classes = [IsAdminUserOrReadOnly]
    filter_backends = [DjangoFilterBackend]
    filterset_class = NewsFilter
    search_fields = ['title', 'content']


    def retrieve(self, request, *args, **kwargs):
        return retrieve_trans(self, request, *args, **kwargs)
