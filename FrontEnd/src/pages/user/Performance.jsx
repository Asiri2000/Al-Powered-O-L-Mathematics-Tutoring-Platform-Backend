import React, { useEffect, useState } from "react";
import axios from "axios";
import {
  TrendingUp,
  Award,
  BookOpen,
  CheckCircle2,
} from "lucide-react";

const API_URL = "http://127.0.0.1:5080/api";

/**
 * =========================
 * 📚 LESSONS BY GRADE
 * =========================
 */
const lessonsByGrade = {
  "10": [
    "Perimeter",
    "Square Root",
    "Fractions",
    "Binomial Expressions",
    "Congruence of Triangles",
    "Area",
    "Factors of Quadratic Expressions",
    "Triangles",
    "Inverse Propotions",
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
  "11": [
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
    "Trignometry",
    "Matrices",
    "Inequalities",
    "Cyclic Quadrilaterals",
    "Tangent",
    "Constructions",
    "Sets",
    "Probability",
  ],
};

const Performance = () => {
  const [grade, setGrade] = useState("");
  const [lesson, setLesson] = useState("");
  const [performance, setPerformance] = useState(null);
  const [loading, setLoading] = useState(false);

  const fetchPerformance = async () => {
    try {
      setLoading(true);
      const token = sessionStorage.getItem("accessToken");

      const res = await axios.get(
        `${API_URL}/dashboard/performance?grade=${grade}&lesson=${lesson}`,
        {
          headers: {
            Authorization: `Bearer ${token}`,
          },
        }
      );

      setPerformance(res.data);
    } catch (error) {
      console.error("Performance fetch failed", error);
      setPerformance(null);
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    if (grade && lesson) {
      fetchPerformance();
    }
  }, [grade, lesson]);

  return (
    <div className="min-h-screen bg-white px-4 py-10 flex justify-center">
      <div className="max-w-4xl w-full bg-[#e5fee6ff] rounded-2xl p-8 shadow-md">

        {/* Header */}
        <div className="flex items-center gap-4 mb-8">
          <div className="bg-green-100 p-3 rounded-xl">
            <TrendingUp className="w-8 h-8 text-green-700" />
          </div>
          <div>
            <h1 className="text-3xl font-bold text-black">
              Your Performance
            </h1>
            <p className="text-gray-500 font-medium">
              Lesson-wise personalized progress
            </p>
          </div>
        </div>

        {/* Filters */}
        <div className="grid grid-cols-1 md:grid-cols-2 gap-4 mb-8">
          <select
            value={grade}
            onChange={(e) => {
              setGrade(e.target.value);
              setLesson("");
              setPerformance(null);
            }}
            className="p-3 rounded-lg border border-gray-300"
          >
            <option value="">Select Grade</option>
            <option value="10">Grade 10</option>
            <option value="11">Grade 11</option>
          </select>

          <select
            value={lesson}
            onChange={(e) => setLesson(e.target.value)}
            className="p-3 rounded-lg border border-gray-300"
            disabled={!grade}
          >
            <option value="">Select Lesson</option>
            {grade &&
              lessonsByGrade[grade].map((lessonName) => (
                <option key={lessonName} value={lessonName}>
                  {lessonName}
                </option>
              ))}
          </select>
        </div>

        {/* Loading */}
        {loading && (
          <p className="text-center text-gray-500 font-medium">
            Loading performance...
          </p>
        )}

        {/* Stats */}
        {performance && !loading && (
          <div className="space-y-5">
            <StatCard
              title="Accuracy"
              value={`${performance.accuracy_percentage ?? 0}%`}
              subtext={`${performance.total_attempts ?? 0} attempts`}
              icon={<CheckCircle2 className="w-8 h-8 text-black" />}
            />

            <StatCard
              title="Average Time"
              value={`${performance.avg_time_seconds ?? 0}s`}
              subtext="Per question"
              icon={<Award className="w-8 h-8 text-black" />}
            />

            <StatCard
              title="Lesson"
              value={performance.lesson}
              subtext={`Grade ${performance.grade}`}
              icon={<BookOpen className="w-8 h-8 text-black" />}
            />
          </div>
        )}

        {!performance && grade && lesson && !loading && (
          <p className="text-center text-gray-500 mt-6">
            No attempts recorded for this lesson yet.
          </p>
        )}
      </div>
    </div>
  );
};

const StatCard = ({ title, value, subtext, icon }) => (
  <div className="relative rounded-2xl p-6 flex items-center justify-between bg-white shadow-md">
    <div>
      <h3 className="text-gray-600 font-semibold text-sm mb-1">{title}</h3>
      <div className="text-4xl font-bold text-black mb-1">{value}</div>
      <p className="text-green-600 text-sm font-medium">{subtext}</p>
    </div>
    <div className="bg-white/70 p-3 rounded-full shadow-sm">
      {icon}
    </div>
  </div>
);

export default Performance;
