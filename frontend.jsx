import React, { useState, useEffect } from 'eact';
import axios from 'axios';

function App() {
  const [patientQuery, setPatientQuery] = useState('');
  const [recommendedDoctors, setRecommendedDoctors] = useState([]);
  const [selectedDoctor, setSelectedDoctor] = useState(null);
  const [appointmentSlots, setAppointmentSlots] = useState([]);

  useEffect(() => {
    axios.post('/api/analyzeQuery', { query: patientQuery })
     .then(response => {
        setRecommendedDoctors(response.data.recommendedDoctors);
      })
     .catch(error => {
        console.error(error);
      });
  }, [patientQuery]);

  const handleSelectDoctor = (doctor) => {
    setSelectedDoctor(doctor);
    axios.post('/api/getAppointmentSlots', { doctorId: doctor.id })
     .then(response => {
        setAppointmentSlots(response.data.appointmentSlots);
      })
     .catch(error => {
        console.error(error);
      });
  };

  const handleBookAppointment = (appointmentSlot) => {
    axios.post('/api/bookAppointment', { doctorId: selectedDoctor.id, appointmentSlot: appointmentSlot })
     .then(response => {
        console.log(response.data);
      })
     .catch(error => {
        console.error(error);
      });
  };

  return (
    <div>
      <input type="text" value={patientQuery} onChange={(e) => setPatientQuery(e.target.value)} />
      <ul>
        {recommendedDoctors.map((doctor) => (
          <li key={doctor.id}>
            <img src={doctor.profileImage} alt={doctor.name} />
            <h2>{doctor.name}</h2>
            <p>{doctor.specialty}</p>
            <button onClick={() => handleSelectDoctor(doctor)}>Select</button>
          </li>
        ))}
      </ul>
      {selectedDoctor && (
        <div>
          <h2>Appointment Slots</h2>
          <ul>
            {appointmentSlots.map((appointmentSlot) => (
              <li key={appointmentSlot.id}>
                <p>{appointmentSlot.date} {appointmentSlot.time}</p>
                <button onClick={() => handleBookAppointment(appointmentSlot)}>Book</button>
              </li>
            ))}
          </ul>
        </div>
      )}
    </div>
  );
}

export default App;