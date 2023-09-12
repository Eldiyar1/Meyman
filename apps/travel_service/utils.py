from rest_framework.response import Response
from apps.travel.utils import translator


def retrieve_translate(self, request, *args, **kwargs):
    instance = self.get_object()
    lang = self.get_language()

    instance.transfer_location = translator.translate(instance.transfer_location, dest=lang).text
    instance.return_location = translator.translate(instance.return_location, dest=lang).text

    serializer = self.get_serializer(instance)
    return Response(serializer.data)

def retrieve_transfer_translate(self, request, *args, **kwargs):
    instance = self.get_object()
    lang = self.get_language()

    instance.description = translator.translate(instance.description, dest=lang).text

    serializer = self.get_serializer(instance)
    return Response(serializer.data)


def retrieve_transfer_translate_review(self, request, *args, **kwargs):
    instance = self.get_object()
    lang = self.get_language()

    instance.comment = translator.translate(instance.comment, dest=lang).text

    serializer = self.get_serializer(instance)
    return Response(serializer.data)
