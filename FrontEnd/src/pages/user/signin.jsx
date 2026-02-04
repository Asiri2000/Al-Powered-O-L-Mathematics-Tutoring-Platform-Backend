import React, { useState } from 'react';
import { useNavigate, Link } from 'react-router-dom';
import { registerUser } from '../../api';

const Signin = () => {
  const [formData, setFormData] = useState({
    studentName: '',
    username: '',
    email: '',
    password: '',
    confirmPassword: '',
    grade: '',
    school: '',
  });

  const [errors, setErrors] = useState({});
  const [isLoading, setIsLoading] = useState(false);
  const navigate = useNavigate();

  const schools = [
    'Kg/Mw/Halpitiya K.V',
    'Kg/Mw/Parakrama M.V',
    'Kg/Puwakdeniya Model School',
  ];

  const grades = ['10', '11'];

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData({ ...formData, [name]: value });

    if (errors[name]) {
      setErrors({ ...errors, [name]: '' });
    }
  };

  const validateForm = () => {
    const newErrors = {};

    if (!formData.studentName.trim()) {
      newErrors.studentName = 'Student name is required';
    }

    if (!formData.username.trim()) {
      newErrors.username = 'Username is required';
    }

    if (!formData.email.trim()) {
      newErrors.email = 'Email is required';
    }

    if (!formData.password || formData.password.length < 6) {
      newErrors.password = 'Password must be at least 6 characters';
    }

    if (formData.password !== formData.confirmPassword) {
      newErrors.confirmPassword = 'Passwords do not match';
    }

    if (!formData.grade) {
      newErrors.grade = 'Grade is required';
    }

    if (!formData.school) {
      newErrors.school = 'School is required';
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
      await registerUser({
        studentName: formData.studentName,
        username: formData.username,
        email: formData.email,
        password: formData.password,
        grade: formData.grade,
        school: formData.school,
      });

      alert('Account created successfully! Please login.');
      navigate('/login');

    } catch (error) {
      console.error(error);
      setErrors({
        username: 'Registration failed. Email or username may already exist.',
      });
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <div className="min-h-screen flex items-center justify-center bg-gradient-to-br from-emerald-50 to-green-50 p-4">
      <div className="bg-white rounded-2xl shadow-xl w-full max-w-2xl p-8 border border-emerald-100">

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
                d="M18 9v3m0 0v3m0-3h3m-3 0h-3m-2-5a4 4 0 11-8 0 4 4 0 018 0zM3 20a6 6 0 0112 0v1H3v-1z"
              />
            </svg>
          </div>
          <h1 className="text-3xl font-bold text-emerald-900">Create Account</h1>
          <p className="text-emerald-600 mt-2">Join our student community</p>
        </div>

        {/* Form */}
        <form onSubmit={handleSubmit} className="space-y-6">

          {/* Name + Username */}
          <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
            <input
              name="studentName"
              placeholder="Student Name"
              value={formData.studentName}
              onChange={handleChange}
              className="input"
            />
            <input
              name="username"
              placeholder="Username"
              value={formData.username}
              onChange={handleChange}
              className="input"
            />
          </div>

          {/* Email */}
          <input
            name="email"
            type="email"
            placeholder="Email"
            value={formData.email}
            onChange={handleChange}
            className="input"
          />

          {/* Passwords */}
          <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
            <input
              type="password"
              name="password"
              placeholder="Password"
              value={formData.password}
              onChange={handleChange}
              className="input"
            />
            <input
              type="password"
              name="confirmPassword"
              placeholder="Confirm Password"
              value={formData.confirmPassword}
              onChange={handleChange}
              className="input"
            />
          </div>

          {/* Grade + School */}
          <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
            <div>
              <label className="block mb-2 font-medium">Grade</label>
              {grades.map((grade) => (
                <label key={grade} className="mr-4">
                  <input
                    type="radio"
                    name="grade"
                    value={grade}
                    checked={formData.grade === grade}
                    onChange={handleChange}
                  />{' '}
                  Grade {grade}
                </label>
              ))}
            </div>

            <select
              name="school"
              value={formData.school}
              onChange={handleChange}
              className="input"
            >
              <option value="">Select School</option>
              {schools.map((school) => (
                <option key={school} value={school}>
                  {school}
                </option>
              ))}
            </select>
          </div>

          {/* Submit */}
          <button
            type="submit"
            disabled={isLoading}
            className="w-full bg-gradient-to-r from-emerald-600 to-green-600 text-white font-semibold py-3 rounded-lg"
          >
            {isLoading ? 'Creating account...' : 'Create Account'}
          </button>

          <p className="text-center text-emerald-700">
            Already have an account?{' '}
            <Link to="/login" className="font-semibold text-emerald-600">
              Sign in
            </Link>
          </p>
        </form>

        <div className="mt-8 pt-8 border-t border-emerald-100 text-center text-sm text-emerald-600">
          © 2024 Student Portal. All rights reserved.
        </div>
      </div>
    </div>
  );
};

export default Signin;
