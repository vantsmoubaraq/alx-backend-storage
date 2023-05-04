-- creates an index idx_name_first_score on the table names
-- Indexes First letter of the name and score

CREATE INDEX idx_name_first_score on names (name(1), score);