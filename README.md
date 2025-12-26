# 🚀 Django Blog Platform

A modern, responsive, and feature-rich blog application built with Django 5 and Bootstrap 5. Designed with a focus on UI/UX, accessibility, and performance.

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?style=for-the-badge&logo=python&logoColor=white)
![Django](https://img.shields.io/badge/Django-5.0-092E20?style=for-the-badge&logo=django&logoColor=white)
![Bootstrap](https://img.shields.io/badge/Bootstrap-5-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white)

## ✨ Features

- **🎨 Modern UI/UX**: Clean, glassmorphism-inspired design using a custom Bootstrap 5 theme.
- **📱 Fully Responsive**: Seamless experience across mobile, tablet, and desktop devices.
- **📝 Dynamic Blog Posts**: Rich content rendering with categories and featured images.
- **🔍 Smart Navigation**: Intuitive pagination and related posts suggestions.
- **📫 Contact System**: Built-in contact form with server-side validation.
- **ℹ️ About Page**: Professional "About Us" section with team styling.
- **🧹 Clean Architecture**: Organized Django app structure with modular templates.

## 🛠️ Tech Stack

- **Backend**: Django 5 (Python)
- **Frontend**: HTML5, CSS3, Bootstrap 5, Custom CSS Variables
- **Database**: SQLite (Default, easily scalable to PostgreSQL)
- **Font**: Inter (Google Fonts)

## 🚀 Getting Started

Follow these steps to set up the project locally.

### Prerequisites

- Python 3.8 or higher installed
- pip (Python package manager)

### Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd blog-platform
   ```

2. **Create a virtual environment**
   ```bash
   # Windows
   python -m venv venv
   .\venv\Scripts\activate

   # macOS/Linux
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Apply database migrations**
   ```bash
   python manage.py migrate
   ```

5. **Create a superuser (optional, for admin access)**
   ```bash
   python manage.py createsuperuser
   ```

6. **Run the development server**
   ```bash
   python manage.py runserver
   ```

   Visit `http://127.0.0.1:8000/blog/` to view the application.

## 📂 Project Structure

```
blog-platform/
├── blog/                   # Main blog application
│   ├── migrations/         # Database migrations
│   ├── static/             # Static assets (CSS, Images)
│   ├── templates/          # HTML Templates
│   ├── admin.py            # Admin configuration
│   ├── models.py           # Database models
│   ├── urls.py             # App-level routing
│   └── views.py            # View logic
├── myapp/                  # Project configuration
│   ├── settings.py         # Global settings
│   └── urls.py             # Global routing
├── manage.py               # Django command-line utility
└── requirements.txt        # Project dependencies
```

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

This project is open source and available under the [MIT License](LICENSE).
