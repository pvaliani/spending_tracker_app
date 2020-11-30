DROP TABLE IF EXISTS transactions;
DROP TABLE IF EXISTS amounts;
DROP TABLE IF EXISTS merchants;
DROP TABLE IF EXISTS merchant_types;

-- Creates an empty table called "amounts" to store values of floating point type which represent user inputted transaction amounts. Assigns a column called id as the primary key - don't need the amounts tbale as we are just inputting a value into transactions - doesn't need to track them so don't need a view.

CREATE TABLE amounts (
    id SERIAL PRIMARY KEY,
    value FLOAT
);

-- Creates an empty table called "merchant_types" to store names which represent merchant tags i.e "groceries". Assigns a column called id as the primary key

CREATE TABLE merchant_types (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255)
);

-- Creates an empty table called "merchants" to store names of merchants i.e "Amazon". Creates a column called merchant_type_id which represents the primary key id of merchant_types. Therefore, linking merchant and merchant_type_id as they are in the class definition of Merchant

CREATE TABLE merchants (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    merchant_type_id INT REFERENCES merchant_types(id) ON DELETE CASCADE
);

-- Creates an empty table called "Transactions" to store transactions. Creates a column called merchant_id which represents the primary key id of merchant_id and a column called amount_id which represents the primary key id of amount_id. Therefore, linking transactions to amounts and merchants as in the class defintion of Transaction


CREATE TABLE transactions (
    id SERIAL PRIMARY KEY,
    merchant_id SERIAL REFERENCES merchants(id) ON DELETE CASCADE,
    amount_id SERIAL REFERENCES amounts(id) ON DELETE CASCADE
);

-- delete amount_id and replace with the amount as an integer




-- Possibly add code to delete on cascade

-- format to access database tables below:

-- psql -U username -d mydatabase -c 'SELECT * FROM mytable'

-- psql -U user -d transactions -c 'SELECT SUM (value) FROM amounts'   - sums all amounts


