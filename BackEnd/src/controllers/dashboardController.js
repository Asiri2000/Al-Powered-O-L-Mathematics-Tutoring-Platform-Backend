const QuizAttempt = require("../models/QuizAttempt");
const ChapterMastery = require("../models/ChapterMastery");
const { Op } = require("sequelize");

exports.getDashboardOverview = async (req, res) => {
  try {
    const user_id = req.user.id;

    const mastery = await ChapterMastery.findAll({
      where: { user_id },
      order: [["updated_at", "DESC"]]
    });

    const recentAttempts = await QuizAttempt.findAll({
      where: { user_id },
      order: [["createdAt", "DESC"]],
      limit: 20
    });

    res.json({
      chapters: mastery,
      recent_attempts: recentAttempts
    });
  } catch (err) {
    console.error(err);
    res.status(500).json({ message: "Dashboard load failed" });
  }
};

exports.getChapterProgress = async (req, res) => {
  try {
    const user_id = req.user.id;
    const { chapter } = req.params;

    const attempts = await QuizAttempt.findAll({
      where: {
        user_id,
        chapter
      },
      order: [["createdAt", "ASC"]]
    });

    res.json({
      chapter,
      attempts
    });
  } catch (err) {
    console.error(err);
    res.status(500).json({ message: "Progress fetch failed" });
  }
};
