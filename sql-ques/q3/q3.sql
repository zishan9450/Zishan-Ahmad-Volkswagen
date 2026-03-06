CREATE DATABASE PerformanceDB;
USE PerformanceDB;

CREATE TABLE Employees (
    emp_id     INT PRIMARY KEY,
    emp_name   VARCHAR(100) NOT NULL,
    department VARCHAR(50)  NOT NULL,
    salary     DECIMAL(10, 2)
);

INSERT INTO Employees (emp_id, emp_name, department, salary)
VALUES
-- Engineering (high salaries)
(1,  'Arjun Sharma',    'Engineering', 95000.00),
(2,  'Priya Mehta',     'Engineering', 112000.00),
(3,  'Vikram Singh',    'Engineering', 78000.00),
(4,  'Sneha Kapoor',    'Engineering', 134000.00),
(5,  'Rahul Verma',     'Engineering', 89000.00),

-- HR (low-mid salaries)
(6,  'Anjali Rao',      'HR',          52000.00),
(7,  'Karan Patel',     'HR',          61000.00),
(8,  'Meena Iyer',      'HR',          48000.00),
(9,  'Divya Nair',      'HR',          57000.00),

-- Marketing (mid salaries)
(10, 'Rohit Joshi',     'Marketing',   72000.00),
(11, 'Neha Verma',      'Marketing',   85000.00),
(12, 'Aman Khanna',     'Marketing',   68000.00),
(13, 'Pooja Tiwari',    'Marketing',   91000.00),

-- Finance (mid-high salaries)
(14, 'Suresh Nambiar',  'Finance',     105000.00),
(15, 'Kavita Desai',    'Finance',     98000.00),
(16, 'Nikhil Yadav',    'Finance',     76000.00),
(17, 'Ritu Sharma',     'Finance',     88000.00),

-- Operations (low salaries)
(18, 'Deepak Menon',    'Operations',  45000.00),
(19, 'Swati Bose',      'Operations',  51000.00),
(20, 'Anil Kumar',      'Operations',  43000.00);

SELECT emp_id, emp_name, department, salary
FROM Employees
WHERE salary > (SELECT AVG(salary) FROM Employees);

SELECT e.emp_id, e.emp_name, e.department, e.salary
FROM Employees e
WHERE e.salary > (
    SELECT AVG(salary)
    FROM Employees
    WHERE department = e.department
);

SELECT emp_id, emp_name, department, salary
FROM Employees e
WHERE salary = (
    SELECT MAX(salary)
    FROM Employees
    WHERE department = e.department
);

SELECT emp_id, emp_name, department, salary
FROM Employees
WHERE salary > (SELECT AVG(salary) FROM Employees)
  AND salary < (SELECT MAX(salary) FROM Employees);

SELECT department, AVG(salary) AS dept_avg
FROM Employees
GROUP BY department
HAVING AVG(salary) > (SELECT AVG(salary) FROM Employees);