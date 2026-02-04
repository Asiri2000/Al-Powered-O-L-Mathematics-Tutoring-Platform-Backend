import React, { useState, useRef, useEffect } from "react";
import {
  MessageCircleQuestion,
  CheckCircle,
  XCircle,
  Image as ImageIcon,
} from "lucide-react";

import { generateQuiz, submitQuizAttempt } from "../../api";

/* -------------------------------
   FULL O/L SYLLABUS
-------------------------------- */
const SYLLABUS = {
  10: [
    "Perimeter",
    "Square Root",
    "Fractions",
    "Binomial Expressions",
    "Congruence of Triangles",
    "Area",
    "Factors of Quadratic Expressions",
    "Triangles",
    "Inverse Proportions",
    "Data Representation",
    "Least Common Multiple of Algebraic Expressions",
    "Algebraic Fractions",
    "Percentages",
    "Equations",
    "Parallelograms",
    "Sets",
    "Logarithms",
    "Graphs",
    "Rate",
    "Formula",
    "Arithmetic Progressions",
    "Algebraic Inequalities",
    "Frequency Distributions",
    "Chords of a Circle",
    "Constructions",
    "Surface Area and Volume",
    "Probability",
    "Angles in a Circle",
    "Scale Diagrams",
  ],
  11: [
    "Real Numbers",
    "Indices and Logarithms",
    "Surface Area of Solids",
    "Volume of Solids",
    "Binomial Expressions",
    "Algebraic Fractions",
    "Areas of Plane Figures between Parallel Lines",
    "Percentages",
    "Share Market",
    "Mid Point Theorem",
    "Graphs",
    "Equations",
    "Equiangular Triangles",
    "Data Representation and Interpretation",
    "Geometric Progressions",
    "Pythagoras's Theorem",
    "Trigonometry",
    "Matrices",
    "Inequalities",
    "Cyclic Quadrilaterals",
    "Tangent",
    "Constructions",
    "Sets",
    "Probability",
  ],
};

const QuestionGenerator = () => {
  const [loading, setLoading] = useState(false);
  const [question, setQuestion] = useState(null);
  const [selectedOption, setSelectedOption] = useState(null);
  const [feedback, setFeedback] = useState("idle");

  const [selectedGrade, setSelectedGrade] = useState(10);
  const [selectedLesson, setSelectedLesson] = useState(SYLLABUS[10][0]);

  const lastQuestionRef = useRef(null);
  const questionRef = useRef(null);
  const startTimeRef = useRef(null);

  const resetQuestion = () => {
    setQuestion(null);
    setSelectedOption(null);
    setFeedback("idle");
    startTimeRef.current = null;
  };

  useEffect(() => {
    setSelectedLesson(SYLLABUS[selectedGrade][0]);
    resetQuestion();
    lastQuestionRef.current = null;
  }, [selectedGrade]);

  useEffect(() => {
    resetQuestion();
    lastQuestionRef.current = null;
  }, [selectedLesson]);

  /* ---------------------------------
     GENERATE QUESTION
  --------------------------------- */
  const generateQuestion = async () => {
    if (loading) return;

    setLoading(true);
    resetQuestion();

    try {
      const data = await generateQuiz({
        grade: selectedGrade,
        topic: selectedLesson,
        difficulty_level: 3,
        weak_areas: [],
      });

      const q = data?.questions?.[0];
      if (!q || !q.options) throw new Error("Invalid MCQ");

      if (q.question === lastQuestionRef.current)
        throw new Error("Repeated question");

      lastQuestionRef.current = q.question;
      startTimeRef.current = Date.now();
      setQuestion(q);

    } catch (err) {
      console.error("Quiz generation failed:", err);
      alert("❌ Failed to generate question.");
    } finally {
      setLoading(false);
    }
  };

  /* ---------------------------------
     CHECK ANSWER + SAVE ATTEMPT ✅
  --------------------------------- */
  const handleCheckAnswer = async () => {
    if (!selectedOption || !question) return;

    const isCorrect = selectedOption === question.correct_answer;
    setFeedback(isCorrect ? "correct" : "incorrect");

    const timeTaken = startTimeRef.current
      ? Math.round((Date.now() - startTimeRef.current) / 1000)
      : 0;

    try {
      await submitQuizAttempt({
        question_id: question.id || crypto.randomUUID(),
        chapter: selectedLesson,
        question: question.question,
        selected_answer: selectedOption,
        correct_answer: question.correct_answer,
        time_taken: timeTaken,
      });
    } catch (error) {
      console.error("❌ Failed to save quiz attempt", error);
    }

    if (isCorrect) {
      setTimeout(generateQuestion, 900);
    }
  };

  useEffect(() => {
    if (question && questionRef.current) {
      questionRef.current.scrollIntoView({ behavior: "smooth" });
    }
  }, [question]);

  return (
    <div className="flex flex-col items-center p-6 min-h-screen bg-[#F3FBF6]">
      <div className="bg-white p-6 rounded-xl w-full max-w-3xl shadow-sm">
        <h2 className="text-2xl font-bold mb-4 flex gap-2 items-center">
          <MessageCircleQuestion /> Question Generator
        </h2>

        <div className="flex gap-4 mb-4">
          {[10, 11].map((g) => (
            <button
              key={g}
              onClick={() => setSelectedGrade(g)}
              className={`px-4 py-2 rounded font-bold ${
                selectedGrade === g
                  ? "bg-green-700 text-white"
                  : "bg-gray-200"
              }`}
            >
              Grade {g}
            </button>
          ))}
        </div>

        <select
          value={selectedLesson}
          onChange={(e) => setSelectedLesson(e.target.value)}
          className="w-full mb-4 p-2 border rounded"
        >
          {SYLLABUS[selectedGrade].map((lesson) => (
            <option key={lesson}>{lesson}</option>
          ))}
        </select>

        <button
          onClick={generateQuestion}
          disabled={loading}
          className="w-full bg-green-700 text-white py-2 rounded font-bold"
        >
          {loading ? "Generating..." : "Generate Question"}
        </button>
      </div>

      {question && (
        <div
          ref={questionRef}
          className="bg-white p-6 mt-6 rounded-xl w-full max-w-3xl shadow-sm"
        >
          <h3 className="font-bold mb-3">{question.question}</h3>

          {question.needs_image && (
            <div className="mb-4 flex items-center gap-2 text-sm text-gray-600">
              <ImageIcon size={18} />
              Diagram will be generated here
            </div>
          )}

          <div className="grid grid-cols-1 md:grid-cols-2 gap-3">
            {Object.entries(question.options).map(([k, v]) => (
              <button
                key={k}
                onClick={() => {
                  setSelectedOption(k);
                  setFeedback("idle");
                }}
                className={`border p-3 rounded text-left ${
                  selectedOption === k
                    ? "bg-green-100 border-green-600"
                    : "hover:bg-gray-100"
                }`}
              >
                <strong>{k}.</strong> {v}
              </button>
            ))}
          </div>

          <button
            onClick={handleCheckAnswer}
            disabled={!selectedOption}
            className="mt-4 w-full bg-green-700 text-white py-2 rounded font-bold"
          >
            Check Answer
          </button>

          {feedback === "correct" && (
            <p className="text-green-600 mt-3 flex gap-2 items-center">
              <CheckCircle /> Correct! Next question coming…
            </p>
          )}

          {feedback === "incorrect" && (
  <div className="mt-4 p-4 border border-red-300 rounded bg-red-50">
    <p className="text-red-600 flex gap-2 items-center font-semibold">
      <XCircle /> Incorrect
    </p>

    <p className="mt-2 text-sm">
      <strong>Your Answer:</strong> {selectedOption}
    </p>

    <p className="mt-1 text-sm text-green-700">
      <strong>Correct Answer:</strong> {question.correct_answer}
    </p>

    {question.explanation && (
      <p className="mt-2 text-sm text-gray-700">
        <strong>Explanation:</strong> {question.explanation}
      </p>
    )}
  </div>
)}

        </div>
      )}
    </div>
  );
};

export default QuestionGenerator;
