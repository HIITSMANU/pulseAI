from django.contrib import admin

from blog.models import BlogCategory,Blog

# Register your models here.

class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'created_at', 'publish')
    search_fields = ('title','content')
    list_filter = ('category','publish')
    list_editable = ('publish',)
    list_per_page = 1


admin.site.register(BlogCategory)
admin.site.register(Blog,BlogAdmin)
