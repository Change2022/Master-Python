-- Autor: Roberto Jaime Rico Sandoval.
-- File: Practica1.
-- Des: Funciones en SQL parte 1.
-- Version and fechone: V.0.0.1 -- 03/ 12/ /2021  

/*
** FUNCIONES PREDETERMINADAS:

CREATE FUNCTION = Crear una nueva función.
@ = Nombramiento de variables.
Return / returns = Para retornar un valor.
DECLARE = Para declarar una variable.
SET = Para modificar o actualziar el valor de una variable.
AS = Modificar o actualizar el valor de una variable, desde una consulta.

** TIPOS DE DATOS:
money = Número decimal con separación de una coma.

** ESTRUCTURA PARA CÓDIGO COMPILABLE:
AS > BEGIN > END

*/

-- Crear una función escalar en SQL.

CREATE FUNCTION CalculoIVA (@Price money) RETURNS money
AS
BEGIN
    DECLARE @IVA money
    SET @IVA = @Price * 1.16
    RETURN @IVA
END

-- Realizar una consulta en la base de datos (Extracción de datos / ETL).

SELECT ProductID, ProductName, UnitPrice, dbo, CalculoIVA (UnitPrice) As IVA FROM Product

