from django.urls import path
from . import views

urlpatterns = [
    # path(*, views.base, name='base'),
    path('', views.index, name='index'),
    path('category/<slug:slug>', views.CategoryDetailView.as_view(), name='category-detail'),
    path('author/<slug:slug>', views.AuthorDetailView.as_view(), name='author-detail')
]
