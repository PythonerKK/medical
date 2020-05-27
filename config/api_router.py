from rest_framework.routers import DefaultRouter

from medical.address.views import AddressViewSet
from medical.article.views import CategoryViewSet, ArticleViewSet
from medical.users.api.views import UserViewSet
from medical.medicine.views import MedicineCategoryViewSet, MedicineViewSet

router = DefaultRouter()

router.register("users", UserViewSet)
router.register("article_categories", CategoryViewSet, basename="article_categories")
router.register("articles", ArticleViewSet, basename="articles")
router.register("medicines", MedicineCategoryViewSet, basename="medicine_categories")
router.register("medicines", MedicineViewSet, basename="medicines")
router.register("addresses", AddressViewSet, basename="addresses")


app_name = "api"
urlpatterns = router.urls
