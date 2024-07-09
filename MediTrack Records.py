######################################################################################################################
#
# Project Name - MediTrack Records
# School - The Heritage School, Kolkata
# Team - Innovators
# Participants - Divyansh Garg and Devansh Jain
#
########################################################################################################################


import csv
import random
from datetime import date

filename = 'PatientRecords.csv'


def writefile(fname, patient_name, patient_id, patient_dob, appointmentid, appointment_time, appointment_date,
              symptoms,
              disease):
    with open(fname, 'a') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerows([[patient_id, patient_name, patient_dob, appointmentid, appointment_time, appointment_date,
                              symptoms, disease]])


available_appointment_times = ["9.30AM", "10.00AM", "10.30AM", "11.00AM", "11.30AM", "12.00PM", "12.30AM", "1.00PM",
                               "1.30PM", "2.00PM", "2.30PM", "3.00PM", "2.00PM", "2.30PM", "3.00PM", "3.30PM", "4.00PM",
                               "4.30PM", "5.00PM", "5.30PM"]

appointment_id = 99999


def appointments():
    global available_appointment_times

    if len(available_appointment_times) == 0:
        print("No Available Appointments for the Day. Try Again Tomorrow!!")
        return

    print("Available Appointment Times - ")
    for time in available_appointment_times:
        print(time)

    find = 0
    while find == 0:
        booking_time = input("When would you like to schedule your Doctor's appointment - ")

        for time in available_appointment_times:
            if time == booking_time.upper():
                pid = generate_patient_id()
                global appointment_id
                appointment_id += 1
                print(f"""

Congratulations!!!
Your Booking for {booking_time} is Successful!!
Patient ID - {pid}
Appointment ID - {appointment_id}
                            """)
                available_appointment_times.remove(booking_time.upper())

                return pid, appointment_id, booking_time.upper(), date.today().strftime("%d/%m/%Y")

        print("Time Slot already taken...")


def generate_patient_id():
    pid = random.randint(100000, 999999)
    with open(filename, 'r') as csv1:
        csv_reader = csv.reader(csv1)
        for row in csv_reader:
            if row[0] == pid:
                generate_patient_id()
    return pid


def readfile(fname, pid):
    with open(fname, 'r') as csv1:
        csv_reader = csv.reader(csv1)
        for row in csv_reader:
            for col in row:
                print(col, end="\t\t")
            print()
            break

        for row in csv_reader:
            if str(row[0]) == str(pid):
                for col in row:
                    print(col, end="\t\t\t")
                print()
                return
        print("Patient ID Not Found")


def disease_diagnosis(pid, symptoms, disease):
    patient = []
    with open(filename, 'r') as csv1:
        csv_reader = csv.reader(csv1)
        for row in csv_reader:
            col = []
            for column in row:
                col.append(column)
            patient.append(col)
    write_disease_symptoms(pid, symptoms, disease, patient)


def write_disease_symptoms(pid, symptoms, disease, mylist):
    for i in range(0, len(mylist)):
        if str(mylist[i][0]) == str(pid):
            mylist[i][6] = symptoms
            mylist[i][7] = disease
            with open(filename, 'w') as csvfile:
                csvwriter = csv.writer(csvfile)
                csvwriter.writerows(mylist)
            return
    print("Patient ID Not Found")


def main():
    print("""

#################### Welcome to the XYZ Hospital!!! ####################

Are you a Doctor(D) or Patient(P)?""", end=" ")
    identity = input()
    if identity.upper() == "P":

        choice = 0
        while choice != 3:
            print("""
What would you like to do?
1. Schedule an Appointment
2. Enquire About Your Appointment/Disease Diagnosis
3. Exit

Enter your choice - """, end="")
            choice = int(input())
            if choice == 1:
                patient_name = input("Please enter the patient's name: ")
                patient_dob = input("Please enter the patient's DOB(DD/MM/YYYY): ")
                pid, aid, at, d = appointments()
                writefile(filename, patient_name, pid, patient_dob, aid, at, d, None, None)
            elif choice == 2:
                pid = int(input("Please enter the patient ID: "))
                readfile(filename, pid)
            elif choice == 3:
                return
            else:
                print("Wrong Input. Try Again")
    elif identity.upper() == "D":
        choice = 0
        while choice != 3:
            print("""
What would you like to do?
1. Disease Diagnosis
2. Enquire About Patient Details
3. Exit

Enter your choice - """, end="")
            choice = int(input())
            if choice == 1:
                pid = int(input("Please enter the patient ID: "))
                patient_symptoms = input("Please enter the patient's symptoms: ")
                patient_dis = input("Please enter the patient's disease diagnosis: ")
                disease_diagnosis(pid, patient_symptoms, patient_dis)
            elif choice == 2:
                pid = int(input("Please enter the patient ID: "))
                readfile(filename, pid)
            elif choice == 3:
                return
            else:
                print("Wrong Input. Try Again")


main()
