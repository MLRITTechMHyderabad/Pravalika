SELECT FirstName, COUNT(*) AS Occurrences
FROM Employees
GROUP BY FirstName
HAVING COUNT(*) > 1;