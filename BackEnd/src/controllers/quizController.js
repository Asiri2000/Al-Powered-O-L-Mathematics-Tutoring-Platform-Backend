const QuizAttempt = require("../models/QuizAttempt");
const ChapterMastery = require("../models/ChapterMastery");
const Question = require("../models/Question");

exports.submitQuiz = async (req, res) => {
  try {
    const user_id = req.user.id; // 🔒 Authenticated user
    const { chapter, answers, difficulty_level } = req.body;

    if (!chapter || !Array.isArray(answers) || answers.length === 0) {
      return res.status(400).json({ message: "Invalid quiz payload" });
    }

    let correct = 0;
    let totalTime = 0;

    for (const a of answers) {
      const { questionId, selected_answer, time_taken } = a;

      // 🔒 1. Fetch question from DB (source of truth)
      const question = await Question.findByPk(questionId);

      if (!question) {
        return res.status(404).json({ message: "Question not found" });
      }

      // 🔒 2. Backend validation
      const is_correct = question.correctAnswer === selected_answer;

      if (is_correct) correct++;
      totalTime += time_taken;

      // 🔒 3. Store validated attempt (FIX IS HERE)
      await QuizAttempt.create({
        user_id,
        question_id: question.id,          // ✅ REQUIRED FIX
        chapter,
        question: question.questionText,
        selected_answer,
        correct_answer: question.correctAnswer,
        is_correct,
        time_taken
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

    return res.status(200).json({
      accuracy,
      avg_time,
      mastery_level
    });

  } catch (error) {
    console.error(error);
    return res.status(500).json({ message: "Quiz submission failed" });
  }
};
