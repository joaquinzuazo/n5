import React, { useEffect, useState } from 'react';
import axios from 'axios';
import { useAuth } from '../context/AuthContext';

const Vehicles = () => {
  const [vehicles, setVehicles] = useState([]);
  const [persons, setPersons] = useState([]);
  const [update, setUpdate] = useState(false);
  const [error, setError] = useState(null);
  const [modalError, setModalError] = useState(null);
  const { token } = useAuth();
  const [showModal, setShowModal] = useState(false);
  const [newVehicle, setNewVehicle] = useState({
    license_plate: '',
    brand: '',
    color: '',
    owner_id: '',
  });
  const [editMode, setEditMode] = useState(false);
  const [vehicleToEdit, setVehicleToEdit] = useState(null);

  useEffect(() => {
    const fetchVehicle = async () => {
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

    const fetchPersons = async () => {
      try {
        const response = await axios.get('http://localhost:8000/person', {
          headers: {
            Authorization: `Bearer ${token}`,
          },
        });
        setPersons(response.data.data);
      } catch (err) {
        setError(err.message);
      }
    };

    fetchVehicle();
    fetchPersons();
  }, [token, update]);

  const handleDelete = async (id) => {
    try {
      await axios.delete(`http://localhost:8000/vehicle/${id}`, {
        headers: {
          Authorization: `Bearer ${token}`,
        },
      });
      setVehicles(vehicles.filter(vehicle => vehicle.id !== id));
    } catch (err) {
      setError(err.message);
    }
  };

  const handleInputChange = (e) => {
    const { name, value } = e.target;
    setNewVehicle({ ...newVehicle, [name]: value });
  };

  const handleCreateVehicle = async (e) => {
    e.preventDefault();
    setModalError(null);
    try {
      await axios.post('http://localhost:8000/vehicle', newVehicle, {
        headers: {
          Authorization: `Bearer ${token}`,
        },
      });
      setUpdate(!update);
      setShowModal(false);
      setNewVehicle({
        license_plate: '',
        brand: '',
        color: '',
        owner_id: '',
      });
    } catch (err) {
      setModalError(err.response?.data?.message || err.message);
    }
  };

  const handleEditVehicle = (vehicle) => {
    setVehicleToEdit(vehicle);
    setNewVehicle({
      license_plate: vehicle.license_plate,
      brand: vehicle.brand,
      color: vehicle.color,
      owner_id: vehicle.owner_id,
    });
    setEditMode(true);
    setShowModal(true);
  };

  const handleUpdateVehicle = async (e) => {
    e.preventDefault();
    setModalError(null);
    try {
      await axios.put(`http://localhost:8000/vehicle/${vehicleToEdit.id}`, newVehicle, {
        headers: {
          Authorization: `Bearer ${token}`,
        },
      });
      setUpdate(!update);
      setShowModal(false);
      setNewVehicle({
        license_plate: '',
        brand: '',
        color: '',
        owner_id: '',
      });
      setEditMode(false);
      setVehicleToEdit(null);
    } catch (err) {
      setModalError(err.response?.data?.message || err.message);
    }
  };

  return (
    <div style={styles.container}>
      <h2 style={styles.title}>Vehiculos</h2>
      <button style={styles.createButton} onClick={() => {
        setEditMode(false);
        setShowModal(true);
        setNewVehicle({
          license_plate: '',
          brand: '',
          color: '',
          owner_id: '',
        });
      }}>Crear vehiculo</button>
      <table style={styles.table}>
        <thead>
          <tr>
            <th style={styles.th}>Patente</th>
            <th style={styles.th}>Modelo</th>
            <th style={styles.th}>Color</th>
            <th style={styles.th}>ID Propietario</th>
            <th style={styles.th}>Acciones</th>
          </tr>
        </thead>
        <tbody>
          {vehicles.map((vehicle) => (
            <tr key={vehicle.id} style={styles.tr}>
              <td style={styles.td}>{vehicle.license_plate}</td>
              <td style={styles.td}>{vehicle.brand}</td>
              <td style={styles.td}>{vehicle.color}</td>
              <td style={styles.td}>{vehicle.owner_id}</td>
              <td style={styles.td}>
                <button 
                  style={styles.editButton} 
                  onClick={() => handleEditVehicle(vehicle)}
                >
                  Editar
                </button>
                  <button 
                    style={styles.deleteButton} 
                    onClick={() => handleDelete(vehicle.id)}
                  >
                    Eliminar
                  </button>
              </td>
            </tr>
          ))}
        </tbody>
      </table>

      {showModal && (
        <div style={styles.modal}>
          <div style={styles.modalContent}>
            <h2 style={styles.modalTitle}>{editMode ? 'Editar vehiculo' : 'Crear vehiculo'}</h2>
            <form onSubmit={editMode ? handleUpdateVehicle : handleCreateVehicle} style={styles.form}>
              <input
                type="text"
                name="license_plate"
                placeholder="Patente"
                value={newVehicle.license_plate}
                onChange={handleInputChange}
                style={styles.input}
                required
              />
              <input
                type="text"
                name="brand"
                placeholder="Modelo"
                value={newVehicle.brand}
                onChange={handleInputChange}
                style={styles.input}
                required
              />
              <input
                type="text"
                name="color"
                placeholder="Color"
                value={newVehicle.color}
                onChange={handleInputChange}
                style={styles.input}
                required
              />
              <select
                name="owner_id"
                value={newVehicle.owner_id}
                onChange={handleInputChange}
                style={styles.input}
                required
              >
                <option value="" disabled>Selecciona un propietario</option>
                {persons.map((person) => (
                  <option key={person.id} value={person.id}>
                    {person.name} (ID: {person.id})
                  </option>
                ))}
              </select>
              {modalError && <div style={styles.modalError}>{modalError}</div>}
              <button type="submit" style={styles.submitButton}>{editMode ? 'Actualizar' : 'Crear'}</button>
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

export default Vehicles;