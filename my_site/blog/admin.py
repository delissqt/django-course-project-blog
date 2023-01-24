from django.contrib import admin

from .models import Author, Tag, Post
# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_filter = ("author", "tag", "date",) #has to be the same name as was declared in models (columns) in this caso models Post
    list_display = ("title", "date", "author",)
    prepopulated_fields = {"slug": ("title",)}


admin.site.register(Author)
admin.site.register(Tag)
admin.site.register(Post,PostAdmin)
