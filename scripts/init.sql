CREATE TABLE categories (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL
);

INSERT INTO categories (name) VALUES
('Food'),
('Transport'),
('Other');


CREATE TABLE transactions (
    id SERIAL PRIMARY KEY,
    user_id INT,
    description TEXT,
    amount NUMERIC(10,2),
    date DATE,
    category_id INT REFERENCES categories(id),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);