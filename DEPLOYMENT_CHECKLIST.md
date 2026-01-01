# Quick Deployment Checklist

## ✅ Pre-Deployment

- [ ] Code pushed to GitHub
- [ ] `.gitignore` includes sensitive files (`.env`, `__pycache__/`, etc.)
- [ ] `DEBUG=False` in production environment variables
- [ ] Strong `SECRET_KEY` generated and set
- [ ] `ALLOWED_HOSTS` configured with your domain
- [ ] Database connection details ready
- [ ] `requirements.txt` up to date (includes python-dotenv if using .env)
- [ ] `Procfile` correct: `web: gunicorn api.wsgi --log-file -`

## 🚀 App Platform Deployment (Recommended)

- [ ] DigitalOcean account created
- [ ] GitHub repository connected
- [ ] App created in App Platform
- [ ] Environment variables set (SECRET_KEY, DEBUG, ALLOWED_HOSTS, DB_*)
- [ ] PostgreSQL database created and linked
- [ ] Build command: `python manage.py collectstatic --noinput`
- [ ] Migrations run (one-time task or console)
- [ ] App deployed and accessible

## 🖥️ Droplet Deployment (Advanced)

- [ ] Droplet created (Ubuntu 22.04)
- [ ] SSH access configured
- [ ] System packages installed (Python, Nginx, Git)
- [ ] Application user created
- [ ] Code cloned from GitHub
- [ ] Virtual environment created and activated
- [ ] Dependencies installed
- [ ] Environment variables configured (.env file)
- [ ] Migrations run
- [ ] Static files collected
- [ ] Gunicorn service configured and running
- [ ] Nginx configured and running
- [ ] SSL certificate installed (Let's Encrypt)
- [ ] Firewall configured

## 🔒 Security

- [ ] DEBUG=False in production
- [ ] Strong SECRET_KEY set
- [ ] ALLOWED_HOSTS configured
- [ ] HTTPS enabled (automatic in App Platform)
- [ ] Database uses SSL connection
- [ ] No passwords in code (use environment variables)
- [ ] Firewall rules configured (Droplet)

## 🧪 Post-Deployment Testing

- [ ] Application loads at URL
- [ ] Admin portal accessible
- [ ] User portal displays entries
- [ ] Add entry works
- [ ] Edit entry works
- [ ] Delete entry works
- [ ] Real-time updates working
- [ ] Static files loading (CSS, images)
- [ ] Database connection working

## 📊 Monitoring

- [ ] Logs accessible and reviewed
- [ ] Error tracking set up (optional)
- [ ] Database backups enabled
- [ ] Application backups (GitHub)

---

**Quick Start**: Use App Platform - it's the easiest option! See `DIGITALOCEAN_DEPLOYMENT.md` for detailed steps.

