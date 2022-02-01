-- Autor: Roberto Jaime Rico Sandoval.
-- File: Practica2.
-- Des: Funciones en SQL parte 2.
-- Version and fechone: V.0.0.1 -- 03/ 12/ /2021  

/*
** FUNCIONES PREDETERMINADAS:

INSERT INTO = Inserta datos en la tabla (Carga / ETL)
Table = Para señalar a una tabla dentro de la base de datos.
FROM = Trabajar un dato desde un punto exacto de la base de datos.
WHERE = Condicional dentro del código compilable en SQL.

** TIPOS DE DATOS:

Char = Tipo carácteres.
*/

-- Creación de función en línea.
CREATE FUNCTION ContryCunstomers (@Contry char (15)) RETURNS table
RETURN (SELECT CustomerID, CompanyName, Country FROM Customers
        WHERE Country = @Country)


-- Creación de función en múltiple línea.
CREATE FUNCTION ContryCunstomers2 (@Contry char (15))
RETURNS @TableCountry table (ConsumerID char (5),
                             CompanyName char (40),
                             ContacName char (30).
                             Country char (15))

BEGIN
    INSERT INTO @TableCountry
    SELECT CustomerID, CompanyName, ContactName, Country FROM Customers
    WHERE Country = @Country
    RETURN
END

