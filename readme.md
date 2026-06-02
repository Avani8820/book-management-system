#  Book Management System

A full-featured Book Management System developed using Django and Django REST Framework (DRF). The project provides RESTful APIs for managing books along with a Bootstrap-based web dashboard for administrators and users.

##  Features

### Authentication & Authorization

* User Registration API
* JWT Authentication using Simple JWT
* Access Token and Refresh Token support
* Protected API endpoints
* Role-based access through Django Admin

### Book Management

* Create Books
* View Books
* Update Books
* Delete Books
* Book listing dashboard

### Advanced API Features

* Search books by title and author
* Filter books by category
* Order books by title, publication date, and creation date
* Pagination support
* RESTful API architecture

### API Documentation

* Interactive Swagger Documentation using drf-yasg
* Easy API testing through browser interface

### Admin Dashboard

* Django Admin Panel
* Manage Users
* Manage Books
* View database records

### Custom Web Dashboard

* Bootstrap-based UI
* Dashboard statistics
* Book listing page
* Add Book form
* Edit Book form
* Delete Book functionality

---

##  Technologies Used

### Backend

* Python
* Django 6
* Django REST Framework

### Authentication

* JWT (JSON Web Tokens)
* Simple JWT

### API Documentation

* Swagger UI
* drf-yasg

### Frontend

* HTML5
* Bootstrap 5
* Django Templates

### Database

* SQLite (Development)
* Compatible with PostgreSQL/MySQL for Production

### Deployment Ready

* AWS EC2 Compatible
* Gunicorn Compatible
* Nginx Compatible

---

##  Project Structure

bookmanage/

├── accounts/

├── bapp/

├── templates/

│ ├── base.html

│ ├── dashboard.html

│ ├── book_list.html

│ ├── book_form.html

│ └── delete_book.html

├── bookmanage/

├── manage.py

├── requirements.txt

└── README.md

---

## API Endpoints

### Authentication

POST /api/register/

POST /api/token/

POST /api/token/refresh/

### Books

GET /api/books/

POST /api/books/

GET /api/books/{id}/

PUT /api/books/{id}/

DELETE /api/books/{id}/

### Dashboard

/api/dashboard/

/api/books-page/

/api/add-book/

---

## Search Examples

/api/books/?search=Python

## Filter Examples

/api/books/?category=Programming

## Ordering Examples

/api/books/?ordering=title

/api/books/?ordering=-published_date

## Pagination

/api/books/?page=1

---

## Installation

### Clone Repository

git clone <repository-url>

cd book-management-system

### Create Virtual Environment

python -m venv venv

### Activate Environment

Windows:

venv\Scripts\activate

### Install Dependencies

pip install -r requirements.txt

### Run Migrations

python manage.py migrate

### Create Superuser

python manage.py createsuperuser

### Start Server

python manage.py runserver

---

## Future Enhancements

* User Login Page
* User Registration Page
* Book Cover Image Upload
* User Roles and Permissions
* Email Notifications
* AWS Deployment
* PostgreSQL Integration
* Docker Support

---

## Author

Developed by Avani as part of a Django REST Framework learning and portfolio project demonstrating backend development, API design, JWT authentication, database integration, and web application development.
