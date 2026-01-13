# How to Push to GitHub and Enable GitHub Pages

## Step 1: Add all new files

```powershell
git add .
```

This will add all the new static HTML files and other files to git.

## Step 2: Commit the changes

```powershell
git commit -m "Convert to static GitHub Pages site"
```

## Step 3: Push to GitHub

```powershell
git push origin main
```

(If your default branch is `master` instead of `main`, use `git push origin master`)

## Step 4: Enable GitHub Pages

1. Go to your GitHub repository in a web browser
2. Click on **Settings** (top menu of the repository)
3. Click on **Pages** in the left sidebar
4. Under **Source**, select:
   - Branch: `main` (or `master` if that's your default branch)
   - Folder: `/ (root)`
5. Click **Save**
6. Wait a few minutes for GitHub to deploy your site
7. Your site will be available at: `https://YOUR_USERNAME.github.io/YOUR_REPO_NAME/`

## Optional: Clean up Django files before pushing

If you want to remove Django-related files before pushing (they're no longer needed), you can:

1. Delete the Django app folders: `pages/`, `projects/`, `experience/`, `resume/`, `sendemail/`, `NotImplemented/`, `Portfolio/`
2. Delete `staticfiles/` folder
3. Delete `templates/` folder (the old Django templates)
4. Delete `manage.py`, `Procfile`, `runtime.txt`, `requirements.txt`, `db.sqlite3`

Then add and commit again:
```powershell
git add .
git commit -m "Remove Django files - now static site"
git push origin main
```

## Note

- If you see changes to existing files, that's normal - they were updated when converting to static HTML
- The `.nojekyll` file tells GitHub Pages not to process the site with Jekyll (which is good for static HTML)
