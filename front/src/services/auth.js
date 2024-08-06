import backendUrl from '../config';

export const login = async (badge_number, password) => {
  const response = await fetch(`${backendUrl}/login`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({ badge_number, password }),
  });

  if (!response.ok) {
    throw new Error('Numero de oficial o contraseña incorrectos');
  }

  const data = await response.json();
  return data.data;
};