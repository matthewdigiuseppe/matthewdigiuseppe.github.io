#!/bin/bash

# Change to the repository directory
cd /Users/digiuseppe/codingprojects/AcademicWebsite

# Check status
echo "Checking git status..."
git status

# Add changes
echo "Adding changes..."
git add index.html styles.css

# Commit changes
echo "Committing changes..."
git commit -m "Reorganize research section: move working papers to top and highlight AI research"

# Push changes
echo "Pushing changes to GitHub..."
git push origin main

echo "Git push completed successfully!"
