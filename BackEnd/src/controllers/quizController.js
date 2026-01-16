// BackEnd/src/controllers/quizController.js
const QuizAttempt = require("../models/QuizAttempt");
const ChapterMastery = require("../models/ChapterMastery");

exports.submitQuiz = async (req, res) => {
  try {
    const { user_id, chapter, answers, difficulty_level } = req.body;

    let correct = 0;
    let totalTime = 0;

    for (const a of answers) {
      const is_correct = a.selected_answer === a.correct_answer;
      if (is_correct) correct++;
      totalTime += a.time_taken;

      await QuizAttempt.create({
        user_id,
        chapter,
        question: a.question,
        selected_answer: a.selected_answer,
        correct_answer: a.correct_answer,
        is_correct,
        time_taken: a.time_taken
      });
    }

    const accuracy = correct / answers.length;
    const avg_time = totalTime / answers.length;

    // ---------- Mastery Curve ----------
    let mastery_level = "BEGINNER";
    if (accuracy >= 0.8) mastery_level = "EXAM_READY";
    else if (accuracy >= 0.65) mastery_level = "PROFICIENT";
    else if (accuracy >= 0.5) mastery_level = "PRACTICING";

    await ChapterMastery.upsert({
      user_id,
      chapter,
      mastery_level,
      accuracy,
      avg_time,
      difficulty_level,
      total_attempts: answers.length,
      updated_at: new Date()
    });

    res.status(200).json({
      accuracy,
      avg_time,
      mastery_level
    });

  } catch (error) {
    console.error(error);
    res.status(500).json({ message: "Quiz submission failed" });
  }
};
