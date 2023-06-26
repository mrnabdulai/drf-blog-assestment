from rest_framework import pagination


class CustomPageNumberPagination(pagination.PageNumberPagination):
    page_size = 5
    page_query_param = "page"
    max_page_size = 10
    page_size_query_param = "per_page"
