from django.contrib import admin
from .models import Post, Comment


class CommentAdminLInline(admin.TabularInline):
    model = Comment
    fields =['text']
    extra = 0
    
class PostAdmin(admin.ModelAdmin):
    list_display =['id','title','is_enable','publish_time','create_time']
    inlines=[CommentAdminLInline]
    
#class CommentAdmin(admin.ModelAdmin):
    #list_display =['post','text','create_time']

admin.site.register(Post,PostAdmin)
#admin.site.register(Comment,CommentAdmin)