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
            'totalPages': self.page.paginator.num_pages,
            'currentPage': self.page.number,
            'results': data,
            'pageSize': self.page_size,
            'rangeFirst': (self.page.number * self.page_size) - (self.page_size) + 1,
            'rangeLast': min((self.page.number * self.page_size), self.page.paginator.count),
        })


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