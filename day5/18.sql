SELECT TOP 3
    p.ProductName, 
    SUM(od.UnitPrice * od.Quantity) AS TotalRevenue
FROM products p
JOIN Order Details od ON od.ProductID = p.ProductID
GROUP BY p.ProductName
ORDER BY TotalRevenue DESC;