from rest_framework.pagination import PageNumberPagination
import math

from rest_framework.response import Response


class PagePagination(PageNumberPagination):
    page_size = 3
    max_page_size = 10
    page_size_query_param = 'size'

    def get_paginated_response(self, data):
        count = self.page.paginator.count
        total_pages = math.ceil(count/self.get_page_size(self.request))

        return Response({
            'total_pages': total_pages,
            'total_items':count,
            'prev':bool(self.get_previous_link()),
            'next':bool(self.get_next_link()),
            'data':data
        })