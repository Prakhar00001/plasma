CREATE DATABASE appointment_booking;

USE appointment_booking;

CREATE TABLE doctors (
  id INT PRIMARY KEY AUTO_INCREMENT,
  name VARCHAR(255) NOT NULL,
  specialty VARCHAR(255) NOT NULL,
  profile_image VARCHAR(255) NOT NULL
);

CREATE TABLE appointments (
  id INT PRIMARY KEY AUTO_INCREMENT,
  doctor_id INT NOT NULL,
  appointment_slot DATETIME NOT NULL,
  FOREIGN KEY (doctor_id) REFERENCES doctors(id)
);