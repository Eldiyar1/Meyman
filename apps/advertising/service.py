def create_slug(self, validated_data):
    from apps.advertising.models import Advertising
    from django.utils.text import slugify
    if not validated_data.get('slug'):
        title = validated_data.get('title')
        slug = slugify(title)

        queryset = Advertising.objects.filter(slug=slug)
        if queryset.exists():
            slug = f"{slug}-{queryset.count() + 1}"

        validated_data['slug'] = slug

    return super().create(validated_data)
