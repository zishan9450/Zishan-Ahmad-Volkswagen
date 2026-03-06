CREATE DATABASE RetailDB;
USE RetailDB;

-- Table 1: Customers
CREATE TABLE Customers (
    customer_id INT PRIMARY KEY,
    name        VARCHAR(100) NOT NULL,
    city        VARCHAR(50)
);

-- Table 2: Products
CREATE TABLE Products (
    product_id   INT PRIMARY KEY,
    product_name VARCHAR(100) NOT NULL,
    price        DECIMAL(10, 2)
);

-- Table 3: Orders
CREATE TABLE Orders (
    order_id      INT PRIMARY KEY,
    customer_id   INT,
    order_date    DATE,
    total_amount  DECIMAL(10, 2),
    FOREIGN KEY (customer_id) REFERENCES Customers(customer_id)
);

-- Table 4: Order_Items
CREATE TABLE Order_Items (
    order_item_id INT PRIMARY KEY,
    order_id      INT,
    product_id    INT,
    quantity      INT,
    FOREIGN KEY (order_id)   REFERENCES Orders(order_id),
    FOREIGN KEY (product_id) REFERENCES Products(product_id)
);

INSERT INTO Customers (customer_id, name, city)
VALUES
(1,  'Aarav Sharma',   'Delhi'),
(2,  'Priya Nair',     'Mumbai'),
(3,  'Rohan Gupta',    'Bangalore'),
(4,  'Sneha Patel',    'Ahmedabad'),
(5,  'Vikram Reddy',   'Hyderabad'),
(6,  'Anjali Mehta',   'Chennai'),
(7,  'Karan Singh',    'Pune'),
(8,  'Divya Iyer',     'Kolkata'),
(9,  'Mohit Joshi',    'Jaipur'),
(10, 'Neha Verma',     'Lucknow');
-- Customers 9 and 10 will have NO orders (used in Q4)

INSERT INTO Products (product_id, product_name, price)
VALUES
(201, 'Wireless Mouse',    499.00),
(202, 'Mechanical Keyboard', 1299.00),
(203, 'USB-C Hub',          799.00),
(204, 'Laptop Stand',       999.00),
(205, 'Webcam HD',         1499.00),
(206, 'Noise Cancelling Headphones', 2999.00),
(207, 'Monitor 24 inch',  12999.00),
(208, 'Desk Lamp LED',      599.00);

INSERT INTO Orders (order_id, customer_id, order_date, total_amount)
VALUES
-- Aarav: 4 orders (appears in Q1)
(1001, 1, '2024-01-05',  1500.00),
(1002, 1, '2024-02-14',  2300.00),
(1003, 1, '2024-03-22',  999.00),
(1004, 1, '2024-04-10',  4500.00),

-- Priya: 5 orders (appears in Q1)
(1005, 2, '2024-01-18',  3200.00),
(1006, 2, '2024-02-25',  1800.00),
(1007, 2, '2024-03-30',  2700.00),
(1008, 2, '2024-05-12',  5100.00),
(1009, 2, '2024-06-08',  4400.00),

-- Rohan: 2 orders
(1010, 3, '2024-02-01',  1200.00),
(1011, 3, '2024-04-19',  2600.00),

-- Sneha: 4 orders (appears in Q1)
(1012, 4, '2024-01-28',  3900.00),
(1013, 4, '2024-03-05',  2100.00),
(1014, 4, '2024-05-21',  4800.00),
(1015, 4, '2024-07-13',  1700.00),

-- Vikram: 3 orders
(1016, 5, '2024-02-09',  6200.00),
(1017, 5, '2024-04-27',  3400.00),
(1018, 5, '2024-06-15',  5500.00),

-- Anjali: 1 order
(1019, 6, '2024-03-17',  899.00),

-- Karan: 2 orders
(1020, 7, '2024-05-04',  1300.00),
(1021, 7, '2024-07-22',  2200.00),

-- Divya: 1 order
(1022, 8, '2024-06-30',  750.00);
-- Mohit (9) and Neha (10) have NO orders — will appear in Q4

INSERT INTO Order_Items (order_item_id, order_id, product_id, quantity)
VALUES
-- Order 1001
(1, 1001, 201, 2),   -- 2x Wireless Mouse
(2, 1001, 208, 1),   -- 1x Desk Lamp

-- Order 1002
(3, 1002, 202, 1),   -- 1x Keyboard
(4, 1002, 203, 2),   -- 2x USB-C Hub

-- Order 1003
(5, 1003, 204, 1),   -- 1x Laptop Stand

-- Order 1004
(6, 1004, 205, 1),   -- 1x Webcam
(7, 1004, 201, 3),   -- 3x Wireless Mouse

-- Order 1005
(8,  1005, 206, 1),  -- 1x Headphones
(9,  1005, 201, 2),  -- 2x Wireless Mouse

-- Order 1006
(10, 1006, 202, 1),  -- 1x Keyboard
(11, 1006, 208, 2),  -- 2x Desk Lamp

-- Order 1007
(12, 1007, 201, 4),  -- 4x Wireless Mouse
(13, 1007, 203, 1),  -- 1x USB-C Hub

-- Order 1008
(14, 1008, 207, 1),  -- 1x Monitor
(15, 1008, 204, 2),  -- 2x Laptop Stand

-- Order 1009
(16, 1009, 205, 2),  -- 2x Webcam
(17, 1009, 206, 1),  -- 1x Headphones

-- Order 1010
(18, 1010, 201, 1),  -- 1x Wireless Mouse
(19, 1010, 208, 1),  -- 1x Desk Lamp

-- Order 1011
(20, 1011, 202, 2),  -- 2x Keyboard

-- Order 1012
(21, 1012, 207, 1),  -- 1x Monitor
(22, 1012, 201, 2),  -- 2x Wireless Mouse

-- Order 1013
(23, 1013, 203, 3),  -- 3x USB-C Hub

-- Order 1014
(24, 1014, 206, 1),  -- 1x Headphones
(25, 1014, 205, 1),  -- 1x Webcam

-- Order 1015
(26, 1015, 208, 2),  -- 2x Desk Lamp

-- Order 1016
(27, 1016, 207, 1),  -- 1x Monitor
(28, 1016, 202, 1),  -- 1x Keyboard

-- Order 1017
(29, 1017, 201, 5),  -- 5x Wireless Mouse
(30, 1017, 204, 1),  -- 1x Laptop Stand

-- Order 1018
(31, 1018, 206, 2),  -- 2x Headphones

-- Order 1019
(32, 1019, 208, 1),  -- 1x Desk Lamp
(33, 1019, 201, 1),  -- 1x Wireless Mouse

-- Order 1020
(34, 1020, 203, 2),  -- 2x USB-C Hub

-- Order 1021
(35, 1021, 204, 1),  -- 1x Laptop Stand
(36, 1021, 202, 1),  -- 1x Keyboard

-- Order 1022
(37, 1022, 208, 1),  -- 1x Desk Lamp
(38, 1022, 201, 1);  -- 1x Wireless Mouse

SELECT c.customer_id, c.name, COUNT(o.order_id) AS order_count
FROM Customers c
JOIN Orders o ON c.customer_id = o.customer_id
GROUP BY c.customer_id, c.name
HAVING COUNT(o.order_id) > 3;

SELECT c.customer_id, c.name, SUM(o.total_amount) AS total_spent
FROM Customers c
JOIN Orders o ON c.customer_id = o.customer_id
GROUP BY c.customer_id, c.name
ORDER BY total_spent DESC
LIMIT 5;

SELECT p.product_id, p.product_name, SUM(oi.quantity) AS total_quantity
FROM Products p
JOIN Order_Items oi ON p.product_id = oi.product_id
GROUP BY p.product_id, p.product_name
ORDER BY total_quantity DESC
LIMIT 1;

SELECT c.customer_id, c.name, c.city
FROM Customers c
LEFT JOIN Orders o ON c.customer_id = o.customer_id
WHERE o.order_id IS NULL;

SELECT 
    YEAR(order_date)  AS order_year,
    MONTH(order_date) AS order_month,
    SUM(total_amount) AS monthly_revenue
FROM Orders
GROUP BY YEAR(order_date), MONTH(order_date)
ORDER BY order_year, order_month;