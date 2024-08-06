import React, { useEffect, useState } from 'react';
import axios from 'axios';
import { useAuth } from '../context/AuthContext';

const Infractions = () => {
  const [vehicles, setVehicles] = useState([]);
  const [searchEmail, setSearchEmail] = useState('');
  const [searchResults, setSearchResults] = useState([]);
  const [update, setUpdate] = useState(false);
  const [error, setError] = useState(null);
  const [modalError, setModalError] = useState(null);
  const { token } = useAuth();
  const [showModal, setShowModal] = useState(false);
  const [newInfraction, setNewInfraction] = useState({
    license_plate: '',
    timestamp: '',
    comments: '',
  });

  useEffect(() => {
    const fetchVehicles = async () => {
      try {
        const response = await axios.get('http://localhost:8000/vehicle', {
          headers: {
            Authorization: `Bearer ${token}`,
          },
        });
        setVehicles(response.data.data);
      } catch (err) {
        setError(err.message);
      }
    };

    fetchVehicles();
  }, [token, update]);

  const handleInputChange = (e) => {
    const { name, value } = e.target;
    setNewInfraction({ ...newInfraction, [name]: value });
  };

  const handleCreateInfraction = async (e) => {
    e.preventDefault();
    setModalError(null);
    try {
      await axios.post('http://localhost:8000/infractions', newInfraction, {
        headers: {
          Authorization: `Bearer ${token}`,
        },
      });
      setUpdate(!update);
      setShowModal(false);
      setNewInfraction({
        license_plate: '',
        timestamp: '',
        comments: '',
      });
    } catch (err) {
      setModalError(err.response?.data?.message || err.message);
    }
  };

  const handleSearch = async (e) => {
    e.preventDefault();
    setError(null);
    try {
      const response = await axios.get(`http://localhost:8000/infractions/report?email=${searchEmail}`);
      setSearchResults(response.data.data);
    } catch (err) {
      setError(err.response?.data?.message);
    }
  };

  return (
    <div style={styles.container}>
      <h2 style={styles.title}>Infracciones</h2>
      <button style={styles.createButton} onClick={() => {
        setShowModal(true);
        setNewInfraction({
          license_plate: '',
          timestamp: '',
          comments: '',
        });
      }}>Crear infraccion</button>
      <form onSubmit={handleSearch} style={styles.form}>
        <input
          type="email"
          name="searchEmail"
          placeholder="Correo electrónico"
          value={searchEmail}
          onChange={(e) => setSearchEmail(e.target.value)}
          style={styles.input}
          required
        />
        <button type="submit" className="submitButton">Buscar infracciones</button>
      </form>
      {error && <div style={styles.error}>Error: {error}</div>}
      {searchResults.length > 0 && (
        <div>
          <h3>Resultados de la búsqueda</h3>
          <table style={styles.table}>
            <thead>
              <tr>
                <th style={styles.th}>Patente</th>
                <th style={styles.th}>Fecha</th>
                <th style={styles.th}>Comentarios</th>
              </tr>
            </thead>
            <tbody>
              {searchResults.map((infraction) => (
                <tr key={infraction.id} style={styles.tr}>
                  <td style={styles.td}>{infraction.vehicle.license_plate}</td>
                  <td style={styles.td}>{infraction.timestamp}</td>
                  <td style={styles.td}>{infraction.comments}</td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      )}

      {showModal && (
        <div style={styles.modal}>
          <div style={styles.modalContent}>
            <h2 style={styles.modalTitle}>{'Crear infraccion'}</h2>
            <form onSubmit={handleCreateInfraction} style={styles.form}>
              <select
                name="license_plate"
                value={newInfraction.license_plate}
                onChange={handleInputChange}
                style={styles.input}
                required
              >
                <option value="" disabled>Selecciona un vehiculo</option>
                {vehicles.map((vehicle) => (
                  <option key={vehicle.license_plate} value={vehicle.license_plate}>
                    {vehicle.license_plate} (ID: {vehicle.id})
                  </option>
                ))}
              </select>
              <input
                type="datetime-local"
                name="timestamp"
                value={newInfraction.timestamp}
                onChange={handleInputChange}
                style={styles.input}
                required
              />
              <input
                type="text"
                name="comments"
                placeholder="Comentarios"
                value={newInfraction.comments}
                onChange={handleInputChange}
                style={styles.input}
                required
              />
           
              {modalError && <div style={styles.modalError}>{modalError}</div>}
              <button type="submit" style={styles.submitButton}>{'Crear'}</button>
              <button type="button" onClick={() => setShowModal(false)} style={styles.cancelButton}>Cancelar</button>
            </form>
          </div>
        </div>
      )}
    </div>
  );
};

const styles = {
  container: {
    width: '100%',
    margin: '20px auto',
    fontFamily: 'Arial, sans-serif',
  },
  title: {
    textAlign: 'center',
    color: '#fff',
  },
  table: {
    width: '100%',
    borderCollapse: 'collapse',
  },
  th: {
    border: '1px solid #ddd',
    padding: '8px',
    textAlign: 'left',
    backgroundColor: '#555',
    color: '#fff',
  },
  td: {
    border: '1px solid #ddd',
    padding: '8px',
    textAlign: 'left',
    color: '#fff',
  },
  tr: {
    backgroundColor: '#666',
  },
  error: {
    color: 'red',
    textAlign: 'center',
  },
  createButton: {
    marginBottom: '20px',
    padding: '10px 20px',
    color: '#fff',
    backgroundColor: '#5cb85c',
    border: 'none',
    borderRadius: '4px',
    cursor: 'pointer',
  },
  deleteButton: {
    padding: '6px 12px',
    color: '#fff',
    backgroundColor: '#d9534f',
    border: 'none',
    borderRadius: '4px',
    cursor: 'pointer',
  },
  editButton: {
    padding: '6px 12px',
    color: '#fff',
    backgroundColor: '#0275d8',
    border: 'none',
    borderRadius: '4px',
    cursor: 'pointer',
    marginRight: '10px',
  },
  modal: {
    position: 'fixed',
    top: 0,
    left: 0,
    right: 0,
    bottom: 0,
    backgroundColor: 'rgba(0, 0, 0, 0.5)',
    display: 'flex',
    justifyContent: 'center',
    alignItems: 'center',
  },
  modalContent: {
    backgroundColor: '#fff',
    padding: '20px',
    borderRadius: '4px',
    width: '300px',
  },
  modalTitle: {
    textAlign: 'center',
    marginBottom: '20px',
  },
  form: {
    display: 'flex',
    flexDirection: 'column',
    padding: '12px',
  },
  input: {
    marginBottom: '10px',
    padding: '8px',
    borderRadius: '4px',
    border: '1px solid #ccc',
  },
  modalError: {
    color: 'red',
    marginBottom: '10px',
    textAlign: 'center',
  },
  submitButton: {
    padding: '10px',
    color: '#fff',
    backgroundColor: '#5cb85c',
    border: 'none',
    borderRadius: '4px',
    cursor: 'pointer',
  },
  cancelButton: {
    padding: '10px',
    color: '#fff',
    backgroundColor: '#d9534f',
    border: 'none',
    borderRadius: '4px',
    cursor: 'pointer',
    marginTop: '10px',
  },
};

export default Infractions;