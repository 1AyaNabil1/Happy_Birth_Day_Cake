# Quick Setup Guide

## First Time Upload to GitHub

Follow these steps to upload your project to GitHub:

### Option 1: Using the Upload Script (Recommended)

1. Make the script executable:
```bash
chmod +x upload_to_github.sh
```

2. Run the script:
```bash
./upload_to_github.sh
```

### Option 2: Manual Upload

1. Initialize Git repository:
```bash
git init
```

2. Add all files:
```bash
git add .
```

3. Create your first commit:
```bash
git commit -m "Initial commit: Birthday cake animation - Built by AyaNexus 🦢"
```

4. Add the remote repository:
```bash
git branch -M main
git remote add origin https://github.com/1AyaNabil1/Happy_Birth_Day_Cake.git
```

5. Push to GitHub:
```bash
git push -u origin main
```

## Making Updates Later

After the initial upload, when you make changes:

```bash
# Add your changes
git add .

# Commit with a descriptive message
git commit -m "Your change description"

# Push to GitHub
git push
```

## Useful Git Commands

- Check status: `git status`
- View commit history: `git log`
- View remote URL: `git remote -v`
- Create a new branch: `git checkout -b feature-name`
- Switch branches: `git checkout branch-name`

## Troubleshooting

### If you get authentication errors:
Make sure you have set up your GitHub credentials or use a Personal Access Token.

### If the remote already exists:
```bash
git remote remove origin
git remote add origin https://github.com/1AyaNabil1/Happy_Birth_Day_Cake.git
```

### If you need to force push (use carefully):
```bash
git push -f origin main
```

---
<div align="center">
  <em>Built by AyaNexus 🦢</em>
</div>
