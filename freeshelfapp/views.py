from django.shortcuts import render, get_object_or_404
from freeshelfapp.models import Category, Author, Book
from django.views import generic

# Create your views here.
# def base(request):
#     """View function for home page of site."""
#     categories = Category.objects.all()
#     context = {
#        'categories': categories,
#     }
#     return render(request, 'base_generic.html', context=context)

def index(request):
    """View function for home page of site."""

    categories = Category.objects.all()
    books = Book.objects.all()

    # Number of visits to this view, as counted in the session variable.
    num_visits = request.session.get('num_visits', 0)
        # sets the value of the 'num_visits' session key to 0 if it has not previously been set
    request.session['num_visits'] = num_visits + 1
        # each time a request is received, the value is incremented and store it back in the session

    context = {
       'categories': categories,
       'books': books,
       'num_visits': num_visits
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)

class CategoryDetailView(generic.DetailView):
    """View class for category page of site."""
    model = Category

class AuthorDetailView(generic.DetailView):
    """View class for author page of site."""
    model = Author


