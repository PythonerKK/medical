import xadmin

from medical.address.models import Address, AddressImages


class AddressAdmin:
    list_display = ['name', 'lat', 'lng', "description", 'open_time', 'close_time', 'is_open']
    list_filter = ['is_open']
    search_fields = ['name', 'description']
    ordering = ['-is_open']
    style_fields = {'images': 'm2m_transfer'}
    filter_horizontal = ('images',)

class AddressImageAdmin:
    list_display = ['img']

xadmin.site.register(Address, AddressAdmin)
xadmin.site.register(AddressImages, AddressImageAdmin)
