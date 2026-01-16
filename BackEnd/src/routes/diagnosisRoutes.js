const express = require('express');
const router = express.Router();
const diagnosisController = require('../controllers/diagnosisController');
const { protect } = require('../middleware/authMiddleware');

router.get('/errors/:userId', protect, diagnosisController.getErrorBreakdown);
router.get('/weaknesses/:userId', protect, diagnosisController.getWeakChapters);

module.exports = router;
