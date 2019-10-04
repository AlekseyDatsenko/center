from django.contrib import admin
from .models import Post, Video, About, News, Contacts, Comments, Image, Bible

class PostAdmin(admin.ModelAdmin):
    list_display = ('author', 'title', 'created_date', 'published_date')

class CommentsAdmin(admin.ModelAdmin):
    list_display = ('user', 'created')

admin.site.register(Post, PostAdmin)
admin.site.register(Video)
admin.site.register(About)
admin.site.register(News)
admin.site.register(Contacts)
admin.site.register(Comments, CommentsAdmin)
admin.site.register(Image)
admin.site.register(Bible)
