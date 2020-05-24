
from rest_framework import serializers

from medical.article.models import Article, Category
from medical.utils.helpers import removeHTML



class ArticleSerializer(serializers.ModelSerializer):
    content = serializers.SerializerMethodField()
    class Meta:
        model = Article
        exclude = ('updated_at',  'category')

    def get_content(self, obj):
        content = removeHTML(obj.content)
        return content if len(content) < 50 else content[:50] + "..."


class ArticleDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'



class ArticleBriefSerializer(serializers.HyperlinkedModelSerializer):
    """文章简要内容序列化"""
    content = serializers.SerializerMethodField()
    tags = serializers.SerializerMethodField()
    class Meta:
        model = Article
        fields = ('title', 'main_image', 'content', "read_nums", "comment_nums", "tags")

    def get_content(self, obj):
        content = removeHTML(obj.content)
        return content if len(content) < 50 else content[:50] + "..."

    def get_tags(self, obj):
        tags = ",".join([tag.name for tag in obj.tags.all()])
        return tags


class CategorySerializer(serializers.ModelSerializer):
    """类目下的所有文章序列化"""
    article_set = ArticleBriefSerializer(many=True) # 类目的所有商品
    class Meta:
        model = Category
        fields = ("id", "name", "article_set")


class SimpleCategorySerializer(serializers.ModelSerializer):
    """类目序列化"""
    class Meta:
        model = Category
        fields = ("id", "name")
