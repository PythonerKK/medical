import xadmin
from xadmin import views

from medical.medicine.models import Category

class CategoryAdmin:
    list_display = ['name', 'desc','icon', "medicine_nums", 'created_at', 'updated_at']
    list_filter = ['name', 'created_at']
    search_fields = ['name', 'desc']
    ordering = ['-medicine_nums']

xadmin.site.register(Category, CategoryAdmin)
