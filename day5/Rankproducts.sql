SELECT ProductName, SupplierID, UnitPrice,
       RANK() OVER (PARTITION BY SupplierID ORDER BY UnitPrice DESC) AS PriceRank
FROM Products;