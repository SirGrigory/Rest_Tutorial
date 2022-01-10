from django.contrib import admin
from . import models


@admin.register(models.Post)
class AuthorAdmin(admin.ModelAdmin):
    list_display=('id', 'title', 'author', 'slug', 'status')
    prepopulated_fields = {'slug':('title',)}


admin.site.register(models.Category)