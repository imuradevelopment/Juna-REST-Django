from rest_framework import generics, pagination, response
from rest_framework.utils.urls import remove_query_param, replace_query_param
from .models import Post, Category
from .serializers import CategorySerializer, PostSerializer, SimplePostSerializer
from django.db.models import Q


class CategoryList(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class PostDetail(generics.RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class StandardResultsSetPagination(pagination.PageNumberPagination):
    page_size = 10

    # オーバーライドすると返されるJSONの内容に手を加える事ができる
    def get_paginated_response(self, data):
        return response.Response({
            'next': self.get_next_link(),
            'previous': self.get_previous_link(),
            'count': self.page.paginator.count,
            'total_pages': self.page.paginator.num_pages,
            'current_page': self.page.number,
            'results': data,
            'page_size': self.page_size,
            'range_first': (self.page.number * self.page_size) - (self.page_size) + 1,
            'range_last': min((self.page.number * self.page_size), self.page.paginator.count),
        })

    # def get_next_link(self):
    #     if not self.page.has_next():
    #         return None
    #     page_number = self.page.next_page_number()
    #     return replace_query_param('', self.page_query_param, page_number)

    # def get_previous_link(self):
    #     if not self.page.has_previous():
    #         return None
    #     page_number = self.page.previous_page_number()
    #     if page_number == 1:
    #         return None
    #     return replace_query_param('', self.page_query_param, page_number)

class PostList(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = SimplePostSerializer
    pagination_class = StandardResultsSetPagination

    def get_queryset(self):
        queryset = super().get_queryset()

        keyword = self.request.query_params.get('keyword', None)
        if keyword:
            queryset = queryset.filter(
                Q(title__icontains=keyword) | Q(lead_text__icontains=keyword) | Q(main_text__icontains=keyword))

        category = self.request.query_params.get('category', None)
        if category:
            queryset = queryset.filter(category=category)

        return queryset