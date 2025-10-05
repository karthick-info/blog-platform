# MyApp - Django Blog

A modern, feature-rich blog application built with Django.

## 🚀 Features

- **Blog Posts** - Create, manage, and display blog posts
- **Categories** - Organize posts by categories  
- **Contact Form** - Functional contact form with validation
- **Pagination** - Efficient post listing with pagination
- **Admin Interface** - Django admin for content management
- **Slug URLs** - SEO-friendly URLs using slugs
- **Related Posts** - Show related posts by category

## 📁 Project Structure
myapp/
├── blog/
│ ├── migrations/
│ ├── static/
│ ├── templates/blog/
│ │ ├── includes/
│ │ ├── about.html
│ │ ├── base.html
│ │ ├── contact.html
│ │ ├── detail.html
│ │ └── index.html
│ ├── admin.py
│ ├── form.py
│ ├── models.py
│ ├── urls.py
│ └── views.py
├── myapp/
│ ├── settings.py
│ ├── urls.py
│ └── wsgi.py
├── db.sqlite3
└── manage.py

## 🛠️ Installation

# Clone repository
git clone https://github.com/yourusername/django-blog-website.git
cd django-blog-website

# Create virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install dependencies
pip install django

# Run migrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser

# Run server
python manage.py runserver
Models
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    slug = models.SlugField(unique=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
🎯 URLs
/ - Homepage with paginated posts

/post/<slug>/ - Post detail page

/contact/ - Contact form

/about/ - About page

/admin/ - Admin interface

🔧 Admin Features
Custom Post admin with search and filters

Category management

List display customization

📝 Requirements
Django>=4.0
🤝 Contributing
Fork the project

Create your feature branch

Commit your changes

Push to the branch

Open a Pull Request
