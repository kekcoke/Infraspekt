'use strict';
const request = require('supertest');
const app = require('../src/server');

describe('GET /api/infrastructure/status', () => {
  it('returns 200 with an array of services', async () => {
    const res = await request(app).get('/api/infrastructure/status');
    expect(res.statusCode).toBe(200);
    expect(Array.isArray(res.body.services)).toBe(true);
    expect(res.body.services.length).toBeGreaterThan(0);
  });

  it('each service has name, status, and uptime fields', async () => {
    const res = await request(app).get('/api/infrastructure/status');
    res.body.services.forEach(s => {
      expect(s).toHaveProperty('name');
      expect(s).toHaveProperty('status');
      expect(s).toHaveProperty('uptime');
    });
  });
});

describe('GET /api/infrastructure/disk', () => {
  it('returns 200 with disk metrics', async () => {
    const res = await request(app).get('/api/infrastructure/disk');
    expect(res.statusCode).toBe(200);
    expect(res.body).toHaveProperty('filesystem');
    expect(res.body).toHaveProperty('size');
    expect(res.body).toHaveProperty('used');
    expect(res.body).toHaveProperty('available');
    expect(res.body).toHaveProperty('use_percent');
    expect(res.body).toHaveProperty('mount');
    expect(res.body.timestamp).toMatch(/^\d{4}-\d{2}-\d{2}T/);
  });
});

describe('404 fallback', () => {
  it('returns 404 for unknown routes', async () => {
    const res = await request(app).get('/nonexistent');
    expect(res.statusCode).toBe(404);
  });
});
