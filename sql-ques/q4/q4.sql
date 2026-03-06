CREATE DATABASE ECommerceDB;
USE ECommerceDB;

CREATE TABLE Orders (
    order_id     INT PRIMARY KEY,
    customer_id  INT           NOT NULL,
    product_id   INT           NOT NULL,
    quantity     INT           NOT NULL,
    total_amount DECIMAL(10, 2) NOT NULL
);

INSERT INTO Orders (order_id, customer_id, product_id, quantity, total_amount)
VALUES
-- Customer 1: 5 orders, high spender (appears in Q3 and Q4)
(1001, 1, 301,  3,  2500.00),
(1002, 1, 302,  5,  4200.00),
(1003, 1, 303,  2,  1800.00),
(1004, 1, 304,  4,  3100.00),
(1005, 1, 305,  1,   999.00),

-- Customer 2: 4 orders, high spender (appears in Q3 and Q4)
(1006, 2, 301,  6,  5400.00),
(1007, 2, 303,  3,  2700.00),
(1008, 2, 302,  2,  1600.00),
(1009, 2, 306,  4,  3800.00),

-- Customer 3: 2 orders, low spender
(1010, 3, 302,  1,   899.00),
(1011, 3, 305,  2,  1500.00),

-- Customer 4: 4 orders, moderate spender (appears in Q3)
(1012, 4, 303,  5,  4100.00),
(1013, 4, 301,  2,  1700.00),
(1014, 4, 304,  1,   750.00),
(1015, 4, 307,  3,  2200.00),

-- Customer 5: 1 order only
(1016, 5, 306,  2,  1800.00),

-- Customer 6: 5 orders, very high spender (appears in Q3 and Q4)
(1017, 6, 307, 10,  9500.00),
(1018, 6, 301,  4,  3600.00),
(1019, 6, 302,  3,  2400.00),
(1020, 6, 305,  6,  4800.00),
(1021, 6, 303,  2,  1600.00),

-- Customer 7: 2 orders
(1022, 7, 304,  3,  2100.00),
(1023, 7, 306,  1,   950.00),

-- Customer 8: 3 orders
(1024, 8, 301,  5,  4500.00),
(1025, 8, 307,  2,  1900.00),
(1026, 8, 302,  4,  3200.00),

-- Customer 9: 1 order, big single purchase (appears in Q4)
(1027, 9, 307, 15, 14000.00),

-- Customer 10: 2 orders
(1028, 10, 303, 3,  2400.00),
(1029, 10, 305, 2,  1600.00),

-- Extra orders to push product 301 quantity > 100 (appears in Q5)
(1030, 3, 301, 20,  16000.00),
(1031, 5, 301, 18,  14400.00),
(1032, 7, 301, 22,  17600.00),
(1033, 10, 301, 25, 20000.00),

-- Extra orders to push product 302 quantity > 100 (appears in Q5)
(1034, 4, 302, 20,  14000.00),
(1035, 9, 302, 22,  15400.00),
(1036, 5, 302, 18,  12600.00),
(1037, 3, 302, 25,  17500.00);

SELECT customer_id, SUM(total_amount) AS total_spent
FROM Orders
GROUP BY customer_id
ORDER BY total_spent DESC;

SELECT customer_id, COUNT(order_id) AS order_count
FROM Orders
GROUP BY customer_id
ORDER BY order_count DESC;

SELECT customer_id, COUNT(order_id) AS order_count
FROM Orders
GROUP BY customer_id
HAVING COUNT(order_id) > 3
ORDER BY order_count DESC;

SELECT customer_id, SUM(total_amount) AS total_spent
FROM Orders
GROUP BY customer_id
HAVING SUM(total_amount) > 10000
ORDER BY total_spent DESC;

SELECT product_id, SUM(quantity) AS total_quantity_sold
FROM Orders
GROUP BY product_id
HAVING SUM(quantity) > 100
ORDER BY total_quantity_sold DESC;