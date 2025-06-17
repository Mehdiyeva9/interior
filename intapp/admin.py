from django.contrib import admin
from intapp.models import Banner, Product, ProductContent, ProductPhoto, Content, Review, SiteSettings,Wishlist, Savelist
from django.contrib.auth.models import User

admin.site.register(Banner)
admin.site.register(Product)
admin.site.register(ProductContent)
admin.site.register(ProductPhoto)
admin.site.register(Content)
admin.site.register(Review)
admin.site.register(SiteSettings)
admin.site.register(Wishlist)
admin.site.register(Savelist)