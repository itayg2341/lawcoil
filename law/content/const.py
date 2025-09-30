from enum import unique, Enum

CATEGORY_URL = r'^(?P<cat_slug>[\w-]+)/$'
ITEM_URL = r'^(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/(?P<day>[0-9]{2})/(?P<slug>[\w-]+)/$'
ITEM_WITH_CATEGORY_URL = r'^(?P<cat_slug>[\w-]+)/' + ITEM_URL[1:]
ITEM_WITH_TWO_CATEGORY_URL = r'^(?P<parent_cat_slug>[\w-]+)/' + ITEM_WITH_CATEGORY_URL[1:]

CONTENT_TYPES_RE = '(?P<content_type>news|articles|computer-law|legislation)'


@unique
class CONTENT_TYPE(Enum):
    articles = 1
    news = 2
    computer_law = 3
    legislation = 4
