create database if not exists collage;
use collage;

create table Teacher(
id int primary key,
name varchar(100)not null,
subject varchar(100) not null,
salary int not null
);

insert into Teacher 
values
(1,"ajay", "math",50000),
(2,"ajay", "math",50000),
(3,"bharat", "english",50000),
(4,"chetan", "chemistry",50000),
(5,"divya", "physics",50000);
select *from teacher;
 
update Teacher set salary=80000 where id=5;
select salary from Teacher where salary > 55000; 
alter table Teacher change column salary ctc int not null;
update Teacher set ctc=ctc + ctc *0.25;
SET SQL_SAFE_UPDATES = 0;

alter table teacher add column city varchar(100) not null default "gurgaon";
alter table teacher drop ctc;




create table student(
roll_no int primary key,
name varchar(100)not null,
city varchar(100) not null,
marks int not null
);

insert into student 
values 
(1,"adam","noida",76),
(2,"bob","mumbai",65),
(3,"casey","pune",89),
(4,"duke","varanasi",93);
select *from student;
select * from student where marks>75;
select distinct city from student;
select city, max(marks) from student group by(city);
select avg(marks) from student group by(city);
alter table student add column grade varchar(4) ;
update student set grade="O" where marks>=80;
update student set grade="A" where marks>=70 and marks<80;
update student set grade="B" where marks>=60 and marks<70;


create table Employee(
EmpID int primary key,
FirstName varchar(50) not null,
LastName varchar(20) not null,
Department varchar(20)not null,
Salary int not null,
HireDate date not null
);

insert into Employee 
values
(101, 'Alice', 'Johnson', 'IT', 6500, '2020-03-15'),
(102, 'Mark', 'Rivera', 'HR', 4800, '2019-07-22'),
(103, 'Sophia', 'Lee', 'Finance', 7200, '2021-01-10'),
(104, 'Daniel', 'Kim', 'IT', 5800, '2018-11-05'),
(105, 'Emma', 'Brown', 'Marketing', 5300, '2022-04-18'),
(106, 'Liam', 'Patel', 'Finance', 6900, '2020-09-29'),
(107, 'Olivia', 'Garcia', 'HR', 4600, '2017-06-30'),
(108, 'Noah', 'Thompson', 'IT', 7500, '2023-02-12'),
(109, 'Ava', 'Martinez', 'Marketing', 5100, '2019-12-02'),
(110, 'Ethan', 'Davis', 'Finance', 8000, '2016-05-14');

select * from employee;
select FirstName,LastName,Salary from employee;
select *from employee where Department="IT";
select *from employee where salary> 6000;
select *from employee order by HireDate desc;
select distinct department from employee;
select *from employee where FirstName like 'A%';  
select *from employee where salary between 4000 and 7000;
select avg(salary) from employee;
select department, count(*) from employee group by(department) having count(*)>2;

select @@autocommit;
set @@autocommit=0;

start transaction;
update Employee set salary=salary-1000 where EmpID=101;
rollback;
update Employee set salary=salary+1000 where EmpID=102;
rollback;


start transaction;
update Employee set salary=salary-1000 where EmpID=103;
commit;
update Employee set salary=salary-1000 where EmpID=104;
rollback;

begin;
savepoint updation1;
update employee set increments=increments+1000 where EmpID=101;
savepoint updation;
update employee set increments=increments+2000 where EmpID=102;
rollback to updation1;
rollback to updation;
commit;
