-- Insert sample log sources
INSERT INTO log_sources (name, description, format_type, parsing_rules) VALUES
('nginx_access', 'Nginx access logs', 'nginx', '{"timestamp_format": "%d/%b/%Y:%H:%M:%S"}'),
('app_error', 'Application error logs', 'json', '{"level_field": "level"}')
ON CONFLICT (name) DO NOTHING;

-- Insert sample users
INSERT INTO users (username, email, password_hash, role) VALUES
('admin', 'admin@infraspekt.com', 'argon2_hash_placeholder', 'admin')
ON CONFLICT (username) DO NOTHING;
