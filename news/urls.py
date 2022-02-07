from operator import index
from textwrap import indent
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('test/', views.test, name="test"),
    path('test2/', views.ArticleListView.as_view()),
    path("author/", views.author, name="author"),
    path("politics/", views.politics, name="politics"),
    path("post/", views.post, name="post"),
    path("business/", views.business, name="business"),
    path("sports/", views.sports, name="sports"),
    path("art/", views.art, name="art"),
    path("world/", views.world, name="world"),
    path("travel/", views.travel, name="travel"),
    path("news_post/", views.contactus, name="contactus"),
    path("banner1/", views.banner1, name="banner1"),
    path("banner1/", views.banner2, name="banner2"),
    path("banner1/", views.banner3, name="banner3"),
    path("banner4/", views.banner1, name="banner1"),
]