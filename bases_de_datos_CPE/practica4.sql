-- Autor: Roberto Jaime Rico Sandoval.
-- File: práctica 4.
-- Des: Proceso de almacenamientos parte 1.
-- Version and fechone: V.0.0.1 -- 03/ 12/ /2021  

CREATE PROCEDURE CostumerContry
AS
    SELECT * FROM Customers
    WHERE CostumerContry = "México"
GO

