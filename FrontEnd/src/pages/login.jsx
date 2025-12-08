import React, { useState } from 'react';
import { useNavigate, Link } from 'react-router-dom';
import { loginUser } from '../api';

const Login = () => {
  const [formData, setFormData] = useState({
    username: '',
    password: ''
  });
  const [errors, setErrors] = useState({});
  const [isLoading, setIsLoading] = useState(false);
  const navigate = useNavigate();

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData({
      ...formData,
      [name]: value
    });
    // Clear error for this field
    if (errors[name]) {
      setErrors({
        ...errors,
        [name]: ''
      });
    }
  };

  const validateForm = () => {
    const newErrors = {};
    
    if (!formData.username.trim()) {
      newErrors.username = 'Username is required';
    }
    
    if (!formData.password) {
      newErrors.password = 'Password is required';
    } else if (formData.password.length < 6) {
      newErrors.password = 'Password must be at least 6 characters';
    }
    
    return newErrors;
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    const validationErrors = validateForm();
    
    if (Object.keys(validationErrors).length === 0) {
      setIsLoading(true);
      try {
        // 1. Call Backend
        const data = await loginUser(formData);
        
        // 2. Save Token (Session Storage is safer than LocalStorage for now)
        sessionStorage.setItem('accessToken', data.access_token);
        sessionStorage.setItem('username', formData.username);

        window.dispatchEvent(new Event("authChange"));
        // 3. Redirect
        // You might want to fetch user details here using the token, but for now just redirect
        navigate('/'); 
        
      } catch (err) {
        console.error(err);
        setErrors({ 
          password: 'Incorrect username or password' // Generic error for security
        });
      } finally {
        setIsLoading(false);
      }
    } else {
      setErrors(validationErrors);
    }
  };

  return (
    <div className="min-h-screen flex items-center justify-center bg-gradient-to-br from-emerald-50 to-green-50 p-4">
      <div className="bg-white rounded-2xl shadow-xl w-full max-w-md p-8 border border-emerald-100">
        <div className="text-center mb-8">
          <div className="inline-flex items-center justify-center w-16 h-16 bg-emerald-100 rounded-full mb-4">
            <svg className="w-8 h-8 text-emerald-600" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
              <path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M16 7a4 4 0 11-8 0 4 4 0 018 0zM12 14a7 7 0 00-7 7h14a7 7 0 00-7-7z"></path>
            </svg>
          </div>
          <h1 className="text-3xl font-bold text-emerald-900">Welcome Back</h1>
          <p className="text-emerald-600 mt-2">Sign in to your account</p>
        </div>

        <form onSubmit={handleSubmit} className="space-y-6">
          <div>
            <label className="block text-sm font-medium text-emerald-800 mb-2">
              Username
            </label>
            <input
              type="text"
              name="username"
              value={formData.username}
              onChange={handleChange}
              className={`w-full px-4 py-3 rounded-lg border ${
                errors.username ? 'border-red-500' : 'border-emerald-200'
              } focus:outline-none focus:ring-2 focus:ring-emerald-500 focus:border-transparent transition duration-200`}
              placeholder="Enter your username"
            />
            {errors.username && (
              <p className="text-red-500 text-sm mt-1">{errors.username}</p>
            )}
          </div>

          <div>
            <label className="block text-sm font-medium text-emerald-800 mb-2">
              Password
            </label>
            <input
              type="password"
              name="password"
              value={formData.password}
              onChange={handleChange}
              className={`w-full px-4 py-3 rounded-lg border ${
                errors.password ? 'border-red-500' : 'border-emerald-200'
              } focus:outline-none focus:ring-2 focus:ring-emerald-500 focus:border-transparent transition duration-200`}
              placeholder="Enter your password"
            />
            {errors.password && (
              <p className="text-red-500 text-sm mt-1">{errors.password}</p>
            )}
          </div>

          <div className="flex items-center justify-between">
            <div className="flex items-center">
              <input
                type="checkbox"
                id="remember"
                className="h-4 w-4 text-emerald-600 focus:ring-emerald-500 border-emerald-300 rounded"
              />
              <label htmlFor="remember" className="ml-2 text-sm text-emerald-700">
                Remember me
              </label>
            </div>
            <a href="#" className="text-sm font-medium text-emerald-600 hover:text-emerald-500">
              Forgot password?
            </a>
          </div>

          <button
            type="submit"
            className="w-full bg-gradient-to-r from-emerald-600 to-green-600 text-white font-semibold py-3 px-4 rounded-lg hover:from-emerald-700 hover:to-green-700 focus:outline-none focus:ring-2 focus:ring-emerald-500 focus:ring-offset-2 transition duration-200 transform hover:-translate-y-0.5"
          >
            Sign In
          </button>

          <div className="text-center">
            <p className="text-emerald-700">
              Don't have an account?{' '}
              <Link to="/signup" className="font-semibold text-emerald-600 hover:text-emerald-500">
                Sign up
              </Link>
            </p>
          </div>
        </form>

        <div className="mt-8 pt-8 border-t border-emerald-100">
          <p className="text-center text-sm text-emerald-600">
            © 2024 Student Portal. All rights reserved.
          </p>
        </div>
      </div>
    </div>
  );
};

export default Login;