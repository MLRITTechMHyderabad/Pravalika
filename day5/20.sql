SELECT 
    c.CategoryName, 
    COUNT(p.ProductID) AS ProductCount, 
    AVG(p.UnitPrice) AS AveragePrice
FROM Categories c
JOIN Products p ON c.CategoryID = p.CategoryID
GROUP BY c.CategoryName
ORDER BY ProductCount DESC;