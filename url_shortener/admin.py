from django.contrib import admin

from url_shortener.models import Redirect


@admin.register(Redirect)
class UrlShortenerAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "created_at",
        "hits",
        "last_hit",
        "original_url",
    )
    search_fields = (
        "id",
        "created_at",
        "original_url",
    )
    list_filter = (
        "created_at",
        "last_hit",
    )
    ordering = ("last_hit",)
