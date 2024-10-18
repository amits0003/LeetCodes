--Write a solution to find the nth highest salary from the Employee table. If there is no nth highest salary, return null.

--The result format is in the following example.
--+------------------------+
--| getNthHighestSalary(2) |
--+------------------------+
--| 200                    |
--+------------------------+


CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
SET N = N-1;
RETURN
(
    SELECT DISTINCT(salary) from Employee order by salary desc limit 1 OFFSET N
);
END
