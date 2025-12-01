module.exports = {
    development: {
        PORT: process.env.DEV_PORT || 3000,
        DB_URI: process.env.DEV_DB_URI || 'mongodb://localhost:27017/dev_db',
        JWT_SECRET: process.env.DEV_JWT_SECRET || 'your_dev_jwt_secret',
    },
    production: {
        PORT: process.env.PROD_PORT || 8000,
        DB_URI: process.env.PROD_DB_URI || 'mongodb://localhost:27017/prod_db',
        JWT_SECRET: process.env.PROD_JWT_SECRET || 'your_prod_jwt_secret',
    },
    test: {
        PORT: process.env.TEST_PORT || 4000,
        DB_URI: process.env.TEST_DB_URI || 'mongodb://localhost:27017/test_db',
        JWT_SECRET: process.env.TEST_JWT_SECRET || 'your_test_jwt_secret',
    },
};