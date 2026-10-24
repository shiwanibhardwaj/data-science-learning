CREATE TABLE classes (
    ClassID INT PRIMARY KEY,
    ClassName VARCHAR(20) NOT NULL,
    TeacherName VARCHAR(50),
    RoomNo INT
);

INSERT INTO classes VALUES
(101, 'Class 8', 'Mr. Sharma', 201),
(102, 'Class 9', 'Mrs. Verma', 202),
(103, 'Class 10', 'Mr. Singh', 203),
(104, 'Class 11', 'Ms. Gupta', 204),
(105, 'Class 12', 'Mr. Kumar', 205);


CREATE TABLE students (
    StudentID INT PRIMARY KEY,
    StudentName VARCHAR(50) NOT NULL,
    Age INT,
    City VARCHAR(50),
    ClassID INT,
    FOREIGN KEY (ClassID) REFERENCES classes(ClassID)
);

INSERT INTO students VALUES
(1, 'Aarav', 13, 'Delhi', 101),
(2, 'Priya', 14, 'Patna', 102),
(3, 'Rahul', 15, 'Delhi', 103),
(4, 'Ananya', 16, 'Lucknow', 104),
(5, 'Rohan', 17, 'Patna', 105),
(6, 'Sneha', 14, 'Delhi', 102),
(7, 'Amit', 15, 'Jaipur', 103),
(8, 'Neha', 13, 'Mumbai', NULL);

#Display each student's name along with their class name.
select StudentID,StudentName,ClassName from students
inner join classes 
on students.ClassID=classes.ClassID;

#Display all students, including students without an assigned class.
select StudentID,StudentName,ClassName from students
left join classes 
on students.ClassID=classes.ClassID;
#Display all classes, including classes with no students.

select StudentID,StudentName,ClassName from students
right join classes 
on students.ClassID=classes.ClassID;


#Display student names, teacher names, and room numbers.
select StudentName,TeacherName,RoomNo from Students
join classes
on students.ClassID=classes.ClassID;

#Display students who belong to Class 9.
select * from Students
join classes
on students.ClassID=classes.ClassID where classes.ClassName="Class 9";

#Count the number of students in each class.
select ClassName,count(students.ClassID) from students
left join classes
on students.ClassID=classes.ClassID
group by(ClassName);

#Find students who have not been assigned a class.(it is also called exclusive left join.)
select * from students
left join classes 
on students.ClassID=classes.ClassID where students.classID is null;


#Find classes that have no students.(it is also called exclusive right join.)
select *from students
right join classes 
on students.ClassID=classes.ClassID where classes.classID is null;

