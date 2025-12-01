const mongoose = require('mongoose');

const sessionSchema = new mongoose.Schema({
    tutorId: {
        type: mongoose.Schema.Types.ObjectId,
        required: true,
        ref: 'User'
    },
    studentId: {
        type: mongoose.Schema.Types.ObjectId,
        required: true,
        ref: 'User'
    },
    subject: {
        type: String,
        required: true
    },
    sessionDate: {
        type: Date,
        required: true
    },
    duration: {
        type: Number, // duration in minutes
        required: true
    },
    notes: {
        type: String,
        default: ''
    }
}, { timestamps: true });

const Session = mongoose.model('Session', sessionSchema);

module.exports = Session;