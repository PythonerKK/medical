from django.shortcuts import render

# Create your views here.
from rest_framework import mixins, viewsets
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

from article.serializers import CategorySerializer, ArticleSerializer, ArticleDetailSerializer
from medical.article.models import Article, Category


class ArticlePagination(PageNumberPagination):
    page_size = 10


class ArticleViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin,
                     viewsets.GenericViewSet):
    pagination_class = ArticlePagination
    queryset = Article.objects.all()

    def get_serializer_class(self):
        if self.action == 'list':
            return ArticleSerializer
        else:
            return ArticleDetailSerializer

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.read_nums += 1
        instance.save()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)



class CategoryViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin,
                      viewsets.GenericViewSet):
    """所有类目和文章的api接口"""
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
