// src/api.js
import axios from 'axios';

const API_URL = 'http://127.0.0.1:8000/api/v1';

export const registerUser = async (userData) => {
  try {
    // We send JSON. Pydantic aliases handle 'studentName' -> 'full_name' mapping
    const response = await axios.post(`${API_URL}/users/register`, userData);
    return response.data;
  } catch (error) {
    throw error.response ? error.response.data : new Error('Network Error');
  }
};

export const loginUser = async (credentials) => {
  try {
    // FastAPI OAuth2 expects form-data, NOT JSON. We must convert it.
    const params = new URLSearchParams();
    params.append('username', credentials.username);
    params.append('password', credentials.password);

    const response = await axios.post(`${API_URL}/users/login`, params, {
      headers: { 'Content-Type': 'application/x-www-form-urlencoded' }
    });
    return response.data;
  } catch (error) {
    throw error.response ? error.response.data : new Error('Login failed');
  }
};