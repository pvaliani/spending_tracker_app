DROP TABLE IF EXISTS transactions;
DROP TABLE IF EXISTS amounts;
DROP TABLE IF EXISTS merchants;
DROP TABLE IF EXISTS merchant_types;

-- this was previously a VARCHAR(255) for name of humans but now a value of FLOAT

CREATE TABLE amounts (
    id SERIAL PRIMARY KEY,
    value FLOAT
);

CREATE TABLE merchant_types (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255)
);

CREATE TABLE merchants (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    merchant_type_id INT REFERENCES merchant_types(id)
);

CREATE TABLE transactions (
    id SERIAL PRIMARY KEY,
    merchant_id SERIAL REFERENCES merchants(id),
    amount_id SERIAL REFERENCES amounts(id)
);


-- possibly add code to delete on cascade