from django.urls import path, include
from core.v1.api import CategoryView, ProductView
from rest_framework.routers import DefaultRouter

from core.v1.auth import LoginView, RegisView, LogoutView

router = DefaultRouter()
router.register(r'categories', CategoryView, basename='ctg')
router.register(r'products', ProductView, basename='product')

urlpatterns = [
    path('login/', LoginView.as_view()),
    path('regis/', RegisView.as_view()),
    path('logout/', LogoutView.as_view),
    path('', include(router.urls))

]
