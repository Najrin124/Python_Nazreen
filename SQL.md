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












