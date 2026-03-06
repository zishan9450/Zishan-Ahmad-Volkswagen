CREATE DATABASE CompanyDB;
USE CompanyDB;

-- Table 1: Employees
CREATE TABLE Employees (
    emp_id       INT PRIMARY KEY,
    emp_name     VARCHAR(100) NOT NULL,
    department   VARCHAR(50),
    salary       DECIMAL(10, 2),
    joining_date DATE
);
-- Table 2: Projects
CREATE TABLE Projects (
    project_id   INT PRIMARY KEY,
    project_name VARCHAR(100) NOT NULL,
    start_date   DATE,
    end_date     DATE
);
-- Table 3: Employee_Project (Junction/Bridge Table)
CREATE TABLE Employee_Project (
    emp_id       INT,
    project_id   INT,
    hours_worked INT,
    rating       DECIMAL(3, 1),
    PRIMARY KEY (emp_id, project_id),
    FOREIGN KEY (emp_id)     REFERENCES Employees(emp_id),
    FOREIGN KEY (project_id) REFERENCES Projects(project_id)
);
INSERT INTO Employees (emp_id, emp_name, department, salary, joining_date)
VALUES
(1,  'Arjun Sharma',   'Engineering',  85000.00, '2020-03-15'),
(2,  'Priya Mehta',    'Engineering',  92000.00, '2019-07-01'),
(3,  'Rahul Verma',    'HR',           55000.00, '2021-01-10'),
(4,  'Sneha Kapoor',   'Marketing',    67000.00, '2018-11-22'),
(5,  'Vikram Singh',   'Engineering',  78000.00, '2022-06-05'),
(6,  'Anjali Rao',     'HR',           60000.00, '2020-09-30'),
(7,  'Karan Patel',    'Marketing',    72000.00, '2017-04-18'),
(8,  'Divya Nair',     'Finance',      88000.00, '2023-02-14'),
(9,  'Rohit Joshi',    'Finance',      91000.00, '2016-08-25'),
(10, 'Meena Iyer',     'Marketing',    65000.00, '2021-12-01');

INSERT INTO Projects (project_id, project_name, start_date, end_date)
VALUES
(101, 'Alpha Launch',     '2023-01-01', '2023-06-30'),
(102, 'Beta Redesign',    '2023-03-15', '2023-09-15'),
(103, 'Gamma Analytics',  '2023-07-01', '2024-01-31'),
(104, 'Delta Migration',  '2024-02-01', '2024-08-31'),
(105, 'Epsilon Security', '2024-09-01', '2025-03-31');

INSERT INTO Employee_Project (emp_id, project_id, hours_worked, rating)
VALUES
-- Arjun on 3 projects (will appear in Q1)
(1, 101, 120, 4.5),
(1, 102,  95, 4.8),
(1, 103, 110, 4.2),

-- Priya on 4 projects (will appear in Q1)
(2, 101, 140, 3.9),
(2, 102, 130, 4.6),
(2, 103, 160, 4.9),
(2, 104,  80, 4.7),

-- Rahul on 1 project
(3, 102,  60, 3.5),

-- Sneha on 2 projects
(4, 103,  75, 4.1),
(4, 104,  90, 3.8),

-- Vikram on 3 projects (will appear in Q1)
(5, 101, 200, 4.3),
(5, 103, 180, 4.6),
(5, 105, 150, 4.5),

-- Anjali on 1 project
(6, 104,  50, 3.2),

-- Karan on 2 projects
(7, 101,  70, 4.9),
(7, 105,  85, 4.8),

-- Rohit on 1 project
(9, 105, 110, 2.9);

-- Divya (emp_id=8) and Meena (emp_id=10) have NO projects (will appear in Q4)

SELECT e.emp_id, e.emp_name
FROM Employees e
JOIN Employee_Project ep ON e.emp_id = ep.emp_id
GROUP BY e.emp_id, e.emp_name
HAVING COUNT(ep.project_id) > 2;

SELECT e.emp_id, e.emp_name, AVG(ep.rating) AS avg_rating
FROM Employees e
JOIN Employee_Project ep ON e.emp_id = ep.emp_id
GROUP BY e.emp_id, e.emp_name
HAVING AVG(ep.rating) > 4;

SELECT e.emp_id, e.emp_name, e.department, e.salary
FROM Employees e
WHERE e.salary = (
    SELECT MAX(salary)
    FROM Employees
    WHERE department = e.department
);

SELECT e.emp_id, e.emp_name
FROM Employees e
LEFT JOIN Employee_Project ep ON e.emp_id = ep.emp_id
WHERE ep.emp_id IS NULL;

SELECT p.project_id, p.project_name, SUM(ep.hours_worked) AS total_hours
FROM Projects p
JOIN Employee_Project ep ON p.project_id = ep.project_id
GROUP BY p.project_id, p.project_name
ORDER BY total_hours DESC
LIMIT 1;
