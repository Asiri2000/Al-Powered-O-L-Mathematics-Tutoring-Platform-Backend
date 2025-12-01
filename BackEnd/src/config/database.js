const mongoose = require('mongoose');
const config = require('./environment');

const connectDB = async () => {
    try {
        await mongoose.connect(config.database.uri, {
            useNewUrlParser: true,
            useUnifiedTopology: true,
            useCreateIndex: true,
        });
        console.log('MongoDB connected successfully');
    } catch (error) {
        console.error('MongoDB connection failed:', error.message);
        process.exit(1);
    }
};

module.exports = connectDB;