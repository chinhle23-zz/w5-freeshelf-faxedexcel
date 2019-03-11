from django.shortcuts import render
from freeshelfapp.models import Category, Author, Book
from django.views import generic

# Create your views here.
def index(request):
   """View function for home page of site."""

   # Generate counts of some of the main objects
   num_books = Book.objects.all().count()
  
   # The 'all()' is implied by default.   
   num_authors = Author.objects.count()

   context = {
       'num_books': num_books,
       'num_authors': num_authors,
   }

   # Render the HTML template index.html with the data in the context variable
   return render(request, 'index.html', context=context)