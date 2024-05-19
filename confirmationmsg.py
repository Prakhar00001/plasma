# Define the patient and doctor information
patient_name = "ARYA KUMAR"
patient_email = "ARYAKUMAR@gmail.com"
doctor_name = "Dr. ARUN"
doctor_email = "drarun99@example.com"
appointment_time = "May 19, 2024 at 10:00 AM"

# Define the confirmation message for the patient
patient_message = f"Dear {patient_name},\n\nYour appointment with Dr. {doctor_name} has been confirmed for {appointment_time}.\n\nThank you for choosing our clinic. We look forward to seeing you soon.\n\nBest regards,\nThe Clinic Team"

# Define the confirmation message for the doctor
doctor_message = f"Dear Dr. {doctor_name},\n\nYou have a new appointment scheduled with {patient_name} on {appointment_time}.\n\nPlease confirm your availability and update your calendar accordingly.\n\nThank you,\nThe Clinic Team"

# Send the confirmation messages to the patient and the doctor
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Set up the email server
server = smtplib.SMTP('smtp.example.com', 587)
server.starttls()
server.login('youremail@example.com', 'yourpassword')

# Send the patient confirmation message
msg = MIMEMultipart()
msg['From'] = 'youremail@example.com'
msg['To'] = patient_email
msg['Subject'] = 'Appointment Confirmation'
msg.attach(MIMEText(patient_message, 'plain'))
server.sendmail('youremail@example.com', patient_email, msg.as_string())

# Send the doctor confirmation message
msg = MIMEMultipart()
msg['From'] = 'youremail@example.com'
msg['To'] = doctor_email
msg['Subject'] = 'New Appointment'
msg.attach(MIMEText(doctor_message, 'plain'))
server.sendmail('youremail@example.com', doctor_email, msg.as_string())

# Close the email server
server.quit()

print("Confirmation messages sent to patient and doctor.")