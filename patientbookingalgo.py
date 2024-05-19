import datetime

def find_appointment_slot(appointments, doctor_id, appointment_time):
  # Check if the doctor is available at the specified time
  for appointment in appointments:
    if appointment.doctor_id == doctor_id and appointment.appointment_slot == appointment_time:
      return False
  return True

def book_appointment(appointments, doctor_id, appointment_time):
  # Book the appointment if the doctor is available
  if find_appointment_slot(appointments, doctor_id, appointment_time):
    appointments.append(Appointment(doctor_id, appointment_time))
    return True
  else:
    return False

appointments = [...]  # List of appointments
doctor_id = ...  # ID of the doctor
appointment_time = datetime.datetime(...)  # Appointment time
book_appointment(appointments, doctor_id, appointment_time)