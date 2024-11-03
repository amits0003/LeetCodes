--Table: Logs
--
--+-------------+---------+
--| Column Name | Type    |
--+-------------+---------+
--| id          | int     |
--| num         | varchar |
--+-------------+---------+
--In SQL, id is the primary key for this table.
--id is an autoincrement column starting from 1.
--
--
--Find all numbers that appear at least three times consecutively.
--
--Return the result table in any order.
--
--The result format is in the following example.
--
--
--
--Example 1:
--
--Input:
--Logs table:
--+----+-----+
--| id | num |
--+----+-----+
--| 1  | 1   |
--| 2  | 1   |
--| 3  | 1   |
--| 4  | 2   |
--| 5  | 1   |
--| 6  | 2   |
--| 7  | 2   |
--+----+-----+
--Output:
--+-----------------+
--| ConsecutiveNums |
--+-----------------+
--| 1               |
--+-----------------+
--Explanation: 1 is the only number that appears consecutively for at least three times.


-- # Write your MySQL query statement below
-- WITH RankedLogs AS
-- (Select num, ROW_NUMBER() OVER (ORDER BY id) - ROW_NUMBER() OVER (PARTITION BY num ORDER BY id) as grp from Logs WHERE id IS NOT NULL AND num IS NOT NULL AND id <> '' AND num <> ''),
-- ConsecutiveGroups AS
-- (Select num, COUNT(*) AS count1 from RankedLogs GROUP BY num, grp having COUNT(*) >= 3 )
-- select COUNT(*) as ConsecutiveNums from ConsecutiveGroups;

WITH cte as
(select num,
lead(num, 1) over() num1,
lead(num, 2) over() num2
from Logs)
select distinct num ConsecutiveNums from cte where (num = num1) and (num = num2)
