from math import ceil

from django.core.paginator import Paginator
from django.utils.functional import cached_property


class UnequalFirstPagePaginator(Paginator):
    """
    Implelemt a paginator where 1st page can contain different number of items
    than rest of pages.
    """

    def __init__(self, object_list, per_page, orphans=0,
                 allow_empty_first_page=True,
                 first_page_size=None):

        super().__init__(object_list, per_page, orphans,
                         allow_empty_first_page)

        self.first_page_size = first_page_size or per_page

    @cached_property
    def num_pages(self):
        """
        Returns the total number of pages.
        """
        if self.count == 0 and not self.allow_empty_first_page:
            return 0
        hits = max(1, self.count - self.orphans)

        first_page_items = min(hits, self.first_page_size)
        first_page = int(ceil(first_page_items / float(self.first_page_size)))

        rest_items = max(hits - self.first_page_size, 0)
        rest_pages = int(ceil(rest_items / float(self.per_page)))

        return first_page + rest_pages

    def page(self, number):
        """
        Returns a Page object for the given 1-based page number.
        """
        number = self.validate_number(number)

        if number > 1:
            bottom = self.first_page_size + max(0, number - 2) * self.per_page
            top = bottom + self.per_page
        else:
            bottom = 0
            top = self.first_page_size

        if top + self.orphans >= self.count:
            top = self.count

        return self._get_page(self.object_list[bottom:top], number, self)
