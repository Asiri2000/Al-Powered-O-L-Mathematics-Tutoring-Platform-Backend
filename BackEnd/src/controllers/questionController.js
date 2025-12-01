const Question = require('../models/Question');

// Create a new question
exports.createQuestion = async (req, res) => {
    try {
        const questionData = req.body;
        const newQuestion = new Question(questionData);
        await newQuestion.save();
        res.status(201).json({ message: 'Question created successfully', question: newQuestion });
    } catch (error) {
        res.status(500).json({ message: 'Error creating question', error: error.message });
    }
};

// Get all questions
exports.getAllQuestions = async (req, res) => {
    try {
        const questions = await Question.find();
        res.status(200).json(questions);
    } catch (error) {
        res.status(500).json({ message: 'Error retrieving questions', error: error.message });
    }
};

// Get a question by ID
exports.getQuestionById = async (req, res) => {
    try {
        const question = await Question.findById(req.params.id);
        if (!question) {
            return res.status(404).json({ message: 'Question not found' });
        }
        res.status(200).json(question);
    } catch (error) {
        res.status(500).json({ message: 'Error retrieving question', error: error.message });
    }
};

// Update a question
exports.updateQuestion = async (req, res) => {
    try {
        const question = await Question.findByIdAndUpdate(req.params.id, req.body, { new: true });
        if (!question) {
            return res.status(404).json({ message: 'Question not found' });
        }
        res.status(200).json({ message: 'Question updated successfully', question });
    } catch (error) {
        res.status(500).json({ message: 'Error updating question', error: error.message });
    }
};

// Delete a question
exports.deleteQuestion = async (req, res) => {
    try {
        const question = await Question.findByIdAndDelete(req.params.id);
        if (!question) {
            return res.status(404).json({ message: 'Question not found' });
        }
        res.status(200).json({ message: 'Question deleted successfully' });
    } catch (error) {
        res.status(500).json({ message: 'Error deleting question', error: error.message });
    }
};