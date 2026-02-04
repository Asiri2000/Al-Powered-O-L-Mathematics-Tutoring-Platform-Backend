import React, { useState } from 'react';
import { useNavigate, Link } from 'react-router-dom';
import { loginUser } from '../../api';

const Login = () => {
  const [formData, setFormData] = useState({
    email: '',
    password: '',
  });

  const [errors, setErrors] = useState({});
  const [isLoading, setIsLoading] = useState(false);
  const navigate = useNavigate();

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData({ ...formData, [name]: value });

    if (errors[name]) {
      setErrors({ ...errors, [name]: '' });
    }
  };

  const validateForm = () => {
    const newErrors = {};

    if (!formData.email.trim()) {
      newErrors.email = 'Email is required';
    }

    if (!formData.password) {
      newErrors.password = 'Password is required';
    }

    return newErrors;
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    const validationErrors = validateForm();

    if (Object.keys(validationErrors).length !== 0) {
      setErrors(validationErrors);
      return;
    }

    setIsLoading(true);

    try {
      // 🔐 Call backend login
      const response = await loginUser(formData);

      // ✅ Store token & user info
      sessionStorage.setItem('accessToken', response.token);
      sessionStorage.setItem('username', response.user.username);
      sessionStorage.setItem('user_role', response.user.role);

      // Notify navbar / protected routes
      window.dispatchEvent(new Event('authChange'));

      // 🔀 Redirect by role
      if (response.user.role === 'admin') {
        navigate('/admin');
      } else {
        navigate('/');
      }

    } catch (error) {
      console.error(error);
      setErrors({
        password: 'Invalid email or password',
      });
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <div className="min-h-screen flex items-center justify-center bg-gradient-to-br from-emerald-50 to-green-50 p-4">
      <div className="bg-white rounded-2xl shadow-xl w-full max-w-md p-8 border border-emerald-100">

        {/* Header */}
        <div className="text-center mb-8">
          <div className="inline-flex items-center justify-center w-16 h-16 bg-emerald-100 rounded-full mb-4">
            <svg
              className="w-8 h-8 text-emerald-600"
              fill="none"
              stroke="currentColor"
              viewBox="0 0 24 24"
            >
              <path
                strokeLinecap="round"
                strokeLinejoin="round"
                strokeWidth="2"
                d="M16 7a4 4 0 11-8 0 4 4 0 018 0zM12 14a7 7 0 00-7 7h14a7 7 0 00-7-7z"
              />
            </svg>
          </div>
          <h1 className="text-3xl font-bold text-emerald-900">Welcome Back</h1>
          <p className="text-emerald-600 mt-2">Sign in to your account</p>
        </div>

        {/* Form */}
        <form onSubmit={handleSubmit} className="space-y-6">

          {/* Email */}
          <div>
            <label className="block text-sm font-medium text-emerald-800 mb-2">
              Email
            </label>
            <input
              type="email"
              name="email"
              value={formData.email}
              onChange={handleChange}
              className={`w-full px-4 py-3 rounded-lg border ${
                errors.email ? 'border-red-500' : 'border-emerald-200'
              } focus:outline-none focus:ring-2 focus:ring-emerald-500`}
              placeholder="Enter your email"
            />
            {errors.email && (
              <p className="text-red-500 text-sm mt-1">{errors.email}</p>
            )}
          </div>

          {/* Password */}
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
              } focus:outline-none focus:ring-2 focus:ring-emerald-500`}
              placeholder="Enter your password"
            />
            {errors.password && (
              <p className="text-red-500 text-sm mt-1">{errors.password}</p>
            )}
          </div>

          {/* Submit */}
          <button
            type="submit"
            disabled={isLoading}
            className="w-full bg-gradient-to-r from-emerald-600 to-green-600 text-white font-semibold py-3 px-4 rounded-lg hover:from-emerald-700 hover:to-green-700 transition"
          >
            {isLoading ? 'Signing in...' : 'Sign In'}
          </button>

          {/* Signup */}
          <div className="text-center">
            <p className="text-emerald-700">
              Don&apos;t have an account?{' '}
              <Link to="/signup" className="font-semibold text-emerald-600">
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
