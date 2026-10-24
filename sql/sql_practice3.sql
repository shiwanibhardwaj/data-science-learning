create database company_db;
show databases;
use company_db;

create table employees(
employee_id int primary key,
name varchar(100) not null,
department varchar(20) not null,
salary int not null default 12000,
age int constraint check (age >=18)
);
insert into employees values(1,"dune","block A",20000,23);
insert into employees (employee_id,name,department,salary,age)
values 
(2,"aksha","block c",21000,21),
(3,"divya","block b",24000,22),
(4,"mansi","block A",28000,24),
(5,"apurva","block b",56000,33),
(6,"shivani","block c",57000,31),
(7,"saurabh","block d",88000,40);

insert into employees (employee_id,name,department)
values 
(8,"tara", "block A");

desc employees;
select * from employees;

select name,salary from employees;
select distinct department from employees;
select salary from employees where salary>60000;
select salary from employees where salary<50000;
select salary from employees where salary=50000;
select salary from employees where salary between 50000 and 70000;
select name,department from employees where department='block A';
select name,department from employees where department in ("block A","block c");
select name,department from employees where department not in ("block A","block c");
select * from employees order by salary asc;
select * from employees order by salary desc;
select * from employees order by age asc;
select *from employees order by salary desc limit 3;
select *from employees order by salary asc limit 3;
select *from employees order by salary desc,department asc limit 3;
select count(*) from employees;
select sum(salary) from employees;
select avg(salary) from employees;
select min(salary) from employees;
select max(salary) from employees;
select avg(age) from employees;
select count(*) from employees where department='block A';
select department,count(*) from employees group by department;
select department,avg(salary) from employees group by department;
select department,sum(salary) from employees group by department;
select department,avg(age) from employees group by department;
select department from employees group by department having count(*)>2;
