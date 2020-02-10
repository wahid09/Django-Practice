from django.contrib import admin
from .models import PersonelInfo
from .models import Product

# Register your models here.
class PersonelInfoAdmin(admin.ModelAdmin):
    search_fields = ['name', 'appoinment', 'joining_date']
    list_display = ['name', 'appoinment', 'joining_date']
    list_editable = ['appoinment', 'joining_date']
    list_filter = ['joining_date']
    list_per_page = 10
    class Meta:
        model = PersonelInfo


admin.site.register(PersonelInfo, PersonelInfoAdmin)

# Product Model
class ProductAdmin(admin.ModelAdmin):
    search_fields = ['title', 'description', 'price']
    list_display = ['title', 'price', 'active', 'updated']
    list_editable = ['price', 'active']
    list_filter = ['price', 'active']
    readonly_fields = ['updated', 'timestamp']
    prepopulated_fields = {"slug": ("title",)}
    list_per_page = 10

    class Meta:
        module = Product

admin.site.register(Product, ProductAdmin)
