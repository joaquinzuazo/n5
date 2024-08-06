import React from 'react';
import { Link, Route, Routes } from 'react-router-dom';
import Officials from './Officials';
import Persons from './Persons';
import Vehicles from './Vehicles';
import Infractions from './Infractions';

const Dashboard = () => {
    return (
      <div style={styles.dashboard}>
        <nav style={styles.nav}>
          <Link to="officials" style={styles.link}>Oficiales</Link>
          <Link to="persons" style={styles.link}>Personas</Link>
          <Link to="vehicles" style={styles.link}>Vehículos</Link>
          <Link to="infractions" style={styles.link}>Infracciones</Link>
        </nav>
        <div style={styles.content}>
          <Routes>
            <Route path="officials" element={<Officials />} />
            <Route path="persons" element={<Persons />} />
            <Route path="vehicles" element={<Vehicles />} />
            <Route path="infractions" element={<Infractions />} />
          </Routes>
        </div>
      </div>
    );
  };

const styles = {
  dashboard: {
    display: 'flex',
    flexDirection: 'column',
    alignItems: 'center',
    padding: '20px',
    backgroundColor: '#444',
    borderRadius: '8px',
    marginTop: '20px',
    width: '100%',
  },
  nav: {
    display: 'flex',
    justifyContent: 'space-around',
    width: '100%',
    backgroundColor: '#555',
    padding: '10px',
    borderRadius: '4px',
    marginBottom: '20px',
  },
  link: {
    color: '#fff',
    textDecoration: 'none',
    padding: '10px 20px',
    borderRadius: '4px',
    backgroundColor: '#666',
  },
  content: {
    width: '100%',
    backgroundColor: '#555',
    padding: '20px',
    borderRadius: '4px',
  },
};

export default Dashboard;