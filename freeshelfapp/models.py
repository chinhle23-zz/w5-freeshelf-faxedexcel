from django.db import models
from django.urls import reverse
    # Used to generate URLs by reversing the URL patterns
import uuid
    # Required for unique book instances
from django.contrib.auth.models import User
    # Required to make use of 'User' class
from datetime import date
from django.utils.text import slugify

# Create your models here.
class Category(models.Model):
    """Model representing a book category."""
    name = models.CharField(max_length=200, help_text='Enter a book category (e.g. Python, HTML, etc.)')
    slug = models.SlugField(unique=True, null=True, blank=True)

    class Meta:
        ordering = ['name']

    def save(self, *args, **kwargs):
        self.set_slug()
        super().save(*args, **kwargs)

    def set_slug(self):
        if self.slug:
            return
        base_slug = slugify(self.name)
        slug = base_slug
        n = 0
        while Category.objects.filter(slug=slug).count():
            n += 1
            slug = base_slug + "-" + str(n)
        self.slug =slug

    def get_absolute_url(self):
        """Returns the url to access a particular category instance."""
        return reverse('category-detail', args=[str(self.id)])
    
    def __str__(self):
        """String for representing the Model object."""
        return self.name

class Author(models.Model):
    """Model representing an author."""
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, null=True, blank=True)

    class Meta:
        ordering = ['name']

    def save(self, *args, **kwargs):
        self.set_slug()
        super().save(*args, **kwargs)

    def set_slug(self):
        if self.slug:
            return
        base_slug = slugify(self.name)
        slug = base_slug
        n = 0
        while Category.objects.filter(slug=slug).count():
            n += 1
            slug = base_slug + "-" + str(n)
        self.slug =slug

    def get_absolute_url(self):
        """Returns the url to access a particular author instance."""
        return reverse('author-detail', args=[str(self.id)])

    def __str__(self):
        """String for representing the Model object."""
        return self.name

class Book(models.Model):
    """Model representing a book (but not a specific copy of a book)."""
    title = models.CharField(max_length=200)

    # ManyToManyField used because author can write many books. Books can have many authors.
    author = models.ManyToManyField(Author)

    summary = models.TextField(max_length=1000, help_text='Enter a brief description of the book')
    
    date_added = models.DateField(null=True, blank=True)

    # ManyToManyField used because category can contain many books. Books can cover many categories.
    # category class has already been defined so we can specify the object above.
    category = models.ManyToManyField(Category, help_text='Select a category for this book')

    url = models.URLField(max_length=2000, null=True, blank=True)
    picture = models.ImageField(upload_to='books/', null=True, blank=True)
        # https://docs.djangoproject.com/en/2.1/ref/models/fields/


    class Meta:
        ordering = ['-date_added',]

    def display_category(self):
        """Create a string for the Category. This is required to display category in Admin."""
        return ', '.join(category.name for category in self.category.all()[:3])
            # str.join(iterable) --> https://docs.python.org/3.7/library/stdtypes.html?highlight=join#str.join
            # 1st three '[:3]' category items in the 'self.category.all()' for a 'Book' object will be joined separated by a comma ', '

    display_category.short_description = 'category'
        # '.short_description' is a built-in Django attribute to provide human-readable descriptions for callback functions
        # https://docs.djangoproject.com/en/2.1/ref/contrib/admin/actions/

    def display_author(self):
        """Create a string for the Category. This is required to display category in Admin."""
        return ', '.join(author.name for author in self.author.all()[:3])
            # str.join(iterable) --> https://docs.python.org/3.7/library/stdtypes.html?highlight=join#str.join
            # 1st three '[:3]' category items in the 'self.category.all()' for a 'Book' object will be joined separated by a comma ', '

    display_author.short_description = 'author'
        # '.short_description' is a built-in Django attribute to provide human-readable descriptions for callback functions
        # https://docs.djangoproject.com/en/2.1/ref/contrib/admin/actions/

    def __str__(self):
        """String for representing the Model object."""
        return self.title

    def get_absolute_url(self):
        """Returns the url to access a detail record for this book."""
        return reverse('book-detail', args=[str(self.id)])