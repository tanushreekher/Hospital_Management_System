from db.db_conn import connection
conn = connection()
cursor = conn.cursor()

def doctor_table():
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Doctors(
    Doctor_id INT PRIMARY KEY,
    Doctor_name VARCHAR(100),
    Specialization VARCHAR(100),
    Phone VARCHAR(15)
    )
    """)
    conn.commit()

def patients_table():
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Patients(
    Patient_id INT PRIMARY KEY,
    Patient_name VARCHAR(100),
    Age INT,
    Gender VARCHAR(10),
    Phone INT,
    Address VARCHAR(100)
    )
    """)
    conn.commit()

def appointments_table():
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Appointment(
    Appointment_id INT AUTO_INCREMENT PRIMARY KEY,
    Patient_id INT,
    Doctor_id INT,     
    Appointment_date DATE,
    Time TIME,
    FOREIGN KEY(Patient_id) REFERENCES Patients(Patient_id),
    FOREIGN KEY(Doctor_id) REFERENCES Doctors(Doctor_id)
    )
    """)
    conn.commit()