from django.urls import path, re_path
from . import views

urlpatterns = [
    # re_path(r'\w*', views.base, name='base'),
    path('', views.index, name='index'),
    path('category/<slug:slug>', views.CategoryDetailView.as_view(), name='category-detail'),
    path('author/<slug:slug>', views.AuthorDetailView.as_view(), name='author-detail'),
    # path('registration/', views.registration, name='registration'),
    path('books/<int:book_pk>/favorite/', views.book_favorite_view, name="book_favorite"),
    path('myfavorites/', views.FavoritedBooksByUserListView.as_view(), name='my-favorites'),
]
