from django.urls import path

from core.v1.api import CategoryView, ProductView
from rest_framework.routers import DefaultRouter

urlpatterns = [


]

router = DefaultRouter()
router.register(r'ctgs', CategoryView, basename='ctg')
router.register(r'products', ProductView, basename='product')
urlpatterns = router.urls
