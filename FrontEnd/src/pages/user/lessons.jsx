import React, { useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import axios from 'axios';
import { motion } from 'framer-motion';

// Simple mapping for icons based on theme
const themeIcons = {
  geometry: '📐',
  algebra: '∑',
  numbers: '🔢',
  stats: '📊',
  logic: '🧩',
  default: '📝'
};

export default function lessons() {
  const [lessons, setLessons] = useState([]);
  const [loading, setLoading] = useState(true);
  const navigate = useNavigate();

  useEffect(() => {
    const fetchLessons = async () => {
      try {
        const res = await axios.get('http://127.0.0.1:8000/lessons/');
        setLessons(res.data);
      } catch (err) {
        console.error("Error fetching lessons:", err);
      } finally {
        setLoading(false);
      }
    };
    fetchLessons();
  }, []);

  if (loading) return <div className="p-10 text-center">Loading Syllabus...</div>;

  return (
    <div className="min-h-screen bg-gray-50 p-8 pt-20">
      <div className="max-w-6xl mx-auto">
        <h1 className="text-3xl font-bold text-gray-800 mb-2">O/L Mathematics Syllabus</h1>
        <p className="text-gray-600 mb-8">Select a topic to begin your theory & practice session.</p>

        <div className="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-6">
          {lessons.map((lesson, index) => (
            <motion.div
              key={lesson.id}
              whileHover={{ y: -5, boxShadow: "0 10px 25px -5px rgba(0, 0, 0, 0.1)" }}
              className="bg-white rounded-2xl p-6 shadow-sm border border-gray-100 cursor-pointer flex flex-col items-center text-center transition-all"
              onClick={() => navigate(`/lesson/${lesson.id}`)}
            >
              {/* Icon Circle */}
              <div className={`w-16 h-16 rounded-full flex items-center justify-center text-3xl mb-4 ${
                index % 2 === 0 ? 'bg-blue-50 text-blue-500' : 'bg-green-50 text-green-500'
              }`}>
                {themeIcons[lesson.theme_slug] || themeIcons.default}
              </div>

              <h3 className="font-bold text-gray-800 text-lg mb-2 line-clamp-2">
                {lesson.title}
              </h3>
              
              <p className="text-gray-500 text-xs mb-4">
                {lesson.description || "Start learning concepts"}
              </p>

              <button className="mt-auto px-4 py-2 bg-green-700 text-white text-sm font-bold rounded-lg w-full hover:bg-green-800">
                START
              </button>
            </motion.div>
          ))}
        </div>
      </div>
    </div>
  );
}