-- Write a SQL query to calculate the average salary of employees in each department and display the average 
-- salary along with the details of each employee in that department, ordered by the employee's salary in descending order.


-- Q1) Write a query to rank employees within each department based on their salary in descending order.

SELECT
    emp_name,
    emp_dep,
    emp_id,
    dep_id,
    salary,
    RANK() OVER (PARTITION BY dep_id ORDER BY salary DESC) AS ranking
FROM employee;

-- Q2) Write a query to calculate the dense rank of employees based on their salary in descending order.

SELECT
    emp_name,
    emp_dep,
    emp_id,
    dep_id,
    salary,
    DENSE_RANK() OVER (ORDER BY salary DESC) AS dense_ranking

FROM employee;    

-- Q3)
-- You are given a database schema with two tables: salesperson and region. 
-- The salesperson table contains information about salespeople, including their 
-- salesperson_id, first_name, last_name, salary, and region_id. The region table 
-- contains information about regions, including their region_id and region_name.Write a 
-- SQL query to calculate the average salary of salespeople in each region and display the 
-- average salary along with the details of each salesperson in that region, ordered by the salesperson's salary in descending order.

SELECT
    s.salesperson_id,
    s.first_name,
    s.last_name,
    s.salary,

    AVG(s.salary) OVER (PARTITION BY r.region_id) AS avg_sal_region

    FROM salesperson s

    JOIN region r ON s.region_id = r.region_id

    ORDER BY

    r.region_id,
    s.salary DESC;

-- Q4)
-- You are given a database schema with two tables: student and course. 
-- The student table contains information about students, including their student_id, 
-- first_name, last_name, and course_id. The course table contains information about courses,
--  including their course_id, course_name, and department_id.Write a SQL query to calculate the average 
--  GPA of students in each department and display the average 
-- GPA along with the details of each student in that department, ordered by 
-- the student's GPA in descending order.


WITH student_avg_gpa AS (
    SELECT
        s.student_id,
        s.first_name,
        s.last_name,
        s.gpa,
        c.department_id,
        AVG(s.gpa) OVER (PARTITION BY c.department_id) AS avg_gpa_department
    FROM
        student s
    JOIN course c ON s.course_id = c.course_id
)
SELECT
    sag.student_id,
    sag.first_name,
    sag.last_name,
    sag.gpa,
    sag.department_id,
    sag.avg_gpa_department
FROM
    student_avg_gpa sag
ORDER BY
    sag.department_id,
    sag.gpa DESC;



-- Q5)
-- You are given a database schema with two tables: employee and department. 
-- The employee table contains information about employees, including their employee_id, first_name,
--  last_name, salary, and department_id. The department table contains information about departments, 
--  including their department_id and department_name.Write a SQL query to calculate the total salary budget for 
--  each department (i.e., the sum of salaries of all employees in that department) and display the total salary budget along 
-- with the details of each employee in that department, ordered by the employee's salary in descending order.


WITH total_sal_each_dep AS (
    SELECT
        e.employee_id,
        e.first_name,
        e.last_name,
        e.salary,
        e.department_id,

        SUM(e.salary) OVER (PARTITION BY e.department_id) AS total_sal

        FROM employee e

        JOIN  department d ON e.department_id = d.department_id
 
)
SELECT
    tsed.employee_id,
    tsed.first_name,
    tsed.last_name,
    tsed.department_id,
    tsed.total_sal
FROM
    total_sal_each_dep tsed
ORDER BY
    tsed.department_id,
    tsed.total_sal DESC;


