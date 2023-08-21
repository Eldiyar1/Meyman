from apps.travel_service.constants import DESTINATION_CHOICES


def to_representation(self, instance):
    data = super().to_representation(instance)
    operating_area = data.get('operating_area', [])

    if 'Все' in operating_area:
        data['operating_area'] = [choice[0] for choice in DESTINATION_CHOICES if choice[0] != 'Все']

    return data