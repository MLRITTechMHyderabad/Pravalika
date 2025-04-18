SELECT ProductName, UnitPrice
FROM Products p
WHERE UnitPrice > (
    SELECT AVG(UnitPrice)
    FROM Products
    WHERE CategoryID = p.CategoryID
);