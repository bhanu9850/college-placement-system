# college-placement-system

College Placement System
Overview
The College Placement System is a web-based application built using Django, designed to streamline the placement process within a college. This system consists of two main apps: student and college_management, each serving distinct roles and functionalities. The student app focuses on student-related operations, while the college_management app caters to administrative tasks and facilitates communication between students and the college management.

Features
Student App
User Authentication: Secure login and registration system for students.
Profile Management: Enter and manage personal and academic details.
Job Applications: View and apply for job openings displayed on the student dashboard.

College Management App
User Authentication: Secure login for college administrators.
Student Management: Add, delete, and monitor student profiles.
Job Management: Post, monitor, and manage job openings.
Application Monitoring: Track and review job applications submitted by students.

Requirements
Python (version 3.8)
Django (version 3.0.7)
vs code

Installation
Clone the repository:
git clone https://github.com/your-username/college-placement-system.git

Navigate to the project directory:
cd college-placement-system

Install the required packages:
pip install -r requirements.txt

Run migrations:
python manage.py migrate

Start the development server:
python manage.py runserver

Usage
Access the application via the browser at http://localhost:8000/.
Students can register/login, enter their details, and apply for jobs through the student app.
College administrators can log in, manage student profiles, post job openings, and monitor applications using the college_placement app.

Acknowledgements
Django Documentation
Python Documentation
