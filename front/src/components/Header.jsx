import React from 'react';
import { useAuth } from '../context/AuthContext';
import { Link } from 'react-router-dom';

const Header = () => {
  const { token, logout } = useAuth();

  return (
    <header style={styles.header}>
      <h1 style={styles.title}>n5 - Challenge</h1>
      {token && (
        <button style={styles.button} onClick={logout}>
          Logout
        </button>
      )}
    </header>
  );
};

const styles = {
    header: {
      display: 'flex',
      justifyContent: 'space-between',
      alignItems: 'center',
      backgroundColor: '#333',
      color: '#fff',
      padding: '10px 20px',
      position: 'fixed',
      top: 0,
      left: 0,
      right: 0,
      zIndex: 1000, 
    },
    title: {
      margin: 0,
    },
    button: {
      backgroundColor: '#f44336',
      color: '#fff',
      border: 'none',
      padding: '10px 20px',
      cursor: 'pointer',
    },
};

export default Header;