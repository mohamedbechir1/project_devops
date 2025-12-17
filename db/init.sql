CREATE TABLE IF NOT EXISTS notes (
  id SERIAL PRIMARY KEY,
  title TEXT NOT NULL,
  created_at TIMESTAMP DEFAULT NOW()
);

INSERT INTO notes (title) VALUES ('Hello DevOps');
