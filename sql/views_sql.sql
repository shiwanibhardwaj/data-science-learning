create view view1 as 
select StudentID,StudentName from students;

select * from view1;

create view view2 as
select  StudentID,StudentName,ClassName from students
inner join classes
on students.ClassID=classes.ClassID;

select * from view2;
drop view view1;