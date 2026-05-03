from django.contrib import admin
from django.utils.html import format_html
from .models import ItemPost, Tag


@admin.register(ItemPost)
class ItemPostAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'post_type',
        'user',
        'location',
        'date',
        'claimed',
        'image_preview'
    )

    list_filter = ('post_type', 'claimed', 'date', 'tags')
    search_fields = ('title', 'description', 'location', 'user__username')
    ordering = ('-created_at',)

    list_editable = ('claimed',)
    list_per_page = 20

    filter_horizontal = ('tags',)

    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="50" style="border-radius:6px;" />', obj.image.url)
        return "-"
    
    image_preview.short_description = "Image"


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    search_fields = ('name',)