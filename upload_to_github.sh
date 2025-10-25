#!/bin/bash

# GitHub Upload Script for Happy Birthday Cake Project
# Built by AyaNexus 🦢

echo "Happy Birthday Cake - GitHub Upload Script"
echo "=============================================="
echo ""

# Check if git is installed
if ! command -v git &> /dev/null; then
    echo "Git is not installed. Please install Git first."
    exit 1
fi

echo "Step 1: Initializing Git repository..."
git init

echo ""
echo "Step 2: Adding all files to Git..."
git add .

echo ""
echo "💾 Step 3: Creating initial commit..."
git commit -m "Initial commit: Professional birthday cake animation project

Features:
- Beautiful pink/purple themed birthday cake animation
- Multi-layered cake with candles, hearts, and stars
- Personalized birthday message
- Cross-platform Python Turtle Graphics implementation

Project Structure:
- Organized source code in src/ folder
- Media assets in assets/ folder (includes demo video)
- Comprehensive documentation in docs/ folder
- Example variations in examples/ folder

Documentation:
- Comprehensive README with video demo
- MIT License
- Contributing guidelines
- Setup guide for Git and GitHub
- Changelog and requirements

Built by AyaNexus 🦢"

echo ""
echo "Step 4: Adding remote repository..."
git branch -M main
git remote add origin https://github.com/1AyaNabil1/Happy_Birth_Day_Cake.git

echo ""
echo "Step 5: Pushing to GitHub..."
git push -u origin main

echo ""
echo "Done! Your project has been uploaded to GitHub!"
echo "Visit: https://github.com/1AyaNabil1/Happy_Birth_Day_Cake"
echo ""
echo "Built by AyaNexus 🦢"
