SELECT TOP 5 
    c.CustomerID, 
    c.CompanyName, 
    SUM(o.Freight) AS TotalFreight
FROM Customers c
JOIN Orders o ON c.CustomerID = o.CustomerID
GROUP BY c.CustomerID, c.CompanyName
ORDER BY TotalFreight DESC;