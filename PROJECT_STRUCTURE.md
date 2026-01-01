# Project Structure & File Usage Guide

## 📁 Core Django Application Files

### Root Level (`apps/`)

#### `manage.py`
**Purpose**: Django's command-line utility for administrative tasks
**Usage**: Run Django commands like `python manage.py runserver`, `makemigrations`, `migrate`, etc.
**Required**: ✅ Yes - Core Django file

#### `requirements.txt`
**Purpose**: Python package dependencies
**Usage**: Install with `pip install -r requirements.txt`
**Required**: ✅ Yes - Lists all Python packages needed

#### `Procfile`
**Purpose**: Configuration for production deployment (Heroku, DigitalOcean, etc.)
**Usage**: Tells the platform how to run your app
**Status**: ⚠️ Needs fix (currently says `core.wsgi`, should be `api.wsgi`)
**Required**: ✅ Yes (for production deployment)

---

### Django Project Configuration (`apps/api/`)

#### `api/__init__.py`
**Purpose**: Makes `api` a Python package
**Required**: ✅ Yes

#### `api/config.py`
**Purpose**: Django settings file - all application configuration
**Contains**: 
- Database settings (PostgreSQL)
- Installed apps
- Middleware
- Templates configuration
- Static files configuration
- Security settings
**Required**: ✅ Yes - Core Django settings file

#### `api/urls.py`
**Purpose**: Root URL configuration - routes URLs to different apps
**Usage**: Main URL dispatcher that includes app-specific URLs
**Required**: ✅ Yes - Defines URL routing

#### `api/wsgi.py`
**Purpose**: WSGI configuration for production deployment
**Usage**: Entry point for production web servers (Gunicorn, uWSGI)
**Required**: ✅ Yes - Needed for production deployment

#### `api/serializers.py`
**Purpose**: Would be used for Django REST Framework API serialization
**Status**: ❌ Empty, not used (no REST API in this project)
**Action**: 🗑️ Can be removed

---

### Main Application (`apps/main/`)

#### `main/__init__.py`
**Purpose**: Makes `main` a Python package
**Required**: ✅ Yes

#### `main/migrations/`
**Purpose**: Database migration files for the main app
**Status**: ⚠️ Empty directory (migrations are in `main/tracker/migrations/`)
**Action**: 🗑️ Can be removed (empty)

---

### Tracker App (`apps/main/tracker/`)

#### `main/tracker/__init__.py`
**Purpose**: Makes `tracker` a Python package
**Required**: ✅ Yes

#### `main/tracker/models.py`
**Purpose**: Database models - defines the `Entry` model (name, shape, color, created_at)
**Usage**: Defines the database structure
**Required**: ✅ Yes - Core data model

#### `main/tracker/forms.py`
**Purpose**: Django forms - defines `EntryForm` for creating/editing entries
**Usage**: Form validation and rendering in admin portal
**Required**: ✅ Yes - Handles form input

#### `main/tracker/views.py`
**Purpose**: View functions - handles HTTP requests and responses
**Contains**:
- `admin_portal()` - Admin dashboard
- `edit_entry()` - Edit entry functionality
- `delete_entry()` - Delete entry functionality
- `user_portal()` - User grid view
- `table_rows()` - API endpoint for real-time updates
**Required**: ✅ Yes - Core business logic

#### `main/tracker/urls.py`
**Purpose**: URL patterns for tracker app routes
**Defines**: All URL endpoints (/, /admin/, /api/rows/, etc.)
**Required**: ✅ Yes - URL routing

#### `main/tracker/migrations/`
**Purpose**: Database migration files for tracker app
**Contains**: `0001_initial.py` - Creates the Entry table
**Required**: ✅ Yes - Database schema changes

---

### Frontend Templates (`apps/main/frontend/`)

#### `frontend/base.html`
**Purpose**: Base template with navigation and common structure
**Usage**: Extended by all other templates
**Required**: ✅ Yes - Template inheritance

#### `frontend/user.html`
**Purpose**: User Portal template - displays grid/table view
**Usage**: Shows entries with colored shapes
**Required**: ✅ Yes - User-facing page

#### `frontend/admin.html`
**Purpose**: Admin Portal template - CRUD interface
**Usage**: Form to add entries, list of entries with edit/delete
**Required**: ✅ Yes - Admin interface

#### `frontend/_rows.html`
**Purpose**: Partial template for table rows (HTMX updates)
**Usage**: Returned by `table_rows()` view for real-time polling
**Required**: ✅ Yes - Real-time updates

#### `frontend/_entry_row.html`
**Purpose**: Partial template for single entry row in admin list
**Usage**: Used in admin portal entry list, also returned after edit
**Required**: ✅ Yes - Admin entry display

#### `frontend/_edit_form.html`
**Purpose**: Partial template for inline edit form
**Usage**: Replaces entry row when editing
**Required**: ✅ Yes - Edit functionality

---

### Static Files (`apps/main/static/`)

#### `static/style.css`
**Purpose**: CSS styles for the entire application
**Contains**: 
- Layout styles
- Form styles
- Table styles
- Shape rendering (triangles, squares, circles)
- Color styles
**Required**: ✅ Yes - Visual styling

---

## 📚 Documentation Files (Redundant - Can be consolidated)

### Root Level Documentation

#### `NEXT_STEPS.md`
**Purpose**: Guide for next steps after PostgreSQL connection
**Status**: 🗑️ Redundant - Info can be in README
**Action**: Consolidate into README.md

#### `CREATE_DATABASE.md`
**Purpose**: Instructions for creating PostgreSQL database
**Status**: 🗑️ Redundant - Duplicate info
**Action**: Consolidate into README.md

#### `SET_PG_PASSWORD.md`
**Purpose**: Guide for setting PostgreSQL password
**Status**: 🗑️ Redundant - Duplicate info
**Action**: Consolidate into README.md

#### `SQLTOOLS_TROUBLESHOOTING.md`
**Purpose**: Troubleshooting SQLTools connection issues
**Status**: 🗑️ Redundant - Can be in README
**Action**: Consolidate into README.md

#### `create_database.sql`
**Purpose**: SQL script to create database
**Status**: 🗑️ Redundant - Simple command, doesn't need separate file
**Action**: Remove (can be done via psql directly)

#### `test_postgres_connection.ps1`
**Purpose**: PowerShell script to test PostgreSQL connection
**Status**: 🗑️ Optional helper script
**Action**: Remove (not essential)

### Apps Level Documentation

#### `apps/POSTGRESQL_SETUP.md`
**Purpose**: Comprehensive PostgreSQL setup guide
**Status**: 🗑️ Redundant - Duplicate info
**Action**: Consolidate into README.md

#### `apps/RUN_MIGRATIONS.md`
**Purpose**: Guide for running migrations
**Status**: 🗑️ Redundant - Can be in README
**Action**: Consolidate into README.md

#### `apps/SETUP_COMPLETE.md`
**Purpose**: Setup completion guide
**Status**: 🗑️ Redundant - Duplicate info
**Action**: Consolidate into README.md

---

## 🗑️ Files to Remove (Redundant/Unused)

1. ❌ `apps/api/serializers.py` - Empty, not used
2. ❌ `apps/main/migrations/` - Empty directory
3. ❌ `NEXT_STEPS.md` - Consolidate into README
4. ❌ `CREATE_DATABASE.md` - Consolidate into README
5. ❌ `SET_PG_PASSWORD.md` - Consolidate into README
6. ❌ `SQLTOOLS_TROUBLESHOOTING.md` - Consolidate into README
7. ❌ `create_database.sql` - Not needed
8. ❌ `test_postgres_connection.ps1` - Optional helper, not essential
9. ❌ `apps/POSTGRESQL_SETUP.md` - Consolidate into README
10. ❌ `apps/RUN_MIGRATIONS.md` - Consolidate into README
11. ❌ `apps/SETUP_COMPLETE.md` - Consolidate into README

---

## ⚠️ Files to Fix

1. ⚠️ `apps/Procfile` - Change `core.wsgi` to `api.wsgi`

---

## 📝 Recommended: Create README.md

Consolidate all documentation into a single comprehensive README.md with:
- Project description
- Setup instructions
- Database configuration
- Running the application
- Troubleshooting


