import { useState } from 'react';
import { useAuth } from '../context/AuthContext';
import { login as loginService } from '../services/auth';

const Login = () => {
  const [badge, setBadge] = useState('');
  const [password, setPassword] = useState('');
  const [error, setError] = useState('');
  const { login } = useAuth();

  const handleSubmit = async  (event) => {
    event.preventDefault();
    try {
        const { access_token, refresh_token } = await loginService(badge, password);
        login(access_token, refresh_token);
      } catch (error) {
        setError(error.message);
      }
  };

  return (
    <div className="form-container">
      <h2>Login</h2>
      {error && <p style={{ color: 'red' }}>{error}</p>}
      <form onSubmit={handleSubmit}>
        <div>
          <label>Username: </label>
          <input
            type="text"
            value={badge}
            onChange={(e) => setBadge(e.target.value)}
          />
        </div>
        <div>
          <label>Password: </label>
          <input
            type="password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
          />
        </div>
        <button type="submit">Login</button>
      </form>
    </div>
  );
};

export default Login;