# 📝 ToDo App (Django)

Simple CRUD application with user authentication.

## 🚀 Stack
- Python 3.x
- Django
- SQLite

## ⚙️ Features
- User registration & login
- Create / Read / Update / Delete tasks
- Django ORM & Templates

## ▶️ Run locally
```bash
git clone https://github.com/<your-username>/todo-app-django.git
cd todo-app-django
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
