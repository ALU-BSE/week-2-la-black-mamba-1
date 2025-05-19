from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
from .models import Book

def book_list(request):
    search = request.GET.get('search', '')
    try:
        per_page = int(request.GET.get('per_page', 5))
    except ValueError:
        per_page = 5

    per_page_options = [5, 10, 15, 20]
    if per_page not in per_page_options:
        per_page = 5

    books = Book.objects.all().order_by('title')
    if search:
        books = books.filter(author__icontains=search)

    paginator = Paginator(books, per_page)
    page_number = request.GET.get('page')

    try:
        page_obj = paginator.get_page(page_number)
    except (PageNotAnInteger, EmptyPage):
        page_obj = paginator.get_page(1)

    return render(request, 'books/book_list.html', {
        'page_obj': page_obj,
        'search': search,
        'per_page': per_page,
        'per_page_options': per_page_options
    })
