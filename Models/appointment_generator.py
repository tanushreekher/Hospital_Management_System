import os

def generate_appointment(appointment_id, patient_id, patient_name, doctor_id, doctor_name, appointment_date):
    if not os.path.exists("Appointments"):
        os.makedirs("Appointments")
    
    file_name = f"Appointments/{patient_id}_{patient_name}.txt"
    with open(file_name, "w") as file:
        file.write("Appointment Details:\n")
        file.write("___________________________________")
        file.write(f"Appointment Id: {appointment_id} \n")
        file.write(f"Patient Id: {patient_id}\n")
        file.write(f"Patient Name: {patient_name}\n")
        file.write(f"Doctor Id: {doctor_id}\n")
        file.write(f"Doctor Name: {doctor_name}\n")
        file.write(f"Appointment Date: {appointment_date}")
    print(f"Appointment generated : {file_name}")

def cancel_appointment(patient_id, patient_name):
    file_name = f"Appointments/{patient_id}_{patient_name}.txt"
    if os.path.exists(file_name):
        os.remove(file_name)
        print(f"Appointment Cancelled!")
    else:
        print("Appointment Not Found")