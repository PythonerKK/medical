from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import mixins, viewsets, filters
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.throttling import AnonRateThrottle, UserRateThrottle

from article.serializers import CategorySerializer, ArticleSerializer, ArticleDetailSerializer, SimpleCategorySerializer
from medical.article.models import Article, Category


class ArticlePagination(PageNumberPagination):
    page_size = 10


class ArticleViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin,
                     viewsets.GenericViewSet):
    """
    list:
    返回所有文章列表数据

    retrieve:
    返回文章详情数据
    """
    pagination_class = ArticlePagination
    queryset = Article.objects.all()
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    throttle_classes = (AnonRateThrottle, UserRateThrottle)
    search_fields = ("title", "content")
    ordering_fields = ("created_at", "read_nums", "comment_nums")
    # permission_classes = (IsAuthenticated,)


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

    def get_serializer_class(self):
        if self.action == "list":
            # 返回所有类别
            return SimpleCategorySerializer
        else:
            # 返回该类别下所有文章
            return CategorySerializer

