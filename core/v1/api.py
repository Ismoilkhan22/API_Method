from rest_framework import viewsets, generics, filters
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView, CreateAPIView
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin
from rest_framework.viewsets import GenericViewSet

# ruxsatlar
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser

# modellar
from base.helper import MethodNot
from core.models import Category, Product
# serializerlar
from core.serializer import CtgSerializer, ProductSerializer, LikeSerializer

from rest_framework.generics import DestroyAPIView


class CategoryView(viewsets.ModelViewSet):
    permission_classes = (IsAdminUser,)
    queryset = Category.objects.all()
    serializer_class = CtgSerializer
    authentication_classes = (TokenAuthentication,)


class CategoryView2(
    ListModelMixin,
    RetrieveModelMixin,
    GenericViewSet
):
    permission_classes = (IsAuthenticated,)
    serializer_class = CtgSerializer
    queryset = Category.objects.all()


class ProductView(viewsets.ModelViewSet):
    permission_classes = (IsAdminUser,)
    authentication_classes = (TokenAuthentication,)
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [filters.SearchFilter]
    search_filters = ['title', 'desc']


class ProductView2(
    ListModelMixin,
    RetrieveModelMixin,
    GenericViewSet
):
    permission_classes = (IsAuthenticated,)
    serializer_class = ProductSerializer
    queryset = Product.objects.all()


class LikeApi(CreateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = LikeSerializer
    authentication_classes = (TokenAuthentication,)
