from django.urls import path,include
from intapp.api import views

urlpatterns = [
    path('user-create/', views.UserCreateAPIView.as_view()),
    path('banner-list/',views.BannerListAPIView.as_view()),
    path('wishlist-create/',views.WishlistCreateAPIView.as_view()),
    path('user-wishlist/',views.UserWishlistListAPIView.as_view()),
    path('wishlist/',views.WishlistListAPIView.as_view()),
    path('product-list/', views.ProductListAPIView.as_view()),
    path('product-retrieve/', views.ProductRetrieveAPIView.as_view()),
    path('review-list/',views.ReviewListAPIView.as_view()),
    path('settings-list/', views.SiteSettingsListAPIView.as_view()),
    path('savelist-create/', views.SavelistCreateAPIView.as_view()),
    path('savelist/', views.SavelistListAPIView.as_view()),
    path('user-savelist/',views.UserSavelistListAPIView.as_view())
]