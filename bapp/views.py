from rest_framework import viewsets, generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from django.contrib.auth.models import User
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter

from .models import Book
from .serializers import BookSerializer
from .user_serializer import UserRegisterSerializer



class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    filter_backends = [
        DjangoFilterBackend,
        SearchFilter,
        OrderingFilter
    ]

    filterset_fields = ['category']

    search_fields = [
        'title',
        'author'
    ]

    ordering_fields = [
        'title',
        'published_date',
        'created_at'
    ]


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegisterSerializer


from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from .models import Book
from .forms import BookForm


def dashboard(request):

    return render(
        request,
        'dashboard.html',
        {
            'total_books': Book.objects.count(),
            'total_users': User.objects.count()
        }
    )


def book_list(request):

    books = Book.objects.all()

    return render(
        request,
        'book_list.html',
        {'books': books}
    )


def add_book(request):

    if request.method == 'POST':

        form = BookForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('book_list')

    else:
        form = BookForm()

    return render(
        request,
        'book_form.html',
        {'form': form}
    )


def edit_book(request, pk):

    book = get_object_or_404(Book, pk=pk)

    if request.method == 'POST':

        form = BookForm(
            request.POST,
            instance=book
        )

        if form.is_valid():
            form.save()
            return redirect('book_list')

    else:
        form = BookForm(instance=book)

    return render(
        request,
        'book_form.html',
        {'form': form}
    )


def delete_book(request, pk):

    book = get_object_or_404(Book, pk=pk)

    if request.method == 'POST':

        book.delete()

        return redirect('book_list')

    return render(
        request,
        'delete_book.html',
        {'book': book}
    )