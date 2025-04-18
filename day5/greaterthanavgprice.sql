SELECT ProductName, UnitPrice
FROM Products
WHERE UnitPrice > (
    SELECT AVG(UnitPrice) * 3
    FROM Products
);