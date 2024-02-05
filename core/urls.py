from django.urls import path, include
from core.v1.api import CategoryView, ProductView, CategoryView2, ProductView2, LikeApi
from rest_framework.routers import DefaultRouter

from core.v1.auth import LoginView, RegisView, LogoutView

router = DefaultRouter()
router.register(r'categories', CategoryView, basename='ctg')
router.register(r'products', ProductView, basename='product')
router.register(r'products2', ProductView2, basename='product2')
router.register(r'categories2', CategoryView2, basename='ctg2')

urlpatterns = [
    path('login/', LoginView.as_view()),
    path('regis/', RegisView.as_view()),
    path('logout/', LogoutView.as_view()),
    path('like/', LikeApi.as_view()),
    # path('', include(router.urls))

]+router.urls
