from rest_framework.routers import DefaultRouter

from medical.article.views import CategoryViewSet, ArticleViewSet
from medical.users.api.views import UserViewSet
from medical.medicine.views import MedicineCategoryViewSet

router = DefaultRouter()

router.register("users", UserViewSet)
router.register("article_categories", CategoryViewSet)
router.register("articles", ArticleViewSet)
router.register("medicines", MedicineCategoryViewSet)


app_name = "api"
urlpatterns = router.urls
