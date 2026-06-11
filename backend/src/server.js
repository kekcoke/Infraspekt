'use strict';
const express = require('express');
const cors = require('cors');
const healthRouter = require('./routes/health');
const infraRouter = require('./routes/infrastructure');

const app = express();
const PORT = process.env.PORT || 3001;

app.use(cors());
app.use(express.json());

app.use('/health', healthRouter);
app.use('/api/infrastructure', infraRouter);

// 404 fallback
app.use((_req, res) => res.status(404).json({ error: 'Not found' }));

if (require.main === module) {
  app.listen(PORT, () => console.log(`InfraWatch Backend running on port ${PORT}`));
}

module.exports = app; // exported for supertest
