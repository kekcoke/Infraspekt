'use strict';
const { Router } = require('express');
const { execSync } = require('child_process');
const router = Router();

router.get('/status', (_req, res) => {
  res.json({
    services: [
      { name: 'Database', status: 'running', uptime: '99.9%' },
      { name: 'Cache', status: 'running', uptime: '99.8%' },
      { name: 'Load Balancer', status: 'running', uptime: '100%' },
    ],
    timestamp: new Date().toISOString(),
  });
});

// Assignment endpoint: real disk usage via df
router.get('/disk', (_req, res) => {
  try {
    const raw = execSync('df -h / | tail -1').toString().trim();
    const [filesystem, size, used, available, use_percent, mount] = raw.split(/\s+/);
    res.json({ filesystem, size, used, available, use_percent, mount, timestamp: new Date().toISOString() });
  } catch (err) {
    res.status(500).json({ error: 'Failed to retrieve disk metrics', detail: err.message });
  }
});

module.exports = router;
