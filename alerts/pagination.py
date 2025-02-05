# books/pagination.py

from rest_framework.pagination import PageNumberPagination

class CustomPagination(PageNumberPagination):
    page_size = 5  # Default page size
    page_size_query_param = 'limit'  # Allow clients to set page size
    max_page_size = 100  # Maximum limit for page size