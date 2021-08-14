from django.urls import path
from . import views

app_name = 'article'

urlpatterns = [
    path('articles/', views.ArticleListView.as_view()),
    path('articles/create/', views.ArticleCreateView.as_view()),
    path('articles/<uuid:pk>/', views.ArticleRUDView.as_view()),
    #path('articles/comments/<uuid:article_pk>/', views.CommentCreateView.as_view()),
    path('articles/comments/', views.CommentCreateView.as_view()),
    #path('articles/reply/<int:comment_pk>/', views.ReplyCreateView.as_view()),
    path('articles/comments/reply/', views.ReplyCreateView.as_view()),
    path('tags/', views.TagListView.as_view()),
    path('articles/favorite/', views.ArticleView.as_view())
]