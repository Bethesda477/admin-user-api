# DigitalOcean Deployment Guide

This guide covers deploying your Django application to DigitalOcean using **App Platform** (recommended) or **Droplets** (more control).

---

## 🚀 Option 1: DigitalOcean App Platform (Recommended - Easiest)

**App Platform** is DigitalOcean's Platform-as-a-Service (PaaS) - similar to Heroku but simpler.

### Advantages:

- ✅ Automatic deployments from GitHub
- ✅ Managed PostgreSQL database
- ✅ Automatic SSL certificates
- ✅ Auto-scaling
- ✅ No server management needed
- ✅ Built-in CI/CD

### Prerequisites:

1. DigitalOcean account (sign up at https://www.digitalocean.com)
2. GitHub repository with your code
3. Credit card for payment (Pay-as-you-go, ~$5-12/month for basic setup)

### Step-by-Step Deployment:

#### Step 1: Prepare Your Repository

1. **Push your code to GitHub** (if not already):

   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   git remote add origin https://github.com/yourusername/admin-user-api.git
   git push -u origin main
   ```

2. **Create a `.gitignore` file** (if not exists):

   ```gitignore
   # Python
   __pycache__/
   *.py[cod]
   *$py.class
   *.so
   .Python
   venv/
   env/
   ENV/

   # Django
   *.log
   local_settings.py
   db.sqlite3
   db.sqlite3-journal

   # Static files
   staticfiles/

   # Environment
   .env

   # IDE
   .vscode/
   .idea/
   *.swp
   *.swo
   ```

3. **Update `Procfile`** (should already be correct):
   ```
   web: gunicorn api.wsgi --log-file -
   ```

#### Step 2: Create App in DigitalOcean

1. **Log in to DigitalOcean**: https://cloud.digitalocean.com
2. **Click "Create" → "Apps"**
3. **Connect GitHub repository**:
   - Authorize DigitalOcean to access GitHub
   - Select your repository
   - Select branch (usually `main` or `master`)

#### Step 3: Configure Your App

1. **App Settings**:

   - **Type**: Web Service
   - **Name**: `admin-user-api` (or your choice)
   - **Region**: Choose closest to your users
   - **Run Command**: `gunicorn api.wsgi --log-file -`
   - **HTTP Port**: `8080` (default)
   - **HTTP Request Routes**: `/`

2. **Environment Variables** (Click "Edit" next to Environment Variables):

   ```
   DJANGO_SETTINGS_MODULE=api.config
   DEBUG=False
   SECRET_KEY=your-super-secret-key-here-generate-random
   ALLOWED_HOSTS=your-app-name.ondigitalocean.app,www.yourdomain.com

   # Database (we'll add these after creating database)
   DB_NAME=your_db_name
   DB_USER=your_db_user
   DB_PASSWORD=your_db_password
   DB_HOST=your_db_host
   DB_PORT=25060
   ```

   **Generate SECRET_KEY**:

   ```bash
   python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
   ```

3. **Build Settings**:
   - **Build Command**: Leave empty (Django doesn't need build)
   - **Run Command**: `gunicorn api.wsgi --log-file -`

#### Step 4: Add PostgreSQL Database

1. **In App Platform**, click **"Add Resource"** → **"Database"**
2. **Choose PostgreSQL**:

   - **Version**: Latest (14 or 15)
   - **Plan**: Basic ($15/month) or Professional (for production)
   - **Database Name**: Auto-generated or custom
   - **Region**: Same as your app

3. **After creation**, note the connection details:

   - Host
   - Port (usually 25060)
   - Database name
   - Username
   - Password

4. **Update Environment Variables** in your app:

   ```
   DB_NAME=defaultdb
   DB_USER=doadmin
   DB_PASSWORD=the-password-from-digitalocean
   DB_HOST=your-db-host.db.ondigitalocean.com
   DB_PORT=25060
   ```

   **Important**: DigitalOcean provides these in the database dashboard under "Connection Details".

#### Step 5: Configure Static Files

1. **Add build command** (in App Settings → Build):

   ```
   python manage.py collectstatic --noinput
   ```

2. **WhiteNoise is already configured** in your `config.py`, so static files will be served automatically.

#### Step 6: Run Migrations

1. **Add a one-time task** (in App Platform):

   - Go to "Components" → "Add Component" → "Worker"
   - **Run Command**: `python manage.py migrate`
   - **Type**: One-time task
   - Run this once to set up database tables

   Or use **DigitalOcean Console**:

   - Go to your app → "Console" tab
   - Run: `python manage.py migrate`

#### Step 7: Deploy

1. **Click "Next"** through the review
2. **Select plan**: Basic ($5/month) or Professional
3. **Click "Launch App"**
4. **Wait for deployment** (~5-10 minutes)

#### Step 8: Access Your App

- Your app will be available at: `https://your-app-name.ondigitalocean.app`
- Test: Visit the URL in your browser

---

## 🖥️ Option 2: DigitalOcean Droplet (More Control)

If you want a virtual server with full control (like VPS), use a Droplet.

### Advantages:

- ✅ Full server control
- ✅ More cost-effective for multiple apps
- ✅ Custom configurations
- ✅ Learning experience

### Disadvantages:

- ❌ Server management required
- ❌ Manual SSL setup
- ❌ Manual updates

### Step-by-Step Deployment:

#### Step 1: Create Droplet

1. **DigitalOcean Dashboard** → "Create" → "Droplets"
2. **Choose**:
   - **Image**: Ubuntu 22.04 LTS
   - **Plan**: Basic ($6/month) or higher
   - **Region**: Closest to users
   - **Authentication**: SSH keys (recommended) or password
   - **Hostname**: `admin-user-api`

#### Step 2: Create Managed PostgreSQL Database

1. **DigitalOcean Dashboard** → "Create" → "Database"
2. **Choose PostgreSQL** (same as App Platform steps above)
3. **Note connection details**

#### Step 3: Connect to Droplet

```bash
ssh root@your-droplet-ip
```

#### Step 4: Install Dependencies

```bash
# Update system
apt update && apt upgrade -y

# Install Python and pip
apt install python3 python3-pip python3-venv nginx git -y

# Install PostgreSQL client (optional, for testing)
apt install postgresql-client -y
```

#### Step 5: Set Up Application User

```bash
# Create non-root user
adduser django
usermod -aG sudo django
su - django
```

#### Step 6: Clone Repository

```bash
# Clone your repo
git clone https://github.com/yourusername/admin-user-api.git
cd admin-user-api/apps

# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

#### Step 7: Configure Environment Variables

```bash
# Create .env file
nano .env
```

Add:

```
DEBUG=False
SECRET_KEY=your-generated-secret-key
ALLOWED_HOSTS=your-droplet-ip,your-domain.com
DB_NAME=defaultdb
DB_USER=doadmin
DB_PASSWORD=your-db-password
DB_HOST=your-db-host.db.ondigitalocean.com
DB_PORT=25060
```

#### Step 8: Update Django Settings

Update `apps/api/config.py` to read from `.env`:

```python
import os
from pathlib import Path
from dotenv import load_dotenv  # Add this

load_dotenv()  # Add this

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.environ.get('SECRET_KEY')
DEBUG = os.environ.get('DEBUG', 'False') == 'True'
ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS', '').split(',')

# ... rest of settings
```

Install python-dotenv:

```bash
pip install python-dotenv
# Add to requirements.txt
```

#### Step 9: Run Migrations

```bash
source venv/bin/activate
python manage.py migrate
python manage.py collectstatic --noinput
```

#### Step 10: Test Application

```bash
# Test run (temporary)
python manage.py runserver 0.0.0.0:8000
```

Visit `http://your-droplet-ip:8000` - should work!

#### Step 11: Set Up Gunicorn

```bash
# Test Gunicorn
gunicorn api.wsgi --bind 0.0.0.0:8000
```

Create systemd service:

```bash
sudo nano /etc/systemd/system/gunicorn.service
```

Add:

```ini
[Unit]
Description=gunicorn daemon
After=network.target

[Service]
User=django
Group=www-data
WorkingDirectory=/home/django/admin-user-api/apps
Environment="PATH=/home/django/admin-user-api/apps/venv/bin"
ExecStart=/home/django/admin-user-api/apps/venv/bin/gunicorn \
    --workers 3 \
    --bind unix:/home/django/admin-user-api/apps/gunicorn.sock \
    api.wsgi

[Install]
WantedBy=multi-user.target
```

Start service:

```bash
sudo systemctl start gunicorn
sudo systemctl enable gunicorn
sudo systemctl status gunicorn
```

#### Step 12: Configure Nginx

```bash
sudo nano /etc/nginx/sites-available/admin-user-api
```

Add:

```nginx
server {
    listen 80;
    server_name your-domain.com your-droplet-ip;

    location /static/ {
        alias /home/django/admin-user-api/apps/staticfiles/;
    }

    location / {
        include proxy_params;
        proxy_pass http://unix:/home/django/admin-user-api/apps/gunicorn.sock;
    }
}
```

Enable site:

```bash
sudo ln -s /etc/nginx/sites-available/admin-user-api /etc/nginx/sites-enabled/
sudo nginx -t
sudo systemctl restart nginx
```

#### Step 13: Set Up SSL with Let's Encrypt

```bash
sudo apt install certbot python3-certbot-nginx -y
sudo certbot --nginx -d your-domain.com
```

Follow prompts - SSL will be configured automatically!

#### Step 14: Set Up Firewall

```bash
sudo ufw allow 'Nginx Full'
sudo ufw allow OpenSSH
sudo ufw enable
```

---

## 🔒 Security Checklist for Production

### Both Options:

- [ ] Set `DEBUG=False` in production
- [ ] Use strong `SECRET_KEY` (generate random)
- [ ] Set proper `ALLOWED_HOSTS`
- [ ] Use HTTPS (automatic in App Platform, Let's Encrypt in Droplet)
- [ ] Database uses SSL connection (DigitalOcean managed DB does this)
- [ ] Environment variables for sensitive data (no hardcoded passwords)
- [ ] Regular updates: `apt update && apt upgrade` (Droplet only)

### App Platform (Automatic):

- ✅ SSL certificates
- ✅ Security updates
- ✅ Firewall rules

### Droplet (Manual):

- [ ] Firewall configured (UFW)
- [ ] SSH key authentication only
- [ ] Fail2ban installed (optional)
- [ ] Regular security updates

---

## 📝 Post-Deployment Steps

### 1. Test Your Application

Visit your app URL and test:

- ✅ Admin Portal: Add/edit/delete entries
- ✅ User Portal: View entries with shapes
- ✅ Real-time updates working
- ✅ Static files loading (CSS, images)

### 2. Monitor Logs

**App Platform**:

- Go to "Runtime Logs" tab

**Droplet**:

```bash
# Gunicorn logs
sudo journalctl -u gunicorn -f

# Nginx logs
sudo tail -f /var/log/nginx/error.log
sudo tail -f /var/log/nginx/access.log
```

### 3. Set Up Backups

**App Platform**:

- Database backups are automatic
- App backups: Use GitHub (your code repository)

**Droplet**:

- DigitalOcean Droplet snapshots
- Database backups via DigitalOcean managed DB

### 4. Custom Domain (Optional)

1. **Add domain in DigitalOcean**:

   - Networking → Domains → Add Domain
   - Add A record pointing to your app/droplet IP

2. **Update ALLOWED_HOSTS**:

   ```
   ALLOWED_HOSTS=your-domain.com,www.your-domain.com
   ```

3. **App Platform**: Add domain in app settings
4. **Droplet**: Already configured in Nginx (step 12)

---

## 💰 Cost Estimate

### App Platform Option:

- **App**: $5/month (Basic) or $12/month (Professional)
- **Database**: $15/month (Basic) or higher
- **Total**: ~$20-30/month

### Droplet Option:

- **Droplet**: $6/month (Basic)
- **Database**: $15/month (Basic)
- **Total**: ~$21/month

**Note**: Prices may vary. Check DigitalOcean pricing page for current rates.

---

## 🔧 Troubleshooting

### Database Connection Errors

1. **Check environment variables** are set correctly
2. **Verify database firewall** allows your app/droplet IP
3. **Test connection**:
   ```bash
   psql -h your-db-host -U your-user -d your-db
   ```

### Static Files Not Loading

1. **Run collectstatic**:

   ```bash
   python manage.py collectstatic --noinput
   ```

2. **Check STATIC_ROOT** path in settings
3. **Verify WhiteNoise middleware** is enabled

### 500 Internal Server Error

1. **Check logs** (see monitoring section)
2. **Verify DEBUG=False** in production
3. **Check ALLOWED_HOSTS** includes your domain
4. **Verify database connection** works

### Migration Errors

1. **Run migrations** manually:

   ```bash
   python manage.py migrate
   ```

2. **Check database connection** first

---

## 📚 Additional Resources

- DigitalOcean App Platform Docs: https://docs.digitalocean.com/products/app-platform/
- Django Deployment Checklist: https://docs.djangoproject.com/en/stable/howto/deployment/checklist/
- Gunicorn Documentation: https://gunicorn.org/

---

**Recommended**: Start with **App Platform** (Option 1) - it's easier and handles most configuration automatically! 🚀
