from django.contrib import admin
from lifeflow.models import (   Author, Comment, Draft, Entry, Project, 
                                Flow, Language, Resource, RecommendedSite, Series,
                                SiteToNotify, Translation, Tag)



class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'link')
    search_fields = ['name']
    
    
class CommentAdmin(admin.ModelAdmin):
    list_display = ('entry', 'name', 'email', 'webpage', 'date')
    search_fields = ['name', 'email','body']

class EntryAdmin(admin.ModelAdmin):
    list_display = ('title', 'pub_date')
    search_fields = ['title', 'summary', 'body']
    # fields = (
    #     (None, {'fields' : ('title', 'slug', 'pub_date',)}),
    #     ('Content', {'fields': ('summary', 'body',)}),
    #     ('Options', {'fields': ('use_markdown', 'is_translation', 'send_ping', 'allow_comments', ), 'classes': 'collapse'}),
    #     ('Authors', {'fields' : ('authors',), 'classes': 'collapse'}),
    #     ('Resources', {'fields' : ('resources',), 'classes': 'collapse'}),
    #     ('Series', {'fields': ('series',), 'classes': 'collapse'}),
    #     ('Organization', {'fields': ('flows', 'tags',),}),
    # )


class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'language', 'license', 'size',)
    search_fields = ['title', 'summary', 'body']
    # fields = (
    #     (None, {'fields' : ('title', 'slug', 'size', 'language', 'license', 'use_markdown',)}),
    #     ('Content', {'fields': ('summary', 'body', 'resources')}),
    # )


admin.site.register(Author, AuthorAdmin)
admin.site.register(Entry, EntryAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(Comment, CommentAdmin)


for klass in [Flow, Language, Draft, Resource, Series, SiteToNotify, Tag, Translation]:
    class klassAdmin(admin.ModelAdmin):
        pass
    admin.site.register(klass, klassAdmin)