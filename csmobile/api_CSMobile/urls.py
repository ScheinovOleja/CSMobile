from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views as view

router = DefaultRouter()
router.register('add_data', view.AddDataSet, basename='add_data')
urlpatterns = router.urls
