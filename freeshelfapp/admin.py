from django.contrib import admin
from freeshelfapp.models import Category, Author, Book, Favorite

# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'date_added', 'display_favorited_by','display_author', 'display_category')
    list_filter = ('date_added', 'author',)

@admin.register(Favorite)
class FavoriteAdmin(admin.ModelAdmin):
    list_display = ('user', 'book', 'favorited_at')
