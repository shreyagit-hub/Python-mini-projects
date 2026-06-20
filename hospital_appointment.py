'''a hospital appointment system for patients and doctors'''

class Doctor:
    total_appointments = 0
    
    def __init__(self, name, specialization, available_slots):
        self.name = name
        self.specialization = specialization
        self.available_slots = available_slots
    
    @classmethod
    def get_total_appointments(cls):
        return cls.total_appointments
    
    def book_appointment(self):
        if self.available_slots > 0:
            self.available_slots -= 1
            Doctor.total_appointments += 1
            return True
        return False

class Patient:
    def __init__(self, name, age, phone):
        self.name = name
        self.age = age
        self.phone = phone

class Appointment:
    def __init__(self, patient, doctor, date, time):
        self.patient = patient
        self.doctor = doctor
        self.date = date
        self.time = time
    
    def display_appointment(self):
        print(f"Patient: {self.patient.name} | Age: {self.patient.age}")
        print(f"Doctor: {self.doctor.name} ({self.doctor.specialization})")
        print(f"Date: {self.date} | Time: {self.time}")
        print("\n")

#create doctors and patients
print("HOSPITAL APPOINTMENT BOOKING SYSTEM\n")
doc1 = Doctor("Dr. Yadav", "Cardiology", 5)
doc2 = Doctor("Dr. Maharjan", "Neurology", 3)

patient1 = Patient("Rita Kumari", 45, "555-1234")
patient2 = Patient("Sujan Thapa", 38, "555-5678")
patient3 = Patient("Binita KC", 52, "555-9012")

# Create appointments
print("Booking Appointments:\n")
if doc1.book_appointment():
    apt1 = Appointment(patient1, doc1, "2025-06-15", "10:00 AM")
    apt1.display_appointment()

if doc1.book_appointment():
    apt2 = Appointment(patient2, doc1, "2025-06-15", "11:00 AM")
    apt2.display_appointment()

if doc2.book_appointment():
    apt3 = Appointment(patient3, doc2, "2025-06-16", "02:00 PM")
    apt3.display_appointment()

print(f"Total Appointments Booked: {Doctor.get_total_appointments()}")
print(f"Dr. Yadav Available Slots: {doc1.available_slots}")
print(f"Dr. Maharjan Available Slots: {doc2.available_slots}")