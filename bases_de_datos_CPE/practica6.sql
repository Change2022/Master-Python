-- Autor: Roberto Jaime Rico Sandoval.
-- File: práctica 6.
-- Des: transacciones en SQL.
-- Version and fechone: V.0.0.1 -- 03/ 12/ /2021 

BEGIN TRANSACTION
    UPDATE Customers SET PostalCOde = 16090 WHERE CustomerID = "AAAA"
    INSERT INTO Customer (CustomerID, CompanyName) VALUES ("AAAA", "Pera")

    IF (@@ERROR <> 0)
        BEGIN
        ROLLBACK
        PRINT("Error.")
        END
    ELSE
        BEGIN
        COMMIT
        PRINT("Bien.")
        END

        