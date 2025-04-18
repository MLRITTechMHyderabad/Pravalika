SELECT DISTINCT 
    c.CustomerID, 
    c.CompanyName, 
    p.ProductName
FROM Customers c
JOIN Orders o ON c.CustomerID = o.CustomerID
JOIN Order_Details od ON o.OrderID = od.OrderID
JOIN Products p ON od.ProductID = p.ProductID
WHERE p.ProductName = 'Tofu';