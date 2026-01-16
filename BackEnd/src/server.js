require('dotenv').config();
const app = require('./app');
const { sequelize, connectDB } = require('./config/database');
const { PORT } = require('./config/environment');

const startServer = async () => {
  try {
    // Connect to PostgreSQL
    await connectDB();

    // Sync models
    if (process.env.NODE_ENV === 'development') {
      await sequelize.sync({ alter: true });
      console.log('Database synced');
    }

    // Start server
    app.listen(PORT, () => {
      console.log(`Server running at http://localhost:${PORT}`);
    });
  } catch (error) {
    console.error('Server failed to start:', error);
    process.exit(1);
  }
};

startServer();
