import xadmin
from xadmin import views


class BaseSetting:
    enable_themes = True
    use_bootswatch = True


class GlobalSettings:
    site_title = "校医室后台管理系统"
    site_footer = "广州商学院校医室"



xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(views.CommAdminView, GlobalSettings)
