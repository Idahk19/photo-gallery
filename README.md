# Django Photo Gallery Project

A Django-based web application for managing, uploading, viewing, and displaying photos. The project demonstrates the use of Django models, views, templates, URL routing, forms, and the Django admin interface.

## Project Overview

The Django Photo Gallery allows users to explore a collection of photos through a simple web interface. Each photo can have information such as a title, description, image, and upload date.

The project is designed to demonstrate the basic principles of building a dynamic web application using Django.

## Project Structure

```text
photo-gallery/
├── photoapp/
│   ├── migrations/
│   ├── templates/
│   │   └── photoapp/
│   │       └── photo_detail.html
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── urls.py
│   ├── views.py
│   └── tests.py
├── photo_gallery/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
├── templates/
├── media/
├── manage.py
└── requirements.txt
```

## Technologies Used

* **Python** – Main programming language
* **Django** – Web framework
* **HTML** – Page structure
* **CSS** – Styling
* **SQLite/PostgreSQL** – Database
* **Django Templates** – Dynamic page rendering
* **Django Admin** – Photo management

## Core Features

### 1. Photo Gallery

Displays available photos in a gallery-style interface so users can browse the uploaded images.

### 2. Photo Details

Users can select a photo to view its details on a separate page.

The photo detail page can display:

* Photo
* Title
* Description
* Upload date
* Other relevant photo information

### 3. Photo Management

Photos can be stored in the database and managed through Django.

Administrators can add, edit, and delete photos using the Django admin panel.


## Media Files

The project uses Django's media-file configuration to store uploaded images.

Example:

```text
media/
└── photos/
    ├── image1.jpg
    ├── image2.jpg
    └── image3.png
```

## Setup Instructions

### 1. Clone the Repository

```bash
git clone <repository-url>
cd photo-gallery
```

### 2. Create a Virtual Environment

```bash
python -m venv myenv
```

### 3. Activate the Virtual Environment

**Windows:**

```bash
myenv\Scripts\activate
```

**macOS/Linux:**

```bash
source myenv/bin/activate
```

### 4. Install Dependencies

Install Django:

```bash
pip install django
```

If the project uses Pillow for image uploads:

```bash
pip install pillow
```

You can also install all project dependencies using:

```bash
pip install -r requirements.txt
```

### 5. Configure the Database

Update the database configuration in:

```text
photo_gallery/settings.py
```

The project can use SQLite for development or PostgreSQL for a production environment.

### 6. Create Database Migrations

```bash
python manage.py makemigrations
```

### 7. Apply Migrations

```bash
python manage.py migrate
```

### 8. Create a Superuser

```bash
python manage.py createsuperuser
```

Follow the prompts to create an administrator account.

### 9. Start the Development Server

```bash
python manage.py runserver
```

### 10. Access the Application

Open:

```text
http://127.0.0.1:8000/
```

The Django admin panel is available at:

```text
http://127.0.0.1:8000/admin/
```

## Running the Project

After completing the setup, run:

```bash
python manage.py runserver
```

Then visit:

```text
http://127.0.0.1:8000/
```

## Future Improvements

Possible improvements include:

* User registration and login
* User profiles
* Photo uploads through the website
* Photo reactions/likes
* Comments
* Photo search
* Photo categories
* Pagination
* Responsive design
* User-specific photo collections
* Photo deletion and editing
* Improved image validation

## Project Purpose

The main purpose of this project is to demonstrate how Django can be used to create a database-driven web application for managing and displaying images.

It demonstrates important Django concepts including:

* Models
* Views
* Templates
* URL routing
* Forms
* Database migrations
* Media files
* Django Admin
* CRUD operations

## License

This project is intended for educational and development purposes.
