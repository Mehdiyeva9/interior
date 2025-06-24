from django.contrib import admin
from intapp.models import Banner, Product, ProductContent, ProductPhoto, Content, Review, SiteSettings, Wishlist, Savelist, CustomUser
from django.contrib.auth.admin import UserAdmin
from django.contrib.admin import AdminSite

admin.site.register(Banner)
#admin.site.register(Product)
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

class ProductContentAdmin(admin.TabularInline):
    model = ProductContent
    extra = 1

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductContentAdmin]
    actions = ['make_in_stock', 'make_not_in_stock']

    @admin.action(description="Make selected products in stock")

    def make_in_stock(self, request, queryset):
        queryset.update(is_stock = True)

        text = str(len(queryset)) + "product added in stock." if queryset.count() == 1 else str(len(queryset)) + "products added in stock."
        self.message_user(request, text)

    @admin.action(description="Make selected products not in stock")

    def make_not_in_stock(self, request, queryset):
        queryset.update(is_stock = False)

        text = str(len(queryset)) + "product added not in stock." if queryset.count() == 1 else str(len(queryset)) + "products added not in stock."
        self.message_user(request, text)

AdminSite.site_header = "E-commerce Administration"
AdminSite.site_title = "E-commerce"