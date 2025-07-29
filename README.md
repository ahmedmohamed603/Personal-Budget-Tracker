# Personal-Budget-Tracker

A simple command-line based Personal Budget Tracker written in Python.
This project allows users to manage their income and expenses by category, view summaries, search specific records, and save their data securely in user-specific JSON files.

Features
User Authentication Admin and User roles

Add,Edit,Delete income and expense categories

View summary of total income, expenses, and balance

Search by category

Reset all data (for admin only)

Change password "in the code for demo only" (for both users and admin)

Each user has a private file for their own data

Admin can view all users' data files

Data persistence via JSON

Roles
Admin can:

View, edit, reset all data

Access other users' data

Use all functionalities

User can:

Manage their own data only

Cannot view or modify others' files

Data Storage
Each user has a separate file named:
<username>_data.json

Passwords are stored in-memory in a Python dictionary (for demo purposes only)

How to Use
Run the code:

python budget_tracker.py

Log in using:

Admin: Ahmed / 3266
User: user / 0000

Follow the menu to manage your budget.

📌 Notes
This is a beginner-friendly project designed for practice and learning.
Feel free to fork it, test it, and improve it 

