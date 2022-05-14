from django.urls import path
from .views import index, articles

#On crée une liste contenant des urls pour notre page views.py
urlpatterns = [
    path("", index, name="index-blog"),
    path("article-<str:numero_article>/", articles, name="blog-article")
]