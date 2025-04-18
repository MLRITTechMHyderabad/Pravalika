SELECT 
    c.CustomerID, 
    c.CompanyName, 
    COUNT(o.OrderID) AS TotalOrders
FROM Customers c
JOIN Orders o ON c.CustomerID = o.CustomerID
GROUP BY c.CustomerID, c.CompanyName
ORDER BY TotalOrders DESC;