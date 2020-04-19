import xadmin
from xadmin import views

from medical.medicine.models import Category, Medicine

class CategoryAdmin:
    list_display = ['image_data', 'name', 'description', "medicine_nums", 'created_at', 'updated_at']
    list_filter = ['name', 'created_at']
    search_fields = ['name', 'description']
    ordering = ['-medicine_nums']


class MedicineAdmin:
    list_display = ['image_data', 'name', 'description', "normal_price", 'promotion_price', 'sn', 'created_at', 'status']
    list_filter = ['name', 'description']
    search_fields = ['name', 'description']
    ordering = ['-created_at']

xadmin.site.register(Category, CategoryAdmin)
xadmin.site.register(Medicine, MedicineAdmin)
