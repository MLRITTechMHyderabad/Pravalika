SELECT ProductName, UnitPrice
FROM Products
WHERE UnitPrice = (
    SELECT MAX(UnitPrice)
    FROM Products
    WHERE UnitPrice < (
        SELECT MAX(UnitPrice)
        FROM Prouducts));