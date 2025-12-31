# Admin-User API

A Django web application with an Admin Portal and User Portal that allows admins to manage entries (name, shape, color) displayed to users in a real-time grid format with visual shapes.

## Features

- **Admin Portal**: Add, edit, and delete entries with validation
- **User Portal**: Real-time grid display with colored shapes (triangles, squares, circles)
- **Database**: PostgreSQL backend
- **Real-time Updates**: User portal polls every 3 seconds for updates
- **Visual Shapes**: Color-coded shapes (red, blue, green, yellow)

## Project Structure

```
apps/
├── api/                    # Django project configuration
│   ├── config.py          # Settings file (database, apps, etc.)
│   ├── urls.py            # Root URL routing
│   └── wsgi.py            # WSGI configuration for production
├── main/                   # Main application
│   ├── tracker/           # Tracker app (models, views, forms)
│   ├── frontend/          # HTML templates
│   └── static/            # CSS styles
├── manage.py              # Django management script
├── requirements.txt       # Python dependencies
└── Procfile              # Production deployment config
```

## Setup Instructions

### Prerequisites

- Python 3.8+
- PostgreSQL installed and running
- pip (Python package manager)

### Step 1: Install Dependencies

```powershell
cd apps
pip install -r requirements.txt
```

### Step 2: Configure PostgreSQL

1. **Create the database**:
   ```sql
   psql -U postgres
   CREATE DATABASE admin_user_db;
   \q
   ```

2. **Set environment variables** (PowerShell):
   ```powershell
   $env:DB_NAME = "admin_user_db"
   $env:DB_USER = "postgres"
   $env:DB_PASSWORD = "your_password_here"
   $env:DB_HOST = "localhost"
   $env:DB_PORT = "5432"
   ```

   Or set permanently:
   ```powershell
   [Environment]::SetEnvironmentVariable('DB_PASSWORD', 'your_password', 'User')
   ```

### Step 3: Run Migrations

```powershell
cd apps
python manage.py makemigrations
python manage.py migrate
```

This creates all database tables including `tracker_entry`.

### Step 4: Run the Server

```powershell
python manage.py runserver
```

Visit:
- **User Portal**: http://127.0.0.1:8000/
- **Admin Portal**: http://127.0.0.1:8000/admin/

## Database Configuration

The database configuration is in `apps/api/config.py`:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('DB_NAME', 'admin_user_db'),
        'USER': os.environ.get('DB_USER', 'postgres'),
        'PASSWORD': os.environ.get('DB_PASSWORD', ''),
        'HOST': os.environ.get('DB_HOST', 'localhost'),
        'PORT': os.environ.get('DB_PORT', '5432'),
    }
}
```

Uses environment variables with sensible defaults.

## Using SQLTools (VS Code)

The project includes SQLTools configuration in `.vscode/settings.json`. To connect:

1. Install SQLTools extension in VS Code
2. Install SQLTools PostgreSQL Driver
3. Update password in `.vscode/settings.json`
4. Connect via SQLTools sidebar

## Troubleshooting

### "relation does not exist" error
- Run migrations: `python manage.py migrate`

### "password authentication failed"
- Check `DB_PASSWORD` environment variable matches your PostgreSQL password
- Verify PostgreSQL service is running

### "psql is not on PATH"
- This only affects `python manage.py dbshell`
- Use SQLTools in VS Code instead, or add PostgreSQL bin folder to PATH

### Port already in use
- Stop other Django servers, or use: `python manage.py runserver 8001`

## Production Deployment

The `Procfile` is configured for production deployment (Heroku, DigitalOcean, etc.):

```
web: gunicorn api.wsgi --log-file -
```

Make sure to:
- Set `DEBUG = False` in production
- Set a secure `SECRET_KEY`
- Configure proper `ALLOWED_HOSTS`
- Use environment variables for sensitive data
- Run `python manage.py collectstatic` before deployment

## Technology Stack

- **Backend**: Django 6.0
- **Database**: PostgreSQL
- **Frontend**: HTML, CSS, HTMX (for real-time updates)
- **Deployment**: Gunicorn + WhiteNoise (for static files)

## License

This project was created as a technical assignment.

