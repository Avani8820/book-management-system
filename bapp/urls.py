from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import (
    BookViewSet,
    RegisterView,
    dashboard,
    book_list,
    add_book,
    edit_book,
    delete_book,
)

router = DefaultRouter()
router.register(r'books', BookViewSet)

urlpatterns = [
    # API URLs
    path('register/', RegisterView.as_view(), name='register'),

    # HTML Pages
    path('dashboard/', dashboard, name='dashboard'),

    path(
        'books-page/',
        book_list,
        name='book_list'
    ),

    path(
        'add-book/',
        add_book,
        name='add_book'
    ),

    path(
        'edit-book/<int:pk>/',
        edit_book,
        name='edit_book'
    ),

    path(
        'delete-book/<int:pk>/',
        delete_book,
        name='delete_book'
    ),
]

urlpatterns += router.urls