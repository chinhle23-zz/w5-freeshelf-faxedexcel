from django.shortcuts import render, get_object_or_404, redirect
from freeshelfapp.models import Category, Author, Book
from django.views import generic
from freeshelfapp.forms import RegisterForm
from django.views.decorators.http import require_http_methods
from django.contrib.auth.decorators import login_required
from django.contrib import messages
# from django.http import HttpResponseRedirect

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

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get the context
        context = super(CategoryDetailView, self).get_context_data(**kwargs)
        # Create any data and add it to the context
        context['categories'] = Category.objects.all()
        return context

class AuthorDetailView(generic.DetailView):
    """View class for author page of site."""
    model = Author

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get the context
        context = super(AuthorDetailView, self).get_context_data(**kwargs)
        # Create any data and add it to the context
        context['categories'] = Category.objects.all()
        return context

# I don't know how to define this myself, so I will let Django-registration-redux do this for me
# def registration(request):
#     """View function for registration page of site."""

#     # If this is a POST request then process the Form data
#     if request.method == 'POST':

#         # Create a form instance and populate it with data from the request (binding):
#         form = RegisterForm(request.POST)

#     # Render the HTML template index.html with the data in the context variable
#     return render(request, 'index.html', context=context)




@require_http_methods(['POST'])
    # view decorator to require that only Post requests are accepted
    # https://docs.djangoproject.com/en/dev/topics/http/decorators/#
@login_required
    # view decorator to require that the user is logged in
    # https://docs.djangoproject.com/en/dev/topics/auth/default/
def book_favorite_view(request, book_pk):
    book = get_object_or_404(Book, pk=book_pk)
        # 'get_object_or_404()' function takes a Django model as its first argument and an arbitrary number of keyword arguments, which it passes to the 'get()' function of the model's manager
        # It raises 'Http404' if the object does not exist

    favorite, created = request.user.favorite_set.get_or_create(book=book)
        # '.get_or_created()' function returns a tuple of (object, created), where 'object' is the retrieved or created object and 'created' is a boolean specifying whether a new object was created
        # here, we're getting a favorite object corresponding to the book object...if there is one, then assign it to the variable 'favorite'.
        # if there isn't one, then create one and assign it to the variable 'favorite'
        # since it returns a tuple, we need to add the comma after 'favorite' variable declaration to declare another variable 'created' to capture True or False

    if created: # if the favorite object was newly created:
        messages.success(request, f"You have favorited {book.title}")
            # https://docs.djangoproject.com/en/dev/ref/contrib/messages/
    else: # if the favorite object already existed
        messages.info(request, f"You have unfavorited {book.title}")
        favorite.delete()
            # deletes the favorite object

    return redirect(book.get_absolute_url())
    # return HttpResponseRedirect(request.path_info)


