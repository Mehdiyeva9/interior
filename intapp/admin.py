from django.contrib import admin
from intapp.models import Banner, Product, ProductContent, ProductPhoto, Content, Review, SiteSettings, Wishlist, Savelist, CustomUser
from django.contrib.auth.admin import UserAdmin

admin.site.register(Banner)
admin.site.register(Product)
admin.site.register(ProductContent)
admin.site.register(ProductPhoto)
admin.site.register(Content)
admin.site.register(Review)
admin.site.register(SiteSettings)
admin.site.register(Wishlist)
admin.site.register(Savelist)

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    fieldsets = (
        (None, {"fields": ("password", )}),
        (("Personal info"), {"fields": ("first_name", "last_name", "email")}),
        (
            ("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "user_permissions",
                ),
            },
        ),
        (("Important dates"), {"fields": ("last_login", "date_joined")}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("email", "usable_password", "password1", "password2"),
            },
        ),
    )
    list_display = ("email", "first_name", "last_name", "is_staff")
    search_fields = ("first_name", "last_name", "email")
    ordering = ("email",)
    readonly_fields = ("last_login", "date_joined")