from django.contrib import admin
from display.models import Article


class AdminArticle(admin.ModelAdmin):
    list_display = ('author', 'pub_date')

admin.site.register(Article, AdminArticle)


