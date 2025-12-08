import { useState } from 'react'
import './App.css'
import Navbar from './components/NavBar'
import Footer from './components/Footer'
import { BrowserRouter as Router, Routes, Route, Navigate } from 'react-router-dom';
import QuestionGenerator from './pages/questionGenerator';
import LearningCompanion from './pages/learningCompanion';
import Performance from './pages/Performance';
import Home from './pages/Home';
import Login from './pages/login';
import Signin from './pages/signin';
function App() {

  return (
    <Router>
        <Navbar />
        
        <Routes>
          <Route path='/' element={<Home/>} />
          <Route path="/generator" element={<QuestionGenerator />} />
          <Route path="/companion" element={<LearningCompanion />} />
          <Route path="/performance" element={<Performance/>} />
          <Route path="/login" element={<Login />} />
          <Route path="/signup" element={<Signin />} />
        </Routes>
        <Footer />
    </Router>
  )
}

export default App
