const express = require("express");
const router = express.Router();
const { protect } = require("../middleware/authMiddleware");
const dashboardController = require("../controllers/dashboardController");

router.get("/overview", protect, dashboardController.getDashboardOverview);
router.get("/chapter/:chapter", protect, dashboardController.getChapterProgress);

module.exports = router;
