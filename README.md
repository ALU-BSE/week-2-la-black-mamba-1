# Django Book List with Pagination and Search

This project is a Django web application that displays a list of books. We have implemented key features to improve usability, including search functionality, adjustable pagination, and a clean Bootstrap-based interface.

## What We Have Done

- We have added a **search feature** to filter books by the author's name.
- We have implemented **pagination** to split results across pages.
- We have provided an option to adjust the number of items per page (5, 10, 15, 20).
- We have ensured that invalid page numbers and inputs are handled gracefully.
- We have styled the frontend using **Bootstrap 5** for a clean and responsive UI.

## Requirements

- Python 3.x
- Django 4.x or higher
- Internet access (for Bootstrap 5 CDN)

## Getting Started

1. Clone the repository:
   ```bash
   git clone <https://github.com/ALU-BSE/week-2-la-black-mamba-1.git>
   cd <pagination_project>
````

2. Create and activate a virtual environment:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:

   ```bash
   pip install django
   ```

4. Run migrations and start the server:

   ```bash
   python manage.py migrate
   python manage.py runserver
   ```

5. Open your browser and go to `http://127.0.0.1:8000/books/` to explore the features.

## Project Structure

```
books/
│
├── templates/books/
│   └── book_list.html     # HTML template for listing books
│
├── models.py              # Book model (title, author, published_year)
├── views.py               # book_list view logic
├── urls.py                # URL routing
```