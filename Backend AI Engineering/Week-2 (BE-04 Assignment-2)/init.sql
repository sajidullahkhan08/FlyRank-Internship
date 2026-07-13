CREATE TABLE IF NOT EXISTS tasks (
    id SERIAL PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Stretch goal: Add an index
CREATE INDEX IF NOT EXISTS idx_tasks_title ON tasks(title);