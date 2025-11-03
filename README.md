Hospital Management System

A Python + MySQL based command-line project that efficiently manages hospital operations such as doctor management, patient registration, and appointment booking.
This project also integrates file handling, where every new appointment automatically generates a text file with the appointment details.

Project Overview

The Hospital Management System is designed to simplify administrative tasks in a hospital environment.
It provides functionalities for managing doctors, patients, and appointments — all via a menu-driven interface.

Each booked appointment is recorded in the database and saved locally as a .txt file named in the format:

patientID_patientName.txt


This makes it easy to retrieve patient appointment details offline as well.

Tech Stack

Language: Python

Database: MySQL

Libraries Used: mysql.connector

Concepts Applied:

CRUD Operations

File Handling

Exception Handling

Modular Programming

🔹 Features
👨‍⚕️ Doctor Management

Add new doctors

Update doctor details

View all doctors

Delete doctor records

👩‍💻 Patient Management

Register new patients

View all registered patients

📅 Appointment Management

Book new appointments

View all appointments

Cancel appointments

Automatically generate appointment text files

🧩 Database Design

Tables Used:

doctors

doctor_id (INT, PK)

doctor_name (VARCHAR)

specialization (VARCHAR)

phone (VARCHAR)

patients

patient_id (INT, PK)

patient_name (VARCHAR)

age (INT)

gender (VARCHAR)

phone (VARCHAR)

appointments

appointment_id (INT, PK, AUTO_INCREMENT)

patient_id (INT, FK)

doctor_id (INT, FK)

appointment_date (DATE)

How It Works

Run the main Python file.

Choose an option from the menu (Add/View Doctors, Register Patients, etc.).

When you book an appointment:

Data is saved in the appointments table.

A .txt file is automatically generated with appointment details.

Future Enhancements

Add login system for admin/staff

Add appointment reminders via email

Create a GUI using Tkinter or Flask

Author

Tanushree Kher
Python | Backend | AI Developer in Progress
 #30DayPythonChallenge | #LearningByBuilding
