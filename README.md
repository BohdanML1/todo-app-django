# 📝 ToDo App (Django)

Simple CRUD application with user authentication.

## 🚀 Stack
- Python 3.x
- Django
- SQLite

## 🔗 URL Structure
| URL | Description |
|------|-------------|
| `/login/` | User login |
| `/register/` | User registration |
| `/tasks/` | Task list (CRUD) |


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


## 📸 Screenshots
### Login
![Login](screenshots/login.png)

### Register
![Register](screenshots/register.png)

### Task List
![Task List](screenshots/task_list.png)

### Create Task
![Create Task](screenshots/task_create.png)

### Update Task
![Update Task](screenshots/task_update.png)
