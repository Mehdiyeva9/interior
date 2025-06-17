from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password
from intapp.models import Wishlist, Product, Banner, Review, SiteSettings, Savelist, CustomUser

class BannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Banner
        fields = "__all__"

class UserCreateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only = True)
    class Meta:
        model = CustomUser
        fields = ('username', 'password')

    def validate(self, data):
        validate_password(data["password"])
        return data
    def create(self, validated_data):
        username = validated_data['username']
        password = validated_data['password']

        user = CustomUser.objects.create_user(
            username = username,
            password = password
        )
        return user
    
class ProductRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ("name", "image", "price",)

class WishlistSerializer(serializers.ModelSerializer):
    product = ProductSerializer()
    user = UserCreateSerializer()
    class Meta:
        model = Wishlist
        fields = "__all__"

class WishlistCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wishlist
        fields = ("product",)

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'

class SiteSettingSerializer(serializers.ModelSerializer):
    class Meta:
        model = SiteSettings
        fields = '__all__'

class SavelistSerializer(serializers.ModelSerializer):
    product = ProductSerializer()
    user = UserCreateSerializer()
    class Meta:
        model = Savelist
        fields = '__all__'

class SavelistCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Savelist
        fields = ("product", )
