-- Autor: Roberto Jaime Rico Sandoval.
-- File: práctica 7.
-- Des: Consultas Distinct.
-- Version and fechone: V.0.0.1 -- 03/ 12/ /2021 


-- Distinct.
SELECT [Order Details], ProductID, Products, ProductName
FROM [Order Details[]

INNER JOIN Orders ON [Order Details], OrderID = Orders, OrderID
INNER JOIN Orders ON [Order Details], ProductID = Products, ProductID

WHERE OrderDate >= "04-07-1996"
AND OrderDate <= "05-07-1996"
ORDER BY [Order Details], ProductID

SELECT Distinct [Order Details], ProductID, Products, ProductName
FROM [Order Details]
INNER JOIN Orders ON [Order Details], OrderID = Orders, OrderID
INNER JOIN Orders ON [Order Details], ProductID = Products, ProductID


-- Subconsulta.
SELECT Distinct [Order Details], ProductID, Products, ProductName FROM [Order Details]
INNER JOIN Products ON [Order Details], ProductID = Products, ProductID
WHERE "USA" IN (SELECT Country FROM Suppliers
                WHERE Products, SuppliersID = Suppliers, SuppliersID FROM Suppliers)
AND ProductName LIKE "L%"


-- INTO.
SELECT campo1, campo2, campo3
INTO nuevatabla
FROM dbo.categorias

IF OBJECT_iD("Customer") IS NOT NULL
BEGIN
    DROP TABLE CustomerCopy
END

SELECT CustomerID, CompanyName
INTO CustomerCopy
FROM Customer


-- GROUP BY.
SELECT campo1, campo3 FROM tabla1
INNER JOIN tabla2 ON Tabla1, campo1 = tabla4, campo6
GROUP BY campo1 ORDER BY Campo3

