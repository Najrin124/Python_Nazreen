## 1️⃣ What is MySQL?

# MySQL is an open-source relational database management system (RDBMS) that stores data in tables using SQL (Structured Query Language).

# Example:

CREATE DATABASE school;

CREATE TABLE students (
    id INT PRIMARY KEY,
    name VARCHAR(50),
    age INT
);

INSERT INTO students VALUES (1, 'John', 20);


## 2️⃣ Difference Between Database and Schema
| Database                                 | Schema                                |
| ---------------------------------------- | ------------------------------------- |
| A container that holds data              | A logical structure inside a database |
| Contains tables, views, procedures, etc. | Organizes objects inside the database |
| One database can have multiple schemas   | Schema belongs to one database        |


# 1. What is a Primary Key?
A Primary Key is a column that uniquely identifies each row in a table.
Features


Unique values


Cannot be NULL


One primary key per table



Example
Students Table
student_idname1Rahul2Aman
Here:


student_id is the Primary Key


SQL:
CREATE TABLE students (    student_id INT PRIMARY KEY,    name VARCHAR(50));

# 2. What is a Foreign Key?
A Foreign Key is a column that creates a relationship between two tables.
It refers to the primary key of another table.

Example
Students Table
student_idname1Rahul
Orders Table
order_idstudent_id1011
Here:


student_id in orders is a Foreign Key


SQL:
CREATE TABLE orders (    order_id INT,    student_id INT,    FOREIGN KEY (student_id)    REFERENCES students(student_id));

#Primary Key vs Foreign Key
| Primary Key             | Foreign Key              |
| ----------------------- | ------------------------ |
| Uniquely identifies row | Creates relationship     |
| Cannot contain NULL     | Can contain NULL         |
| One per table           | Multiple allowed         |
| Unique                  | Duplicate values allowed |


# 4. What is a Subquery?
A Subquery is a query inside another query.

Example
SELECT nameFROM employeesWHERE salary > (    SELECT AVG(salary)    FROM employees);
Inner query:
SELECT AVG(salary) FROM employees
Outer query uses that result.

# 5. What is a Correlated Subquery?
A Correlated Subquery depends on the outer query.
It runs once for each row of the outer query.

Example
SELECT e1.nameFROM employees e1WHERE salary > (    SELECT AVG(salary)    FROM employees e2    WHERE e1.department = e2.department);
Here:


Inner query depends on outer query (e1.department)


Executes repeatedly



# Difference Between Subquery and Correlated Subquery
| Subquery    | Correlated Subquery    |
| ----------- | ---------------------- |
| Runs once   | Runs for each row      |
| Independent | Depends on outer query |
| Faster      | Usually slower         |

# 6. What is Indexing?
Indexing improves database search speed.
Like an index in a book:


Without index → search every page


With index → quickly find page



Example
CREATE INDEX idx_nameON students(name);

Advantages of Indexing


Faster SELECT queries


Faster searching


Improves performance



Disadvantages


Takes extra storage


INSERT/UPDATE may become slower



# 7. Difference Between MSSQL, MySQL, and MongoDB
| Feature       | MSSQL           | MySQL         | MongoDB               |
| ------------- | --------------- | ------------- | --------------------- |
| Type          | Relational DB   | Relational DB | NoSQL DB              |
| Company       | Microsoft       | Oracle        | MongoDB Inc           |
| Data Format   | Tables          | Tables        | JSON-like documents   |
| Schema        | Fixed           | Fixed         | Flexible              |
| Language      | SQL             | SQL           | BSON/JSON             |
| Best For      | Enterprise apps | Web apps      | Big/unstructured data |
| Open Source   | Limited         | Yes           | Yes                   |
| Relationships | Strong          | Strong        | Weak                  |

Example Data Storage
MySQL / MSSQL
id | name1  | Rahul

MongoDB
{  "id": 1,  "name": "Rahul"}

When to Use What?
| Database | Best Use                      |
| -------- | ----------------------------- |
| MSSQL    | Large enterprise systems      |
| MySQL    | Websites and applications     |
| MongoDB  | Flexible and large-scale apps |

Quick Summary
| Concept             | Meaning                |
| ------------------- | ---------------------- |
| Primary Key         | Unique identifier      |
| Foreign Key         | Connects tables        |
| WHERE               | Filters rows           |
| HAVING              | Filters grouped data   |
| Subquery            | Query inside query     |
| Correlated Subquery | Depends on outer query |
| Indexing            | Speeds up searching    |
| MySQL               | Relational DB          |
| MongoDB             | NoSQL DB               |








## SQL QUERY
## use anu_db;
-- update employees set salary = 60000 where emp_id = 1;

-- delete from employees where emp_id = 1;
-- -- select emp_id, name, salary from employees where salary > 50000;

-- select * from employees;

-- sub query - query inside a query

select * from employees where salary > (select avg(salary) from employees);

-- exists 

-- select dept_id from employees e1 where exists (select 1 from employees e2 where e2.dept_id = e1.dept_id);

select * from employees limit 10;

explain select * from employees;

select name, salary, salary * 12 as annual_salary from employees;

select * from employees where salary between 30000 and 50000;

select * from employees where dept_id in (1,2);

select * from employees where name like 'Emp3%';

-- join means combine data from mulitple tables

-- inner join - show only matcging records between 2 or more tables

select e.name, d.dept_name from employees e  inner join departments d on e.dept_id = d.dept_id;

-- left join - matching records + all records from left table

select e.name, d.dept_name from employees e  left join departments d on e.dept_id = d.dept_id;

-- right join - matching records + all records from right table

select e.name, d.dept_name from employees e  right join departments d on e.dept_id = d.dept_id;


- -- SELECT * FROM orders; 

-- -- INSERT INTO payments (order_id, payment_date, payment_status) VALUES
-- -- (1, '2026-05-01', 'Completed'),
-- -- (2, '2026-05-02', 'Pending'),
-- -- (3, '2026-05-03', 'Completed'),
-- -- (4, '2026-05-04', 'Failed'),
-- -- (5, '2026-05-05', 'Completed');

# use myDB;
-- select * from employees where dept_id in (1,2);

-- sub query - query inside a query

-- select * from employees e1 where salary > (select avg(salary) from employees e2 where e2.dept_id = e1.dept_id);

-- select distinct dept_id from employees e1 where exists (select 1 from employees e2 where e2.dept_id = e1.dept_id and e2.salary > 60000);



select * from employees;
select emp_name, salary from employees;
select * from employees where salary > 50000;
select * from employees where emp_name like 'A%';
select * from employees where emp_name like '%n';
select * from employees where emp_name like '%ar%';
select * from employees order by salary desc; 

SELECT * FROM employee
ORDER BY salary DESC;
# 🔹 1) SELECT *
SELECT → Keyword used to retrieve data from a database.
* (asterisk) → Means select all columns from the table.

👉 So this part means:
“Get all columns.”

If the table has:

id | name | salary | department

It will return all of them.

# 🔹 2) FROM employee
FROM → Specifies which table to retrieve data from.
employee → The table name.

👉 So this part means:
“Get data from the employee table.”

# 🔹 3) ORDER BY salary
ORDER BY → Sorts the result.
salary → Column used for sorting.

👉 This means:
“Sort the results based on salary.”

# 🔹 4) DESC
DESC → Descending order (highest to lowest).
Opposite is ASC (Ascending – lowest to highest).

👉 This means:
“Show highest salary first.”

# 🔹 5) ; (Semicolon)
Marks the end of the SQL statement.
Required in many SQL tools.

## . CHAR vs VARCHAR
| CHAR                  | VARCHAR         |
| --------------------- | --------------- |
| Fixed length          | Variable length |
| Pads spaces           | No padding      |
| Faster for fixed size | Saves storage   |



select * from customers where email is null;
select * from customers where email is not null;

--- select 10 + null; ---

| WHERE                          | HAVING                      |
| ------------------------------ | --------------------------- |
| Filters rows before grouping   | Filters after GROUP BY      |
| Cannot use aggregate functions | Can use aggregate functions |
| Used with SELECT               | Used with GROUP BY          |


| IN                     | EXISTS                   |
| ---------------------- | ------------------------ |
| Compares values        | Checks existence         |
| Good for small dataset | Better for large dataset |

--- For large datasets → EXISTS performs better.--------

 | Technique                | Example               |
| ------------------------ | --------------------- |
| Index on WHERE column    | salary                |
| Index on JOIN column     | dept_id               |
| Composite index          | (salary, dept_id)     |
| Avoid functions in WHERE | YEAR(hire_date)       |
| Use EXPLAIN              | Check query plan      |
| Use covering index       | Only required columns |







select * from employees;
select emp_name, salary from employees;
select * from employees where salary > 50000;
select * from employees where emp_name like 'A%';
select * from employees where emp_name like '%n';
select * from employees where emp_name like '%ar%';
select * from employees order by salary desc; 
select * from employees order by salary desc limit 5;
select distinct dept_id from employees;

select * from customers where email is null;
select * from customers where email is not null;
select 10 + null;  

select emp_id, emp_name, 
ifnull(salary, 0) as salary from employees;

select emp_name, count(*) from employees group by emp_name having count(*) > 1; 
select count(distinct dept_id) from employees;

SELECT * FROM customers c
WHERE EXISTS (
    SELECT 1 FROM orders o
    WHERE o.customer_id = c.customer_id
); 

select sum(salary) from employees;
SELECT dept_id, AVG(salary)
FROM employee
GROUP BY dept_id;

select max(salary) from employees;
select max(salary) from employees where salary < (select max(salary) from employees);
select  salary from employees order by salary desc limit 1 offset 2;                                                                                                                                            


select * from employees;
select * from departments;

SELECT e.emp_name, e.salary, d.dept_name
FROM employees e
JOIN departments d ON e.dept_id = d.dept_id
WHERE e.salary > 50000;

EXPLAIN SELECT e.emp_name, e.salary, d.dept_name
FROM employees e
JOIN departments d ON e.dept_id = d.dept_id
WHERE e.salary > 40000;

CREATE INDEX idx_salary ON employees(salary);

CREATE INDEX idx_dept_id ON employees(dept_id);

EXPLAIN SELECT e.emp_name, e.salary, d.dept_name
FROM employees e
JOIN departments d ON e.dept_id = d.dept_id
WHERE e.salary > 40000;

-- composite index

CREATE INDEX idx_salary_dept ON employees(salary, dept_id);

CREATE INDEX idx_covering ON employees(salary, emp_name);

EXPLAIN SELECT emp_name, salary
FROM employees
WHERE salary > 40000;

SHOW INDEX FROM employees;

START TRANSACTION;

UPDATE employees
SET salary = salary - 5000
WHERE emp_id = 1;

UPDATE employees
SET salary = salary + 5000
WHERE emp_id = 2;

COMMIT;

START TRANSACTION;

UPDATE employees
SET salary = salary - 100000
WHERE emp_id = 1;

ROLLBACK;

START TRANSACTION;

UPDATE employees SET salary = 90000 WHERE emp_id = 1;

SAVEPOINT before_second_update;

UPDATE employees SET salary = 100000 WHERE emp_id = 2;

ROLLBACK TO before_second_update;

COMMIT;
select * from departments;

INSERT INTO departments (dept_id,dept_name,Location)
VALUES
(29, 'Operations', 'Pune'),
(30, 'Customer Support', 'Hyderabad');
ALTER TABLE departments
ADD  Location VARCHAR(50);

---#
1️⃣ Create Tables
CREATE TABLE departments (
    dept_id INT PRIMARY KEY AUTO_INCREMENT,
    dept_name VARCHAR(100) NOT NULL
);

CREATE TABLE employees (
    emp_id INT PRIMARY KEY AUTO_INCREMENT,
    emp_name VARCHAR(100),
    salary DECIMAL(10,2),
    dept_id INT,
    hire_date DATE,
    FOREIGN KEY (dept_id) REFERENCES departments(dept_id)
);

-- # 2️⃣ Insert Sample Data
INSERT INTO departments (dept_name) VALUES
('HR'),
('IT'),
('Finance'),
('Sales');

INSERT INTO employees (emp_name, salary, dept_id, hire_date) VALUES
('John', 50000, 1, '2020-01-15'),
('Sarah', 75000, 2, '2019-03-20'),
('Mike', 60000, 2, '2021-07-10'),
('Anna', 45000, 1, '2022-02-01'),
('David', 80000, 3, '2018-11-25'),
('Robert', 70000, 4, '2020-06-30'),
('Emily', 65000, 2, '2021-09-12');

-- # 3️⃣ Slow Query (Without Index)
SELECT e.emp_name, e.salary, d.dept_name
FROM employees e
JOIN departments d ON e.dept_id = d.dept_id
WHERE e.salary > 60000;

-- # 4️⃣ Add Indexes (Optimization)
🔹 Index on salary (for WHERE clause)
CREATE INDEX idx_salary ON employees(salary);
🔹 Index on dept_id (for JOIN)
CREATE INDEX idx_dept_id ON employees(dept_id);

-- # 5️⃣ Check Performance Again
EXPLAIN SELECT e.emp_name, e.salary, d.dept_name
FROM employees e
JOIN departments d ON e.dept_id = d.dept_id
WHERE e.salary > 60000;

👉 Now you should see:

type = range (better than ALL)
key = idx_salary

That means index is being used ✅

-- # 6️⃣ Composite Index (Advanced Optimization)

If query frequently uses salary + dept_id:

CREATE INDEX idx_salary_dept ON employees(salary, dept_id);

--- # 7️⃣ Covering Index Example

If query only needs emp_name & salary:

CREATE INDEX idx_covering ON employees(salary, emp_name);

Query:

SELECT emp_name, salary
FROM employees
WHERE salary > 60000;

👉 MySQL can use index only (faster).

-- # ✅ 8️⃣ Avoid These (Bad Practices)

❌ Avoid this (index not used):

SELECT * FROM employees
WHERE YEAR(hire_date) = 2021;

✔ Better:

CREATE INDEX idx_hire_date ON employees(hire_date);

SELECT * FROM employees
WHERE hire_date BETWEEN '2021-01-01' AND '2021-12-31';

--- # 9️⃣ Force Index (Testing Only)
SELECT * FROM employees FORCE INDEX (idx_salary)
WHERE salary > 60000;

-- # 🔟 Check Existing Indexes
SHOW INDEX FROM employees;

























