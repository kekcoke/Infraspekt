'use strict';
const { Router } = require('express');
const router = Router();

router.get('/', (_req, res) => {
  res.json({
    status: 'healthy',
    timestamp: new Date().toISOString(),
    service: 'infrawatch-backend',
  });
});

module.exports = router;
