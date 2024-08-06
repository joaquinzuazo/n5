import React, { useEffect, useState } from 'react';
import axios from 'axios';
import { useAuth } from '../context/AuthContext';

const Persons = () => {
  const [persons, setPersons] = useState([]);
  const [update, setUpdate] = useState(false);
  const [error, setError] = useState(null);
  const [modalError, setModalError] = useState(null);
  const { token } = useAuth();
  const [showModal, setShowModal] = useState(false);
  const [newPerson, setNewPerson] = useState({
    name: '',
    email: '',
  });
  const [editMode, setEditMode] = useState(false);
  const [personToEdit, setPersonToEdit] = useState(null);

  useEffect(() => {
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

    fetchPersons();
  }, [token, update]);

  const handleDelete = async (id) => {
    try {
      await axios.delete(`http://localhost:8000/person/${id}`, {
        headers: {
          Authorization: `Bearer ${token}`,
        },
      });
      setPersons(persons.filter(officer => officer.id !== id));
    } catch (err) {
      setError(err.message);
    }
  };

  const handleInputChange = (e) => {
    const { name, value } = e.target;
    setNewPerson({ ...newPerson, [name]: value });
  };

  const handleCreatePerson = async (e) => {
    e.preventDefault();
    setModalError(null);
    try {
      await axios.post('http://localhost:8000/person', newPerson, {
        headers: {
          Authorization: `Bearer ${token}`,
        },
      });
      setUpdate(!update);
      setShowModal(false);
      setNewPerson({
        name: '',
        email: '',
      });
    } catch (err) {
      setModalError(err.response?.data?.message || err.message);
    }
  };

  const handleEditPerson = (person) => {
    setPersonToEdit(person);
    setNewPerson({
      name: person.name,
      email: person.email,
    });
    setEditMode(true);
    setShowModal(true);
  };

  const handleUpdatePerson = async (e) => {
    e.preventDefault();
    setModalError(null);
    try {
      await axios.put(`http://localhost:8000/officer/${personToEdit.id}`, newPerson, {
        headers: {
          Authorization: `Bearer ${token}`,
        },
      });
      setUpdate(!update);
      setShowModal(false);
      setNewPerson({
        name: '',
        email: '',
      });
      setEditMode(false);
      setPersonToEdit(null);
    } catch (err) {
      setModalError(err.response?.data?.message || err.message);
    }
  };

  return (
    <div style={styles.container}>
      <h2 style={styles.title}>Personas</h2>
      <button style={styles.createButton} onClick={() => {
        setEditMode(false);
        setShowModal(true);
        setNewPerson({
          name: '',
          email: '',
        });
      }}>Crear persona</button>
      <table style={styles.table}>
        <thead>
          <tr>
            <th style={styles.th}>Nombre</th>
            <th style={styles.th}>Email</th>
            <th style={styles.th}>Acciones</th>
          </tr>
        </thead>
        <tbody>
          {persons.map((person) => (
            <tr key={person.id} style={styles.tr}>
              <td style={styles.td}>{person.name}</td>
              <td style={styles.td}>{person.email}</td>
              <td style={styles.td}>
                <button 
                  style={styles.editButton} 
                  onClick={() => handleEditPerson(person)}
                >
                  Editar
                </button>
                  <button 
                    style={styles.deleteButton} 
                    onClick={() => handleDelete(person.id)}
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
            <h2 style={styles.modalTitle}>{editMode ? 'Editar persona' : 'Crear persona'}</h2>
            <form onSubmit={editMode ? handleUpdatePerson : handleCreatePerson} style={styles.form}>
              <input
                type="text"
                name="name"
                placeholder="Nombre"
                value={newPerson.name}
                onChange={handleInputChange}
                style={styles.input}
                required
              />
              <input
                type="email"
                name="email"
                placeholder="Email"
                value={newPerson.email}
                onChange={handleInputChange}
                style={styles.input}
                required
              />
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

export default Persons;