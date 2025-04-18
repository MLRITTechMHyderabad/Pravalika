SELECT 
    c.CustomerID, 
    c.CompanyName, 
    e.FirstName, 
    e.LastName
FROM Customers c
JOIN Orders o ON c.CustomerID = o.CustomerID
JOIN Employees e ON o.EmployeeID = e.EmployeeID;