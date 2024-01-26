from django.contrib import admin

from .models import (
    Category,
    Tag,
    Article,
    SubArticle,
    Comment,
    Author,
)


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name', )


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    search_fields = ('title',)


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    search_fields = ('title',)


class SubArticleInlineAdmin(admin.StackedInline):
    model = SubArticle
    extra = 0


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = (SubArticleInlineAdmin,)
    list_display = ('id', 'author', 'category', 'title', 'created_date')
    readonly_fields = ('slug', 'modified_date', 'created_date')
    search_fields = ('title',)
    list_filter = ('category', 'tags')
    date_hierarchy = 'created_date'
    filter_horizontal = ('tags',)
    autocomplete_fields = ('author',)
    save_on_top = True


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'article', 'name', 'get_image',)
    search_fields = ('name', 'article__title')
    # readonly_fields = ('created_date',)
