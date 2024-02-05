from rest_framework import serializers

from core.models import Category, Product, User, Like


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'username', 'password']


class CtgSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class LikeSerializer(serializers.Serializer):
    product = serializers.IntegerField()
    like = serializers.BooleanField()

    def create(self, validated_data):
        like_obj, _ = Like.objects.get_or_create(product_id=validated_data['product'], user_id=self.context['request'].user.id)
        if like_obj.is_like != validated_data['like']:
            like_obj.is_like = validated_data['like']
            like_obj.save()
        return validated_data

    def to_representation(self, instance):
        return {"status": "Ok"}
