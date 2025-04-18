use w3schools;
SELECT Notes, COUNT(*) AS Count
FROM Employees
GROUP BY Notes
HAVING COUNT(*) > 1;