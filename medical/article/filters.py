import django_filters
from django.db.models import Q

from medical.article.models import Article


class ArticleFilter(django_filters.rest_framework.FilterSet):
    """文章过滤"""

