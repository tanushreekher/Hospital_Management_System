from db.db_conn import connection

conn = connection()
cursor = conn.cursor()

def add_patient():
    id = input("Enter Patient ID: ")
    name = input("Enter Patient Name: ")
    age = input("Enter Patient's Age: ")
    gender = input("Enter Patient's Gender: ")
    phone = input("Enter Mobile Number of Patient: ")
    address = input("Enter Address of Patient: ")

    cursor.execute(
        "INSERT INTO Patients (Patient_id, Patient_name, Age, Gender, Phone, Address) VALUES (%s, %s, %s, %s, %s, %s)",
        (id, name, age, gender, phone, address)
    )
    conn.commit()
    print("Patient registered successfully!")


def view_patients():
    cursor.execute("SELECT * FROM Patients")
    rows = cursor.fetchall()
    if not rows:
        print("\nNo patients found.")
        return

    print("\n-------------------- PATIENT LIST --------------------")
    for row in rows:
        print(row)


def update_patient():
    p_id = input("Enter the Patient ID you want to update: ")
    cursor.execute("SELECT * FROM Patients WHERE Patient_id = %s", (p_id,))
    patient = cursor.fetchone()

    if not patient:
        print("Patient not found!")
        return

    print(f"\nCurrent Details:\n Name: {patient[1]}\n Age: {patient[2]}\n Gender: {patient[3]}\n Phone: {patient[4]}\n Address: {patient[5]}")
    print("\nWhich fields do you want to update?")
    print("Options: name, age, gender, phone, address")
    choices = input("Enter your choices separated by commas: ").lower().replace(" ", "").split(",")

    update_fields = []
    update_values = []

    if "name" in choices:
        new_name = input("Enter the updated name of the patient: ")
        update_fields.append("Patient_name = %s")
        update_values.append(new_name)

    if "age" in choices:
        new_age = input("Enter the updated age of the patient: ")
        update_fields.append("Age = %s")
        update_values.append(new_age)

    if "gender" in choices:
        new_gender = input("Enter the updated gender of the patient: ")
        update_fields.append("Gender = %s")
        update_values.append(new_gender)

    if "phone" in choices:
        new_phone = input("Enter the updated phone number of the patient: ")
        update_fields.append("Phone = %s")
        update_values.append(new_phone)

    if "address" in choices:
        new_address = input("Enter the updated address of the patient: ")
        update_fields.append("Address = %s")
        update_values.append(new_address)

    if not update_fields:
        print("Please select a valid field to update.")
        return

    sql = f"UPDATE Patients SET {', '.join(update_fields)} WHERE Patient_id = %s"
    update_values.append(p_id)
    cursor.execute(sql, tuple(update_values))
    conn.commit()

    print("Patient details updated successfully!")


def delete_patient():
    p_id = input("Enter the Patient ID you want to delete: ")
    cursor.execute("DELETE FROM Patients WHERE Patient_id = %s", (p_id,))
    conn.commit()
    print("Patient removed successfully!")
