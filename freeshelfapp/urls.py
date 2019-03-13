from django.urls import path, re_path
from . import views

urlpatterns = [
    # re_path(r'\w*', views.base, name='base'),
    path('', views.index, name='index'),
    path('category/<slug:slug>', views.CategoryDetailView.as_view(), name='category-detail'),
    path('author/<slug:slug>', views.AuthorDetailView.as_view(), name='author-detail'),
]
