const express = require('express');
const app = express();
const axios = require('axios');
const mysql = require('mysql');

const db = mysql.createConnection({
  host: 'localhost',
  user: 'root',
  password: 'password',
  database: 'appointment_booking'
});

app.use(express.json());

app.post('/api/analyzeQuery', (req, res) => {
  const query = req.body.query;
  // Call NLP API to analyze patient query
  axios.post('https://nlp-api.com/analyze', { query: query })
   .then(response => {
      const recommendedDoctors = response.data.recommendedDoctors;
      res.json({ recommendedDoctors: recommendedDoctors });
    })
   .catch(error => {
      console.error(error);
      res.status(500).json({ error: 'Error analyzing query' });
    });
});

app.post('/api/getAppointmentSlots', (req, res) => {
  const doctorId = req.body.doctorId;
  // Call scheduling API to get appointment slots
  axios.post('https://scheduling-api.com/getSlots', { doctorId: doctorId })
   .then(response => {
      const appointmentSlots = response.data.appointmentSlots;
      res.json({ appointmentSlots: appointmentSlots });
    })
   .catch(error => {
      console.error(error);
      res.status(500).json({ error: 'Error getting appointment slots' });
    });
});

app.post('/api/bookAppointment', (req, res) => {
  const doctorId = req.body.doctorId;
  const appointmentSlot = req.body.appointmentSlot;
  // Call database to book appointment
  db.query('INSERT INTO appointments (doctor_id, appointment_slot) VALUES (?, ?)', [doctorId, appointmentSlot], (error, results) => {
    if (error) {
      console.error(error);
      res.status(500).json({ error: 'Error booking appointment' });
    } else {
      res.json({ success: 'Appointment booked successfully' });
    }
  });
});

app.listen(3000, () => {
  console.log('Server started on port 3000');
});