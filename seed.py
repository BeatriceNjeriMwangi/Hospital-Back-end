from models import db, Doctor, Patient, Appointment, Treatment
from app import app
from datetime import datetime

def seed_data():
    db.session.query(Doctor).delete()
    db.session.query(Patient).delete()
    db.session.query(Appointment).delete()
    db.session.query(Treatment).delete()
    db.session.commit()
    # Create doctors

    doctor1 = Doctor(fname="Dr. Smith",lname="Dr. Smith", email="dr.smith@example.com",  password=456,phone_number=7596,regNo=1,gender="Male")
    doctor2 = Doctor(fname="Dr. Johnson",lname="Dr. Smith", email="dr.johnson@example.com",  password=248,phone_number=4236,regNo=2,gender="Male")
    doctor3 = Doctor(fname="Dr. Johnson",lname="Norway", email="dr.johnson@example.com", password=132,phone_number=7922,regNo=4,gender="Male")
    doctor4 = Doctor(fname="Dr. Rashid",lname="Man", email="dr.rashid@example.com", password=2222, phone_number=7123,regNo=5,gender="Male")
    doctor5 = Doctor(fname="Dr. Claire",lname="Njoki", email="dr.claire@example.com", password=987, phone_number=7567,regNo=3,gender="Male")
    db.session.add(doctor1)
    db.session.add(doctor2)
    db.session.add(doctor3)
    db.session.add(doctor4)
    db.session.add(doctor5)
    
    # Create patients
    patient1 = Patient(fname="John Doe",lname="John Doe", email="john.doe@example.com",password=78824,phone_number=6527,regNo=1, gender="Male" )
    patient2 = Patient(fname="Jane Smith",lname="Jane Smith", email="jane.smith@example.com",password=6748 ,phone_number=98463,regNo=2, gender="Female")
    patient3 = Patient(fname="Claire",lname="Njoki", email="claire@example.com", password=987, phone_number=7567,regNo=3,gender="Female")
    patient4 = Patient(fname="Lewis",lname="Chacha", email="lewis@example.com", password=7895, phone_number=98734,regNo=4,gender="Male")
    patient5 = Patient(fname="Joy",lname="Wambui", email="joy@example.com", password=9287, phone_number=2834,regNo=5,gender="Female")


    db.session.add(patient1)
    db.session.add(patient2)
    db.session.add(patient3)
    db.session.add(patient4)
    db.session.add(patient5)
    db.session.commit()  # Commit patients first to obtain their IDs
    
    # Create appointments
    # appointment_date=datetime.strptime("02/02/2023", '%Y-%m-%d').date()
    # appointment_time=datetime.strptime("12:30", '%H:%M').time()
    appointment1 = Appointment( patients_id=patient1.id, doctors_id=doctor1.id,appointment_date=datetime.now().date(),appointment_time=datetime.now().time()
)
    appointment2 = Appointment(patients_id=patient2.id, doctors_id=doctor2.id,appointment_date=datetime.now().date(),appointment_time=datetime.now().time()
)
    appointment3 = Appointment(patients_id=patient4.id, doctors_id=doctor4.id,appointment_date=datetime.now().date(),appointment_time=datetime.now().time()
)
    appointment4 = Appointment(patients_id=patient5.id, doctors_id=doctor3.id,appointment_date=datetime.now().date(),appointment_time=datetime.now().time()
)

    db.session.add(appointment1)
    db.session.add(appointment2)
    db.session.add(appointment3)
    db.session.add(appointment4)
    db.session.commit()  # Commit appointments to obtain their IDs
    
    # Create treatments
    treatment1 = Treatment(appointment_id=appointment1.id, doctors_id=doctor1.id, patients_id=patient1.id, progress="Active")
    treatment2 = Treatment(appointment_id=appointment2.id, doctors_id=doctor2.id, patients_id=patient3.id, progress="Discharged")
    treatment3 = Treatment(appointment_id=appointment4.id, doctors_id=doctor5.id, patients_id=patient4.id, progress="Transfer")
    treatment4 = Treatment(appointment_id=appointment3.id, doctors_id=doctor3.id, patients_id=patient2.id, progress="Active")

    db.session.add(treatment1)
    db.session.add(treatment2)
    db.session.add(treatment3)
    db.session.add(treatment4)
    
    # Commit the changes
    db.session.commit()

if __name__ == '__main__':
    with app.app_context():
        
        seed_data()
