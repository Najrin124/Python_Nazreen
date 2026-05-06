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
