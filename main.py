from db.db_conn import connection
from db.tables import *
from Models.appointment import *
from Models.appointment_generator import *
from Models.doctor import *
from Models.patients import *

conn = connection()
cursor = conn.cursor()

doctor_table()
patients_table()
appointments_table()

def menu():
    while True:
        print("\n========= HOSPITAL MANAGEMENT SYSTEM =========")
        print("1. Add Doctor")
        print("2. Show Doctors")
        print("3. Update Doctors")
        print("4. Remove Doctor")
        print("5. Add Patient")
        print("6. View Patient")
        print("7. Update Patient")
        print("8. Delete Patient")
        print("9. Book Appointment")
        print("10. View Appointment")
        print("11. Delete Appointment")
        print("12. Exit")
        
        choice = input("Enter your choice (1 - 12): ")

        if choice == "1":
            add_doctor()
        elif choice == "2":
            view_doctors()
        elif choice == "3":
            update_doctors()
        elif choice == "4":
            delete_doctor()
        elif choice == "5":
            add_patient()
        elif choice == "6":
            view_patients()
        elif choice == "7":
            update_patient()
        elif choice == "8":
            delete_patient()
        elif choice == "9":
            book_appointment()
        elif choice == "10":
            view_appointments()
        elif choice == "11":
            cancel_appointments()
        elif choice == "12":
            print("Exitting....")
            break
        else:
            print("Invalid Choice!")

menu()