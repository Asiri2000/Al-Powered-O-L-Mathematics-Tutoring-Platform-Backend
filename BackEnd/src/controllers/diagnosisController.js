const { sequelize } = require('../config/database');

//GET /api/diagnosis/errors/:userId
 //Error type frequency per chapter

exports.getErrorBreakdown = async (req, res) => {
  const { userId } = req.params;

  const query = `
    SELECT 
      chapter,
      error_type,
      COUNT(*) AS occurrences
    FROM quiz_attempts
    WHERE user_id = :userId
      AND error_type IS NOT NULL
    GROUP BY chapter, error_type
    ORDER BY chapter, occurrences DESC
  `;

  const [results] = await sequelize.query(query, {
    replacements: { userId }
  });

  res.json(results);
};


 //GET /api/diagnosis/weaknesses/:userId
 //Rank chapters by lowest accuracy

exports.getWeakChapters = async (req, res) => {
  const { userId } = req.params;

  const query = `
    SELECT
      chapter,
      COUNT(*) AS total_attempts,
      SUM(CASE WHEN is_correct THEN 1 ELSE 0 END) AS correct_answers,
      ROUND(
        (SUM(CASE WHEN is_correct THEN 1 ELSE 0 END)::decimal
        / COUNT(*)) * 100, 2
      ) AS accuracy_percentage
    FROM quiz_attempts
    WHERE user_id = :userId
    GROUP BY chapter
    ORDER BY accuracy_percentage ASC
  `;

  const [results] = await sequelize.query(query, {
    replacements: { userId }
  });

  res.json(results);
};
