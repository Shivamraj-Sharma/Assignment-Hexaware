CREATE DATABASE test1;
USE test1;

-- Creating Vehicle Table

CREATE TABLE Vehicle (
    vehicleID INT PRIMARY KEY,
    make VARCHAR(100),
    model VARCHAR(100),
    year INT,
    dailyRate DECIMAL(10, 2),
    status VARCHAR(50),
    passengerCapacity INT,
    engineCapacity INT
);


-- Creating Customers Table

CREATE TABLE Customer (
    customerID INT PRIMARY KEY,
    firstName VARCHAR(100),
    lastName VARCHAR(100),
    email VARCHAR(100),
    phoneNumber VARCHAR(20)
);


-- Creating Lease Table

CREATE TABLE Lease (
    leaseID INT PRIMARY KEY,
    vehicleID INT,
    customerID INT,
    startDate DATE,
    endDate DATE,
    type VARCHAR(20),
    FOREIGN KEY (vehicleID) REFERENCES Vehicle(vehicleID),
    FOREIGN KEY (customerID) REFERENCES Customer(customerID)
);


-- Creating Payments Table

CREATE TABLE Payment (
    paymentID INT PRIMARY KEY,
    leaseID INT,
    paymentDate DATE,
    amount DECIMAL(10, 2),
    FOREIGN KEY (leaseID) REFERENCES Lease(leaseID)
);


-- Inserting Values in Vehicle Table

INSERT INTO Vehicle (vehicleID, make, model, year, dailyRate, status, passengerCapacity, engineCapacity) 
VALUES 
(1, 'Toyota', 'Camry', 2022, 50.00, 'available', 4, 1450),
(2, 'Honda', 'Civic', 2023, 45.00, 'available', 7, 1500),
(3, 'Ford', 'Focus', 2022, 48.00, 'not available', 4, 1400),
(4, 'Nissan', 'Altima', 2023, 52.00, 'available', 7, 1200),
(5, 'Chevrolet', 'Malibu', 2022, 47.00, 'available', 4, 1800),
(6, 'Hyundai', 'Sonata', 2023, 49.00, 'not available', 7, 1400),
(7, 'BMW', '3 Series', 2023, 60.00, 'available', 7, 2499),
(8, 'Mercedes', 'C-Class', 2022, 58.00, 'available', 8, 2599),
(9, 'Audi', 'A4', 2022, 55.00, 'not available', 4, 2500),
(10, 'Lexus', 'ES', 2023, 54.00, 'available', 4, 2500);
-- SELECT * FROM Vehicle;


-- Inserting Values in Vehicle Table

INSERT INTO Customer(customerID, firstName, lastName, email, phoneNumber)
VALUES
(1, 'John', 'Doe', 'johndoe@example.com', '555-555-5555'),
(2, 'Jane', 'Smith', 'janesmith@example.com', '555-123-4567'),
(3, 'Robert', 'Johnson', 'robert@example.com', '555-789-1234'),
(4, 'Sarah', 'Brown', 'sarah@example.com', '555-456-7890'),
(5, 'David', 'Lee', 'david@example.com', '555-987-6543'),
(6, 'Laura', 'Hall', 'laura@example.com', '555-234-5678'),
(7, 'Michael', 'Davis', 'michael@example.com', '555-876-5432'),
(8, 'Emma', 'Wilson', 'emma@example.com', '555-432-1098'),
(9, 'William', 'Taylor', 'william@example.com', '555-321-6547'),
(10, 'Olivia', 'Adams', 'olivia@example.com', '555-765-4321');
-- SELECT * FROM Customer;


-- Inserting Values in Lease Table

INSERT INTO Lease (leaseID, vehicleID, customerID, startDate, endDate, type)
VALUES
(1, 1, 1, '2023-01-01', '2023-01-05', 'Daily'),
(2, 2, 2, '2023-02-15', '2023-02-28', 'Monthly'),
(3, 3, 3, '2023-03-10', '2023-03-15', 'Daily'),
(4, 4, 4, '2023-04-20', '2023-04-30', 'Monthly'),
(5, 5, 5, '2023-05-05', '2023-05-10', 'Daily'),
(6, 4, 3, '2023-06-15', '2023-06-30', 'Monthly'),
(7, 7, 7, '2023-07-01', '2023-07-10', 'Daily'),
(8, 8, 8, '2023-08-12', '2023-08-15', 'Monthly'),
(9, 3, 3, '2023-09-07', '2023-09-10', 'Daily'),
(10, 10, 10, '2023-10-10', '2023-10-31', 'Monthly');
-- SELECT * FROM Lease;


-- Inserting Values in Payment Table

INSERT INTO Payment (paymentID, leaseID, paymentDate, amount)
VALUES
(1, 1, '2023-01-03', 200.00),
(2, 2, '2023-02-20', 1000.00),
(3, 3, '2023-03-12', 75.00),
(4, 4, '2023-04-25', 900.00),
(5, 5, '2023-05-07', 60.00),
(6, 6, '2023-06-18', 1200.00),
(7, 7, '2023-07-03', 40.00),
(8, 8, '2023-08-14', 1100.00),
(9, 9, '2023-09-09', 80.00),
(10, 10, '2023-10-25', 1500.00);
-- SELECT * FROM Payment;


-- SQL Queries

-- 1. update the daily rate for a Mercedes car to 68. 
UPDATE Vehicle
SET dailyRate = 68
WHERE make = 'mercedes';

-- 2. delete a specific customer and all associated leases and payments.
DECLARE @cust INT;
SELECT @cust = customerID FROM Customer WHERE firstName = 'Sarah' AND lastName = 'Brown';

DELETE FROM Payment WHERE leaseID IN (SELECT leaseID FROM Lease WHERE customerID = @cust);
DELETE FROM Lease WHERE customerID = @cust;
DELETE FROM Customer WHERE customerID = @cust;

-- 3. rename the "paymentDate" column in the Payment table to "transactionDate". 
EXEC sp_rename 'Payment.paymentDate', 'transactionDate';
--SELECT * FROM Payment;

-- 4. find a specific customer by email. 
SELECT * FROM Customer
WHERE email = 'laura@example.com'; 

-- 5. get active leases for a specific customer. 
DECLARE @D DATE;
SELECT @D = GETDATE();

SELECT c.customerID, CONCAT(c.firstName, ' ', c.lastName) AS fullName,
       l.leaseID, l.vehicleID, l.startDate, l.endDate, l.type
FROM Lease l INNER JOIN Customer c
ON l.customerID = c.customerID
WHERE  c.firstName = 'Robert' AND c.lastName = 'Johnson' AND endDate >= @D;

-- 6. find all payments made by a customer with a specific phone number. 
SELECT * FROM Payment
WHERE leaseID = ANY(SELECT leaseID 
				 FROM Lease l INNER JOIN Customer c
				 ON l.customerID = c.customerID
				 WHERE c.phoneNumber = '555-789-1234');

-- 7. calculate the average daily rate of all available cars. 
SELECT AVG(dailyRate) AS avg_dailyRate
FROM Vehicle
WHERE status = 'available';

-- 8. find the car with the highest daily rate. 
SELECT * FROM Vehicle
WHERE dailyRate >= ALL(SELECT dailyRate FROM Vehicle);

-- 9. retrieve all cars leased by a specific customer. 
SELECT v.* FROM Vehicle v
WHERE v.vehicleID = ANY(SELECT l.vehicleID 
						FROM lease l INNER JOIN Customer c
						ON l.customerID = c.customerID
						WHERE c.firstName = 'Robert' AND c.lastName = 'Johnson');

-- 10. find the details of the most recent lease.
SELECT * FROM Lease
WHERE startDate = (SELECT MAX(startDate) FROM Lease);

-- 11. list all payments made in the year 2023.
SELECT * FROM Payment 
WHERE YEAR(transactionDate) = 2023;

-- 12. retrieve customers who have not made any payments.
SELECT * FROM Customer
WHERE customerID NOT IN(SELECT c.customerID 
						FROM Customer c INNER JOIN Lease l 
						ON c.customerID = l.customerID INNER JOIN Payment p 
						ON l.leaseId = p.leaseID);

-- 13. retrieve Car Details and Their Total Payments.
SELECT v.*, COALESCE(SUM(p.amount), 0) AS totalPayments
FROM Vehicle v
LEFT JOIN Lease l ON v.vehicleID = l.vehicleID
LEFT JOIN Payment p ON l.leaseID = p.leaseID
GROUP BY v.vehicleID, v.make, v.model, v.year, v.dailyRate, v.status, v.passengerCapacity, v.engineCapacity;

-- 14. calculate Total Payments for Each Customer. 
SELECT c.*, COALESCE(SUM(p.amount), 0) AS totalPayments
FROM Customer c
LEFT JOIN Lease l ON c.customerID = l.customerID
LEFT JOIN Payment p ON l.leaseID = p.leaseID
GROUP BY c.customerID, c.firstName, c.lastName, c.email, c.phoneNumber;

-- 15. List Car Details for Each Lease. 
SELECT l.leaseID,l.startDate, l.endDate,
	   v.vehicleID, v.make, v.model, v.year, v.dailyRate
FROM Lease l
JOIN Vehicle v ON l.vehicleID = v.vehicleID; 

-- 16. Retrieve Details of Active Leases with Customer and Car Information. 
SELECT l.*, CONCAT(c.firstName,' ', c.lastName) AS fullName,
	   v.make, v.model, v.year, v.dailyRate
FROM Lease l
JOIN Customer c ON l.customerID = c.customerID
JOIN Vehicle v ON l.vehicleID = v.vehicleID
WHERE l.endDate >= GETDATE();

-- 17. find the Customer Who Has Spent the Most on Leases.
SELECT TOP 1 * 
FROM (SELECT CONCAT(c.firstName, ' ', c.lastName) AS fullName, COALESCE(SUM(p.amount), 0) AS totalPayments
	 FROM Customer c
	 LEFT JOIN Lease l ON c.customerID = l.customerID
	 LEFT JOIN Payment p ON l.leaseID = p.leaseID
	 GROUP BY c.customerID, c.firstName, c.lastName, c.email, c.phoneNumber) AS s
ORDER BY totalPayments DESC;

-- 18. list All Cars with Their Current Lease Information. 
SELECT v.vehicleId, v.make, v.model,
	   l.startDate, l.endDate, l.type, 
	   CONCAT(c.firstName, ' ', c.lastName) AS fullName
FROM Vehicle v
LEFT JOIN Lease l ON v.vehicleID = l.vehicleID
LEFT JOIN Customer c ON l.customerID = c.customerID;

