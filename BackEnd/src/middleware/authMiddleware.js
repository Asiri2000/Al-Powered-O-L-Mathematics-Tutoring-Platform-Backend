const express = require('express');
const router = express.Router();
const userController = require('../controllers/userController');
const authMiddleware = require('../middleware/authMiddleware');

// Use authMiddleware.protect instead of destructuring
router.get('/profile', authMiddleware.protect, userController.getProfile);
router.put('/profile', authMiddleware.protect, userController.updateProfile);

module.exports = router;