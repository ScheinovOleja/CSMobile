from rest_framework.routers import DefaultRouter

from .views import AddDataSet

router = DefaultRouter()
router.register(r'add_data', AddDataSet, basename='add_data')
urlpatterns = router.urls
