SELECT 
    e.EmployeeID, 
    e.FirstName, 
    e.LastName, 
    COUNT(o.OrderID) AS OrderCount
FROM Employees e
LEFT JOIN Orders o ON e.EmployeeID = o.EmployeeID
GROUP BY e.EmployeeID, e.FirstName, e.LastName
ORDER BY OrderCount DESC;