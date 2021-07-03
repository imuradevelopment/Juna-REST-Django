from django.urls import path
from . import views

app_name = 'juna'

urlpatterns = [
    path('blog/posts/', views.PostList.as_view(), name='post_list'),
    path('blog/posts/<int:pk>/', views.PostDetail.as_view(), name='post_detail'),
    path('blog/categories/', views.CategoryList.as_view(), name='category_list'),
]