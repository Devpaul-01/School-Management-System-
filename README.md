🏫 School Management System

A Python-based console application that simulates a school environment with role-based access for students, teachers, and admin. The system allows secure login, profile management, grading, attendance tracking, and more — all stored using JSON files for persistence.

🚀 Features

👨‍🎓 Students
- Register with name, age, level, and secure 4-digit PIN.
- Secure login system with 3-attempt lockout.
- View and edit profile (name, age, PIN).
- Add and view personal grades.
- Edit grades in bulk.
- See history log of profile updates and actions.

 👩‍🏫 Teachers
- Register with name, age, subject, and salary.
- Login using secure PIN.
- Update teacher salary.
- Record student attendance with date and status.
- View history of changes and actions.

🔐 Admin
- Access student records using admin credentials.
- View full details stored in JSON format.

📁 Project Structure

```bash
School-Management-System/
│
├── main.py              # Application entry point
├── user.py              # All class definitions and logic
│
├── Students folder/     # Contains student JSON files
└── Teachers folder/     # Contains teacher JSON files
