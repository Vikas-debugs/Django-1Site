from django.contrib import admin

from .models import Post
# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'user', 'created_at','updated_at', 'image']


from .models import story
@admin.register(story)
class StoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')  # Optional: shows in list view
