import React, { useEffect, useState } from 'react';
import axios from 'axios';
import { useAuth } from '../context/AuthContext';

const Officials = () => {
  const [officers, setOfficers] = useState([]);
  const [update, setUpdate] = useState(false);
  const [error, setError] = useState(null);
  const [modalError, setModalError] = useState(null);
  const { token } = useAuth();
  const [showModal, setShowModal] = useState(false);
  const [newOfficer, setNewOfficer] = useState({
    name: '',
    badge_number: '',
    password: '',
    role: 'OFFICER',
  });
  const [editMode, setEditMode] = useState(false);
  const [officerToEdit, setOfficerToEdit] = useState(null);

  useEffect(() => {
    const fetchOfficers = async () => {
      try {
        const response = await axios.get('http://localhost:8000/officer', {
          headers: {
            Authorization: `Bearer ${token}`,
          },
        });
        setOfficers(response.data.data);
      } catch (err) {
        setError(err.message);
      }
    };

    fetchOfficers();
  }, [token, update]);

  const handleDelete = async (id) => {
    try {
      await axios.delete(`http://localhost:8000/officer/${id}`, {
        headers: {
          Authorization: `Bearer ${token}`,
        },
      });
      setOfficers(officers.filter(officer => officer.id !== id));
    } catch (err) {
      setError(err.message);
    }
  };

  const handleInputChange = (e) => {
    const { name, value } = e.target;
    setNewOfficer({ ...newOfficer, [name]: value });
  };

  const handleCreateOfficer = async (e) => {
    e.preventDefault();
    setModalError(null);
    try {
      await axios.post('http://localhost:8000/officer', newOfficer, {
        headers: {
          Authorization: `Bearer ${token}`,
        },
      });
      setUpdate(!update);
      setShowModal(false);
      setNewOfficer({
        name: '',
        badge_number: '',
        password: '',
        role: 'OFFICER',
      });
    } catch (err) {
      setModalError(err.response?.data?.message || err.message);
    }
  };

  const handleEditOfficer = (officer) => {
    setOfficerToEdit(officer);
    setNewOfficer({
      name: officer.name,
      badge_number: officer.badge_number,
      password: '',
      role: officer.role,
    });
    setEditMode(true);
    setShowModal(true);
  };

  const handleUpdateOfficer = async (e) => {
    e.preventDefault();
    setModalError(null);
    try {
      await axios.put(`http://localhost:8000/officer/${officerToEdit.id}`, newOfficer, {
        headers: {
          Authorization: `Bearer ${token}`,
        },
      });
      setUpdate(!update);
      setShowModal(false);
      setNewOfficer({
        name: '',
        badge_number: '',
        password: '',
        role: 'OFFICER',
      });
      setEditMode(false);
      setOfficerToEdit(null);
    } catch (err) {
      setModalError(err.response?.data?.message || err.message);
    }
  };

  return (
    <div style={styles.container}>
      <h2 style={styles.title}>Oficiales</h2>
      <button style={styles.createButton} onClick={() => {
        setEditMode(false);
        setShowModal(true);
        setNewOfficer({
          name: '',
          badge_number: '',
          password: '',
          role: 'OFFICER',
        });
      }}>Crear Oficial</button>
      <table style={styles.table}>
        <thead>
          <tr>
            <th style={styles.th}>Nombre</th>
            <th style={styles.th}>Número de placa</th>
            <th style={styles.th}>Rol</th>
            <th style={styles.th}>Acciones</th>
          </tr>
        </thead>
        <tbody>
          {officers.map((officer) => (
            <tr key={officer.id} style={styles.tr}>
              <td style={styles.td}>{officer.name}</td>
              <td style={styles.td}>{officer.badge_number}</td>
              <td style={styles.td}>{officer.role}</td>
              <td style={styles.td}>
                {officer.role !== 'ADMIN' && (
                <button 
                  style={styles.editButton} 
                  onClick={() => handleEditOfficer(officer)}
                >
                  Editar
                </button>
                )}
                {officer.role !== 'ADMIN' && (
                  <button 
                    style={styles.deleteButton} 
                    onClick={() => handleDelete(officer.id)}
                  >
                    Eliminar
                  </button>
                )}
              </td>
            </tr>
          ))}
        </tbody>
      </table>

      {showModal && (
        <div style={styles.modal}>
          <div style={styles.modalContent}>
            <h2 style={styles.modalTitle}>{editMode ? 'Editar Oficial' : 'Crear Oficial'}</h2>
            <form onSubmit={editMode ? handleUpdateOfficer : handleCreateOfficer} style={styles.form}>
              <input
                type="text"
                name="name"
                placeholder="Nombre"
                value={newOfficer.name}
                onChange={handleInputChange}
                style={styles.input}
                required
              />
              <input
                type="number"
                name="badge_number"
                placeholder="Número de placa"
                value={newOfficer.badge_number}
                onChange={handleInputChange}
                style={styles.input}
                required
              />
              {!editMode && (
                <input
                  type="password"
                  name="password"
                  placeholder="Contraseña"
                  value={newOfficer.password}
                  onChange={handleInputChange}
                  style={styles.input}
                  required
                />
              )}
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

export default Officials;