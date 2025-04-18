WITH YearlyMaxFreight AS (
    SELECT 
        YEAR(OrderDate) AS OrderYear,
        MAX(Freight) AS MaxFreight
    FROM Orders
    GROUP BY YEAR(OrderDate)
)
SELECT o.OrderID, o.OrderDate, o.Freight
FROM Orders o
JOIN YearlyMaxFreight y ON 
    YEAR(o.OrderDate) = y.OrderYear AND 
    o.Freight = y.MaxFreight;