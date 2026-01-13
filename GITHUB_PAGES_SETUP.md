# GitHub Pages Setup Instructions

Your Django portfolio has been converted to a static site for GitHub Pages!

## What Changed

1. **All Django templates converted to static HTML files** in the root directory:
   - `index.html` - Home page
   - `projects.html` - Projects page
   - `experience.html` - Experience timeline
   - `resume.html` - Resume/About page
   - `404.html` - 404 error page

2. **Static files remain in the `static/` folder** - CSS, JS, and images

3. **Backend functionality removed**:
   - Database models (Projects, Resume, etc.)
   - Django views and URLs
   - Admin panel
   - Contact form page and functionality

## Setup Steps

### 1. Enable GitHub Pages

1. Push this repository to GitHub
2. Go to your repository settings on GitHub
3. Navigate to "Pages" in the left sidebar
4. Under "Source", select the branch you want to deploy (usually `main` or `master`)
5. Select the root directory (`/ (root)`)
6. Click "Save"
7. Your site will be available at `https://YOUR_USERNAME.github.io/YOUR_REPO_NAME/`

### 2. (Optional) Custom Domain

If you want to use a custom domain:
1. Add a `CNAME` file in the root with your domain name
2. Configure DNS settings according to GitHub Pages documentation

## Important Notes

- All paths are relative (e.g., `static/css/home.css`), which works for GitHub Pages
- If you want to add a resume PDF download, place it in `static/files/` and uncomment the download button in `resume.html`
- Dark mode theme toggle uses localStorage, so it persists across pages
- All Django backend files can be removed if you no longer need them

## Files You Can Remove (Optional)

Since this is now a static site, you can remove:
- All Django app folders (`pages/`, `projects/`, `experience/`, `resume/`, `sendemail/`, `NotImplemented/`)
- `Portfolio/` Django settings folder
- `manage.py`
- `Procfile`
- `runtime.txt`
- `requirements.txt`
- `db.sqlite3`
- `staticfiles/` (Django collected static files)
- `.env` files

## Testing Locally

To test the site locally before pushing:
1. Use a simple HTTP server:
   ```bash
   # Python 3
   python -m http.server 8000
   
   # Python 2
   python -m SimpleHTTPServer 8000
   
   # Or use Node.js http-server
   npx http-server
   ```
2. Open `http://localhost:8000` in your browser
