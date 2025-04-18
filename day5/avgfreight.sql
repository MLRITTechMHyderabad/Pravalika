use w3schools;
SELECT CustomerID, AVG(Freight) AS AverageFreight
FROM Orders
GROUP BY CustomerID;