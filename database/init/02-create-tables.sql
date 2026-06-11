-- Log sources table
CREATE TABLE IF NOT EXISTS log_sources (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL UNIQUE,
    description TEXT,
    format_type VARCHAR(50) NOT NULL,
    parsing_rules JSONB,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Users table
CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(50) NOT NULL UNIQUE,
    email VARCHAR(100) NOT NULL UNIQUE,
    password_hash VARCHAR(255) NOT NULL,
    role user_role DEFAULT 'viewer',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    last_login TIMESTAMP
);

-- Log entries table (partitioned by timestamp)
CREATE TABLE IF NOT EXISTS log_entries (
    id BIGSERIAL,
    source_id INTEGER REFERENCES log_sources(id),
    timestamp TIMESTAMP NOT NULL,
    level log_level NOT NULL,
    message TEXT NOT NULL,
    metadata JSONB,
    processed_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (id, timestamp)
) PARTITION BY RANGE (timestamp);

-- Create current month partition (static for initialization)
CREATE TABLE IF NOT EXISTS log_entries_default PARTITION OF log_entries
    FOR VALUES FROM ('2024-01-01') TO ('2026-12-31');

-- Create indexes
CREATE INDEX IF NOT EXISTS idx_log_entries_timestamp ON log_entries (timestamp);
CREATE INDEX IF NOT EXISTS idx_log_entries_level ON log_entries (level);
