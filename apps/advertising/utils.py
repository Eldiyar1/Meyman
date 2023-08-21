def retrieve_trans(self, request, *args, **kwargs):
    from rest_framework.response import Response
    from apps.travel.utils import translator
    instance = self.get_object()
    lang = self.get_language()

    instance.title = translator.translate(instance.title, dest=lang).text
    instance.text = translator.translate(instance.text, dest=lang).text

    serializer = self.get_serializer(instance)
    return Response(serializer.data)
