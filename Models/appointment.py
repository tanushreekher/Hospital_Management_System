from db.db_conn import connection
from datetime import datetime
from Models.appointment_generator import generate_appointment, cancel_appointment
# Establish connection
conn = connection()
cursor = conn.cursor()

def book_appointment():
    # Fetch doctors
    cursor.execute("SELECT Doctor_id, Doctor_name, Specialization FROM Doctors")
    doctors = cursor.fetchall()
    if not doctors:
        print("No doctors found. Please add doctors first.")
        return

    print("\n--- Doctors List ---")
    for doc in doctors:
        print(f"Doctor ID: {doc[0]}, Name: {doc[1]}, Specialization: {doc[2]}")

    doctor_id = input("\nEnter Doctor ID to book appointment with: ")

    # Fetch patients
    cursor.execute("SELECT Patient_id, Patient_name FROM Patients")
    patients = cursor.fetchall()
    if not patients:
        print("No patients found. Please add patients first.")
        return

    print("\n--- Patients List ---")
    for pat in patients:
        print(f"Patient ID: {pat[0]}, Name: {pat[1]}")

    patient_id = input("\nEnter Patient ID: ")

    # Get doctor and patient names for text file
    cursor.execute("SELECT Doctor_name FROM Doctors WHERE Doctor_id = %s", (doctor_id,))
    doctor_name = cursor.fetchone()
    cursor.execute("SELECT Patient_name FROM Patients WHERE Patient_id = %s", (patient_id,))
    patient_name = cursor.fetchone()

    if not doctor_name or not patient_name:
        print("Invalid doctor or patient ID.")
        return

    doctor_name = doctor_name[0]
    patient_name = patient_name[0]

    # Input date & time
    date_input = input("Enter appointment date (YYYY-MM-DD): ")
    time_input = input("Enter appointment time (HH:MM, 24-hour format): ")

    try:
        datetime.strptime(date_input, "%Y-%m-%d")
        datetime.strptime(time_input, "%H:%M")
    except ValueError:
        print("Invalid date or time format.")
        return

    # Insert appointment
    cursor.execute("""
        INSERT INTO Appointment (Doctor_id, Patient_id, Appointment_date, Time)
        VALUES (%s, %s, %s, %s)
    """, (doctor_id, patient_id, date_input, time_input))
    conn.commit()

    appointment_id = cursor.lastrowid
    print(f"\nAppointment booked successfully! Appointment ID: {appointment_id}")

    # Generate appointment text file
    generate_appointment(appointment_id, patient_id, patient_name, doctor_id, doctor_name, date_input)


def view_appointments():
    cursor.execute("SELECT * FROM Appointments")
    rows = cursor.fetchall()
    if not rows:
        print("\nNo appointments found.")
        return

    print("\n-------------------- APPOINTMENT LIST --------------------")
    for row in rows:
        print(row)


def cancel_appointments():
    app_id = input("Enter the appointment ID to cancel: ")

    # Fetch appointment details to remove text file too
    cursor.execute("""
        SELECT a.Patient_id, p.Patient_name 
        FROM Appointments a 
        JOIN Patients p ON a.Patient_id = p.Patient_id 
        WHERE a.Appointment_id = %s
    """, (app_id,))
    result = cursor.fetchone()

    if not result:
        print("No such appointment found.")
        return

    patient_id, patient_name = result

    cursor.execute("DELETE FROM Appointments WHERE Appointment_id = %s", (app_id,))
    conn.commit()
    print("Appointment cancelled successfully!")

    # Delete the text file
    cancel_appointment(patient_id, patient_name)
