import React, { useState } from 'react';

interface LogEntry {
  timestamp: string;
  level: 'INFO' | 'WARN' | 'ERROR' | 'DEBUG' | 'CRITICAL';
  message: string;
  metadata?: Record<string, string | number>;
}

interface ProcessingStats {
  processed: number;
  errors: number;
  successRate: number;
}

interface LogViewerProps {
  maxEntries?: number;
}

const LogViewer: React.FC<LogViewerProps> = ({ maxEntries = 100 }) => {
  const [logs] = useState<LogEntry[]>([]);
  const [stats] = useState<ProcessingStats>({
    processed: 0,
    errors: 0,
    successRate: 0
  });

  return (
    <div className="log-viewer">
      <h3>System Logs</h3>
      <div className="stats-bar">
        <span>Processed: {stats.processed}</span>
        <span>Errors: {stats.errors}</span>
        <span>Success Rate: {stats.successRate}%</span>
      </div>
      <div className="log-list">
        {logs.slice(0, maxEntries).map((log, index) => (
          <div key={index} className={`log-item log-${log.level.toLowerCase()}`}>
            <span className="timestamp">[{log.timestamp}]</span>
            <span className="level">{log.level}</span>
            <span className="message">{log.message}</span>
          </div>
        ))}
      </div>
    </div>
  );
};

export default LogViewer;
