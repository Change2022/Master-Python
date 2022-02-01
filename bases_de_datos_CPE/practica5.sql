-- Autor: Roberto Jaime Rico Sandoval.
-- File: práctica 5.
-- Des: Proceso de almacenamientos parte 2.
-- Version and fechone: V.0.0.1 -- 03/ 12/ /2021  

CREATE PROCEDURE insertConsumers_ContryUpdate @CustomerID nchar(5), @CompanyName nchar(5), @ReturnID nchar(5) OUTPUT
AS
BEGIN
    INSERT INTO Customers (CustomerID, CompanyName) VALUES (CustomerID, @CompanyName)
    IF (@@ERROR <> 0)
        BEGIN
            UPDATE Customers
            SET Customers, CustomerID = @CustomerID
            Customers, CompanyName = @CompanyName
            WHERE Customers, CustomerID = @CustomerID
            PRINT("Se realizo un UPDATE")
        END
    ELSE
        BEGIN
            PRINT("Se realizo un INSERT")
        END
        SELECT @ReturnID = @CustomerID FROM Customers WHERE Customers, CustomerID = @CustomerID
END

DECLARE @back nchar(5)
EXECUTE insertConsumers_ContryUpdate "ABA", "Puzzle", @back OUTPUT
SELECT @back

