import xadmin

from medical.article.models import Category, Article

class CategoryAdmin:
    list_display = ['name', 'nums']
    list_filter = ['name']
    search_fields = ['name']
    ordering = ['-nums']


class ArticleAdmin:
    list_display = ['image_data', 'name', 'description', "normal_price", 'promotion_price', 'sn', 'created_at', 'status']
    list_filter = ['name', 'description']
    search_fields = ['name', 'description']
    ordering = ['-created_at']

xadmin.site.register(Category, CategoryAdmin)
# xadmin.site.register(Medicine, MedicineAdmin)
