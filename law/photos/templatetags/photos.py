from django import template
from ..models import WidePhoto, NarrowPhoto


register = template.Library()

PHOTO_TYPES = {
    'wide': {
        'model': WidePhoto,
        'default': 'http://placehold.it/582x420.jpg',
    },
    'narrow': {
        'model': NarrowPhoto,
        'default': 'http://placehold.it/269x615.jpg',
    },
}


@register.simple_tag()
def get_random_photo(photo_type):
    """get a random photo.

    :param photo_type: string one of 'wide' or 'narrow'
    """

    assert photo_type in ('wide', 'narrow'), 'photo_type should' \
                                             'be "wide" or "narrow"'

    photo_info = PHOTO_TYPES[photo_type]
    photo = photo_info['model'].objects.order_by('?').first()

    if not photo:
        return photo_info['default']

    return photo.photo.url
