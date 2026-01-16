const express = require('express');
const router = express.Router();
const analyticsController = require('../controllers/analyticsController');
const { protect } = require('../middleware/authMiddleware');

router.get('/chapters/:userId', protect, analyticsController.getChapterAnalytics);
router.get('/summary/:userId', protect, analyticsController.getOverallSummary);

module.exports = router;
