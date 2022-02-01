-- Autor: Roberto Jaime Rico Sandoval.
-- File: Triggers.
-- Des: Creación de Triggers.
-- Version and fechone: V.0.0.1 -- 03/ 12/ /2021  

/*
** FUNCIONES PREDETERMINADAS:

TRIGGER = Tokken (Proteción), para la base de datos.
ON = Sobre una tabla trabajar.

** ESTRUCTURA AFTER:
DML (Funciones predeterminadas) > TRIGGER

** ESTRUCTURA FOR:
TRIGGER > DML (Funciones predeterminadas)

** TIPOS DE DATOS:

int = Números enteros.
smallint = Números enteros exactos delimitados al número 32000 -32000 (2 bytes).

*/ 

CREATE TRIGGER StockUpdate
ON (OrderDetails)
FOR INSERT
AS
BEGIN
    DECLARE @Cantidad smallint, @ProductID int, @Stock smallint
    SELECT @Cantidad = Quantity, @ProductID = ProductID FROM inserted
    SELECT @Stock = UnitsinStock FROM Products WHERE @ProductID = ProductID
    UPDATE Products SET UnitsinStock = @Stock - @Cantidad WHERE ProductID = @ProductID
END

