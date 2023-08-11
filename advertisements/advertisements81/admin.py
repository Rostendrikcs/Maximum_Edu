from django.contrib import admin
from .models import Advertisements81
# Register your models here.
class Advertisements81Admin(admin.ModelAdmin):
    list_display = ['id', 'title', 'description', 'price', 'auction', 'bu', 'created_time', 'updated_time']
    list_filter = ['auction', 'bu']
    auctions = ['make_auction_as_false']
    fieldsets = (
        ('Общее', {
            'fields': ('title', 'description', 'bu', 'image'),
        }),
        ('Финансы', {
            'fields': ('price', 'auction'),
            'classes': ['collapse']
        })
    )
    #здесь будет еще "Общее"
    @admin.action(description='No auction')
    def make_auction_as_false(self, request, queryset):
        queryset.update(auction=False)

admin.site.register(Advertisements81, Advertisements81Admin)