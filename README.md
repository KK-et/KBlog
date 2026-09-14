# KBlog

KBlog is a simple blogging platform built with **Django**. It allows users to create, edit, and view blog posts through a clean and straightforward interface.

## Features

* Create blog posts
* Edit existing posts
* View published posts
* Django-based backend
* HTML and CSS frontend
* Database integration through Django models
* Simple and user-friendly interface

## Technologies Used

* **Python**
* **Django**
* **HTML**
* **CSS**
* **SQLite / Django database**

## Project Structure

```text
KBlog/
├── blog/
│   ├── migrations/
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
│
├── blog_project/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── static/
├── templates/
├── manage.py
├── requirements.txt
├── Procfile
└── .gitignore
```

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/KK-et/KBlog.git
cd KBlog
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

Activate it:

**Windows:**

```bash
venv\Scripts\activate
```

**Linux/macOS:**

```bash
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run migrations

```bash
python manage.py migrate
```

### 5. Start the development server

```bash
python manage.py runserver
```

Open the local development server shown in your terminal in a web browser.

## Purpose

This project was built as a practical project to develop my understanding of **Python, Django, web development, databases, and deploying web applications**.

## Author

**KK-et**

GitHub: https://github.com/KK-et
