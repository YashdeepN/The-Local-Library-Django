from django.shortcuts import render
from .models import Book, BookInstance, Author, Genre
from django.views import generic

# Create your views here.


def index(request):
    """View funtion for home page of site."""

    # Generate counts of some of the main objects
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()

    # Available books (status = 'a')
    num_instances_available = BookInstance.objects.filter(
        status__exact='a').count()

    # The 'all()' is implied by dafault..
    num_authors = Author.objects.count()

    # Nos. of genres and books that contaion a particular word:

    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_authors': num_authors,
    }

    return render(request, 'index.html', context=context)


class BookListView(generic.ListView):
    model = Book
    paginate_by = 5
    constext_object_name = 'book_list'
    # to get 5 books containing the title mind
    # queryset = Book.objects.filter(title__icontains='yoga')[:5]
    queryset = Book.objects.all()
    template_name = 'books/book_list.html'


class BookDetailView(generic.DetailView):
    model = Book


class AuthorListView(generic.ListView):
    model = Author
    context_object_name = "author_list"
    queryset = Author.objects.all()
    template_name = "authors/author_list.html"


class AuthorDetailView(generic.DetailView):
    model = Author
