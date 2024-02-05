from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView, CreateAPIView

from base.helper import MethodNot
from core.models import Category, Product, Like
from core.serializer import CtgSerializer, ProductSerializer, LikeSerializer


class CategoryView(viewsets.ModelViewSet):
    permission_classes = (IsAdminUser,)
    queryset = Category.objects.all()
    serializer_class = CtgSerializer
    authentication_classes = (TokenAuthentication,)


class CategoryView2(GenericAPIView, MethodNot):
    permission_classes = (IsAuthenticated,)
    serializer_class = CtgSerializer
    authentication_classes = (TokenAuthentication,)

    def get(self, request, pk=None, *args, **kwargs):
        if pk:
            try:
                return Response(Category.objects.get(pk=pk).format())
            except:
                return Response({"error": "Bunaqa category mavjud emas"})
        categories = Category.objects.all().order_by("-pk")
        return Response([x.format() for x in categories])


class ProductView(viewsets.ModelViewSet):
    permission_classes = (IsAdminUser,)
    authentication_classes = (TokenAuthentication,)
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductView2(GenericAPIView, MethodNot):
    permission_classes = (IsAuthenticated,)
    serializer_class = ProductSerializer
    authentication_classes = (TokenAuthentication,)
    queryset = Product.objects.all()

    def get(self, request, pk=None, *args, **kwargs):
        if pk:
            try:
                return Response(Product.objects.get(pk=pk).format())
            except:
                return Response({"error": "Bunaqa product mavjud emas"})
        products = Product.objects.all().order_by("-pk")
        return Response([x.format() for x in products])


class LikeApi(CreateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = LikeSerializer
    authentication_classes = (TokenAuthentication,)


    # def post(self, request, product_id=None, *args, **kwargs):
    #     user = request.user
    #     product = Product.objects.get(id=product_id)
    #     current_likes = product.likes
    #     liked = Like.objects.filter(user=user, product=product).count()
    #     if not liked:
    #         liked = Like.objects.create(user=user, product=product)
    #         current_likes += 1
    #     else:
    #         liked = Like.objects.filter(user=user, product=product).delete()
    #         current_likes = current_likes-1
    #     product.likes = current_likes
    #     product.save()







