from django.urls import path
from .views import NewsHomePage, NewsDetailPage, generate_news_view

urlpatterns = [
    path("all/", NewsHomePage.as_view(), name="all_news"),
    path("generate_news/", generate_news_view, name="GenerateNews-page"),
    path("<int:id>/", NewsDetailPage.as_view(), name="NewsDetail-page"),
    
]