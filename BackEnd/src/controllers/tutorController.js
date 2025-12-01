const Tutor = require('../models/Tutor'); // Assuming you have a Tutor model defined

// Fetch all tutors
exports.getAllTutors = async (req, res) => {
    try {
        const tutors = await Tutor.find();
        res.status(200).json(tutors);
    } catch (error) {
        res.status(500).json({ message: 'Error fetching tutors', error });
    }
};

// Fetch a single tutor by ID
exports.getTutorById = async (req, res) => {
    const { id } = req.params;
    try {
        const tutor = await Tutor.findById(id);
        if (!tutor) {
            return res.status(404).json({ message: 'Tutor not found' });
        }
        res.status(200).json(tutor);
    } catch (error) {
        res.status(500).json({ message: 'Error fetching tutor', error });
    }
};

// Create a new tutor
exports.createTutor = async (req, res) => {
    const newTutor = new Tutor(req.body);
    try {
        const savedTutor = await newTutor.save();
        res.status(201).json(savedTutor);
    } catch (error) {
        res.status(400).json({ message: 'Error creating tutor', error });
    }
};

// Update a tutor's information
exports.updateTutor = async (req, res) => {
    const { id } = req.params;
    try {
        const updatedTutor = await Tutor.findByIdAndUpdate(id, req.body, { new: true });
        if (!updatedTutor) {
            return res.status(404).json({ message: 'Tutor not found' });
        }
        res.status(200).json(updatedTutor);
    } catch (error) {
        res.status(400).json({ message: 'Error updating tutor', error });
    }
};

// Delete a tutor
exports.deleteTutor = async (req, res) => {
    const { id } = req.params;
    try {
        const deletedTutor = await Tutor.findByIdAndDelete(id);
        if (!deletedTutor) {
            return res.status(404).json({ message: 'Tutor not found' });
        }
        res.status(204).send();
    } catch (error) {
        res.status(500).json({ message: 'Error deleting tutor', error });
    }
};