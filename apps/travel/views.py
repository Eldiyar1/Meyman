from rest_framework import mixins, viewsets
from rest_framework.response import Response
from .models import Hotel, Hostel, Apartment, GuestHouse, Sanatorium
from .permissions import IsAdminUserOrReadOnly
from .serializers import HotelSerializer, HostelSerializer, ApartmentSerializer, GuestHouseSerializer, \
    SanatoriumSerializer
from googletrans import Translator

translator = Translator()


class LanguageParamMixin:
    def get_language(self):
        return self.request.query_params.get('lang', 'ru')


class AbstractHousingModelViewSet(mixins.ListModelMixin,
                                  mixins.CreateModelMixin,
                                  mixins.RetrieveModelMixin,
                                  mixins.UpdateModelMixin,
                                  mixins.DestroyModelMixin,
                                  viewsets.GenericViewSet):
    pass




class HotelViewSet(LanguageParamMixin, AbstractHousingModelViewSet):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer
    permission_classes = [IsAdminUserOrReadOnly]
    
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        lang = self.get_language()

        # Translate the fields
        instance.housing_name = translator.translate(instance.housing_name, dest=lang).text
        instance.description = translator.translate(instance.description, dest=lang).text

        serializer = self.get_serializer(instance)
        return Response(serializer.data)




class HostelViewSet(LanguageParamMixin, AbstractHousingModelViewSet):
    queryset = Hostel.objects.all()
    serializer_class = HostelSerializer
    permission_classes = [IsAdminUserOrReadOnly]
    
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        lang = self.get_language()

        # Translate the fields
        instance.housing_name = translator.translate(instance.housing_name, dest=lang).text
        instance.description = translator.translate(instance.description, dest=lang).text

        serializer = self.get_serializer(instance)
        return Response(serializer.data)

class ApartmentViewSet(LanguageParamMixin, AbstractHousingModelViewSet):
    queryset = Apartment.objects.all()
    serializer_class = ApartmentSerializer
    permission_classes = [IsAdminUserOrReadOnly]
    
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        lang = self.get_language()

        # Translate the fields
        instance.housing_name = translator.translate(instance.housing_name, dest=lang).text
        instance.description = translator.translate(instance.description, dest=lang).text  
        instance.location = translator.translate(instance.location, dest=lang).text
        
        serializer = self.get_serializer(instance)
        return Response(serializer.data)


class GuestHouseViewSet(LanguageParamMixin, AbstractHousingModelViewSet):
    queryset = GuestHouse.objects.all()
    serializer_class = GuestHouseSerializer
    permission_classes = [IsAdminUserOrReadOnly]
    
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        lang = self.get_language()

        # Translate the fields
        instance.housing_name = translator.translate(instance.housing_name, dest=lang).text
        instance.description = translator.translate(instance.description, dest=lang).text

        serializer = self.get_serializer(instance)
        return Response(serializer.data)


class SanatoriumViewSet(LanguageParamMixin, AbstractHousingModelViewSet):
    queryset = Sanatorium.objects.all()
    serializer_class = SanatoriumSerializer
    permission_classes = [IsAdminUserOrReadOnly]
    
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        lang = self.get_language()

        # Translate the fields
        instance.housing_name = translator.translate(instance.housing_name, dest=lang).text
        instance.description = translator.translate(instance.description, dest=lang).text

        serializer = self.get_serializer(instance)
        return Response(serializer.data)
