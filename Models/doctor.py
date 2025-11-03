from db.db_conn import connection

conn = connection()
cursor = conn.cursor()

def add_doctor():
    id = input("Enter Doctor ID: ")
    name = input("Enter Doctor Name: ")
    special = input("Enter Doctor's Specialization: ")
    phone = input("Enter Mobile Number of Doctor: ")

    cursor.execute(
        "INSERT INTO Doctors (Doctor_id, Doctor_name, Specialization, Phone) VALUES (%s, %s, %s, %s)",
        (id, name, special, phone)
    )
    conn.commit()
    print("Doctor registered successfully!")


def view_doctors():
    cursor.execute("SELECT * FROM Doctors")
    rows = cursor.fetchall()
    if not rows:
        print("\nNo doctors found.")
        return

    print("\n-------------------- DOCTORS LIST --------------------")
    for row in rows:
        print(row)


def update_doctors():
    doc_id = input("Enter the Doctor ID you want to update: ")
    cursor.execute("SELECT * FROM Doctors WHERE Doctor_id = %s", (doc_id,))
    doctor = cursor.fetchone()

    if not doctor:
        print("Doctor not found!")
        return

    print(f"\nCurrent Details:\n Name: {doctor[1]}\n Specialization: {doctor[2]}\n Phone: {doctor[3]}")
    print("\nWhich fields do you want to update?")
    print("Options: name, specialization, phone")
    choices = input("Enter your choices separated by commas: ").lower().replace(" ", "").split(",")

    update_fields = []
    update_values = []

    if "name" in choices:
        new_name = input("Enter the updated name of the doctor: ")
        update_fields.append("Doctor_name = %s")
        update_values.append(new_name)

    if "specialization" in choices:
        new_s = input("Enter the updated specialization of the doctor: ")
        update_fields.append("Specialization = %s")
        update_values.append(new_s)

    if "phone" in choices:
        new_p = input("Enter the updated phone number of the doctor: ")
        update_fields.append("Phone = %s")
        update_values.append(new_p)

    if not update_fields:
        print("Please select a valid field to update.")
        return

    sql = f"UPDATE Doctors SET {', '.join(update_fields)} WHERE Doctor_id = %s"
    update_values.append(doc_id)
    cursor.execute(sql, tuple(update_values))
    conn.commit()

    print("Doctor details updated successfully!")


def delete_doctor():
    doc_id = input("Enter the Doctor ID you want to delete: ")
    cursor.execute("DELETE FROM Doctors WHERE Doctor_id = %s", (doc_id,))
    conn.commit()
    print("Doctor removed successfully!")
