# StudyBuddy

A Django-based productivity and task management application designed to help students organize their work, track progress, and build focused study habits.

## Features

### Task Management
- Create, edit, and delete tasks.
- Set task priorities.
- Add task descriptions, due dates, and estimated completion times.
- Mark tasks as completed.
- View pending and completed task statistics.

### User Authentication
- User registration and login.
- Individual task lists for each user.
- User-specific task ownership and access.

### Focus Mode
- Pomodoro-style focus timer.
- 25-minute focus sessions.
- 5-minute short breaks.
- 15-minute long breaks.
- Start, pause, resume, and reset controls.
- Optionally associate a focus session with a task.
- Save focus session history and track completed focus time.

## Tech Stack

- **Backend:** Python, Django
- **Frontend:** HTML, CSS, JavaScript
- **Database:** SQLite
- **Version Control:** Git and GitHub

## Project Structure

```text
studybuddy/
├── config/
│   ├── settings.py
│   └── urls.py
├── tasks/
│   ├── migrations/
│   ├── templates/
│   │   ├── registration/
│   │   └── tasks/
│   ├── static/
│   │   └── tasks/
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   └── admin.py
├── manage.py
├── db.sqlite3
└── README.md
```

## Getting Started

### 1. Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
cd studybuddy
```

### 2. Create a virtual environment

```bash
python3 -m venv venv
```

### 3. Activate the virtual environment

On macOS or Linux:

```bash
source venv/bin/activate
```

### 4. Install dependencies

```bash
pip install django
```

### 5. Apply database migrations

```bash
python manage.py migrate
```

### 6. Create an admin account (optional)

```bash
python manage.py createsuperuser
```

### 7. Run the development server

```bash
python manage.py runserver
```

Open http://127.0.0.1:8000/ in your browser.

## Future Improvements

- Weekly and daily productivity analytics.
- Improved focus session statistics.
- Task search, filtering, and sorting.
- Responsive dashboard improvements.
- Better tracking of interrupted and paused focus sessions.

## Author

Developed as a personal learning and portfolio project to explore Django, database design, authentication, frontend development, and productivity-focused application development.
