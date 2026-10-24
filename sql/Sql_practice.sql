show databases;
use hospital_db;
desc appointments;
desc departments;
desc doctors;
desc patients;
desc bills;
select * from departments;

insert into  doctors() 
values
(1,"Rajesh Sharma",1,12,150000),
(2,"Priya Mehta",2,8,120000),
(3,"Amit Verma",3,15,175000),
(4,"Neha Kapoor",4,6,95000),
(5,"Ankit Singh",5,10,110000),
(6,"Sneha Rao",6,7,100000),
(7,"Kavita Jain",1,5,90000);
select *from doctors;
select Department_ID,count(ExperienceYears) from doctors group by (Department_ID);
select Department_ID,max(ExperienceYears) from doctors group by (Department_ID);
select Department_ID,avg(ExperienceYears) from doctors group by (Department_ID);
select Department_ID,min(ExperienceYears) from doctors group by (Department_ID);
select Department_ID,sum(ExperienceYears) from doctors group by (Department_ID);

insert into patients() 
values 
(1,"Rahul Kumar",28,"Male","Delhi"),
(2,"Ananya Sharma",35,"Female","Noida"),
(3,"Mohit Verma",42,"Male","Delhi"),
(4,"Priya Singh",25,"Female","Gurgaon"),
(5,"Riya Gupta",31,"Female","Delhi"),
(6,"Arjun Mehta",50,"Male","Ghaziabad"),
(7,"Simran Kaur",19,"Female","Delhi"),
(8,"Karan Malhotra",45,"Male","Noida"),
(9,"Sneha Kapoor",33,"Female","Delhi"),
(10,"Aman Jain",60,"Male","Gurgaon");
select *from patients;
select Patient_Name,Age from patients;
select Patient_Name,Age,Gender from patients where Age>40;
select Patient_Name,Age,Gender from patients where Age between 20 and 40;
select Patient_Name,Age,Gender from patients where (Age between 20 and 40) and (Gender="Male");
select Patient_Name,Age,Gender,City  from patients where City in("Delhi","Noida") limit 4;
select * from patients order by Age desc;

insert into appointments(Appointment_ID,Patient_ID,Doctor_ID,Appointment_Date,Status) 
values 
(1,2,4,"2026-01-05","Completed"),
(2,1,3,"2026-02-06","Completed"),
(3,6,1,"2026-01-12","Completed"),
(4,2,1,"2026-02-08","Completed"),
(5,3,5,"2026-02-08","Completed"),
(6,2,1,"2026-02-10","Completed"),
(7,1,2,"2026-03-02","Completed");
select *from appointments;
select distinct Patient_ID from appointments;
select Doctor_ID,count(Patient_ID) from appointments group by (Doctor_ID) having count(Patient_ID)>1;

update appointments set Patient_ID=3 where Patient_ID=1;
delete from appointments where Appointment_ID=7;

alter table appointments add column Patient_Name varchar(100) not null;
alter table appointments drop column  Patient_Name ;

alter table appointments rename to appointment;
select *from appointment;

alter table appointment rename to appointments;
select *from appointments;

alter table patients change City Patients_city varchar(100) not null;
select *from patients;

alter table departments add column city int not null;
alter table departments modify city varchar(100) not null;
select * from departments;
desc departments;

create table status(
show_status varchar(100) not null
);
insert into status values("completed");
select * from status;
truncate table status;