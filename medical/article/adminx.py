import xadmin

from medical.article.models import Category, Article

class CategoryAdmin:
    list_display = ['name', 'nums']
    list_filter = ['name']
    search_fields = ['name']
    ordering = ['-nums']


class ArticleAdmin:
    list_display = ['title', 'category', 'comment_nums', "read_nums"]
    list_filter = ['title']
    search_fields = ['title', 'content']
    ordering = ['-created_at']


xadmin.site.register(Category, CategoryAdmin)
xadmin.site.register(Article, ArticleAdmin)
