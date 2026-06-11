import React from 'react';
import { render, screen } from '@testing-library/react';
import App from './App';

test('renders product management dashboard title', async () => {
  render(<App />);
  const titleElement = await screen.findByText(/Product Management Dashboard/i);
  expect(titleElement).toBeInTheDocument();
});
