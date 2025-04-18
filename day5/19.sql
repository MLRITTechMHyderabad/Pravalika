SELECT 
    e.EmployeeID, 
    e.FirstName, 
    e.LastName, 
    COUNT(DISTINCT o.CustomerID) AS CustomerCount
FROM Employees e
JOIN Orders o ON e.EmployeeID = o.EmployeeID
GROUP BY e.EmployeeID, e.FirstName, e.LastName;