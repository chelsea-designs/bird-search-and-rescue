from django.urls import path
from . import views

urlpatterns = [
    path('', views.news, name='news'),
    path('add-post/', views.addNewsPost, name='add_news_post'),
    path('edit-post/<slug:slug>/', views.editNewsPost, name='edit_news_post'),
    path('delete-news-post/<str:pk>/',
         views.deleteNewsPost,
         name='delete_news_post'),
    path('<slug:slug>/', views.newsPostDetail, name='news_post_detail'),
]
