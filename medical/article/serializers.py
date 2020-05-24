
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



class ArticleBriefSerializer(serializers.ModelSerializer):
    """蛋糕简要内容序列化"""
    content = serializers.SerializerMethodField()
    class Meta:
        model = Article
        fields = ('title', 'main_image', 'content', "read_nums", "comment_nums",)

    def get_content(self, obj):
        content = removeHTML(obj.content)
        return content if len(content) < 50 else content[:50] + "..."


class CategorySerializer(serializers.ModelSerializer):
    """类目和蛋糕序列化"""
    article_set = ArticleBriefSerializer(many=True) # 类目的所有商品
    class Meta:
        model = Category
        fields = ("id", "name", "article_set")
