from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView
from intapp.api.serializers import UserCreateSerializer, SiteSettingSerializer, ReviewSerializer, WishlistSerializer, WishlistCreateSerializer, BannerSerializer, ProductSerializer, ProductRetrieveSerializer, SavelistSerializer, SavelistCreateSerializer
from intapp.models import Wishlist, Banner, Product, Review, SiteSettings, Savelist, CustomUser
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, IsAdminUser

class BannerListAPIView(ListAPIView):
    queryset = Banner.objects.all()
    serializer_class = BannerSerializer

class ProductListAPIView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductRetrieveAPIView(RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductRetrieveSerializer
    lookup_field = ('id')

class UserCreateAPIView(CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserCreateSerializer

class UserWishlistListAPIView(ListAPIView):
    def get_queryset(self):
        return Wishlist.objects.filter(
            user = self.request.user
        )
    serializer_class = WishlistSerializer

class WishlistListAPIView(ListAPIView):
    queryset = Wishlist.objects.all()
    serializer_class = WishlistSerializer
    permission_classes = (IsAdminUser, )

class WishlistCreateAPIView(CreateAPIView):
    queryset = Wishlist.objects.all()
    serializer_class = WishlistCreateSerializer
    permission_classes = (IsAuthenticated,)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data = request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)
    
class ReviewListAPIView(ListAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

class SiteSettingsListAPIView(ListAPIView):
    queryset = SiteSettings.objects.all()
    serializer_class = SiteSettingSerializer

class SavelistListAPIView(ListAPIView):
    queryset = Savelist.objects.all()
    serializer_class = SavelistSerializer
    permission_classes = (IsAdminUser, )

class SavelistCreateAPIView(CreateAPIView):
    queryset = Savelist.objects.all()
    serializer_class = SavelistCreateSerializer
    permission_classes = (IsAuthenticated, )
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data = request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)

class UserSavelistListAPIView(ListAPIView):
    def get_queryset(self):
        return Savelist.objects.filter(
            user = self.request.user
        )
    serializer_class = SavelistSerializer