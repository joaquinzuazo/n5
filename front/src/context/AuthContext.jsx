import { createContext, useState, useContext } from 'react';
import { useNavigate } from 'react-router-dom';

const AuthContext = createContext();

export const AuthProvider = ({ children }) => {
  const [token, setToken] = useState(null);
  const [refreshToken, setRefreshToken] = useState(null);
  const navigate = useNavigate();

  const login = (newToken, newRefreshToken) => {
    setToken(newToken);
    setRefreshToken(newRefreshToken);
    navigate('/dashboard');
  };

  const logout = () => {
    setToken(null);
    setRefreshToken(null);
    navigate('/');
  };

  return (
    <AuthContext.Provider value={{ token, refreshToken, login, logout }}>
      {children}
    </AuthContext.Provider>
  );
};

export const useAuth = () => useContext(AuthContext);