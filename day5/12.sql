SELECT 
    p.ProductName, 
    s.CompanyName AS SupplierName, 
    c.CategoryName
FROM Products p
JOIN Suppliers s ON p.SupplierID = s.SupplierID
JOIN Categories c ON p.CategoryID = c.CategoryID;