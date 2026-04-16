-- 1. Create Tables

CREATE TABLE Partners (
    partner_id INT PRIMARY KEY,
    partner_name VARCHAR(50)
);

CREATE TABLE Shipments (
    shipment_id INT PRIMARY KEY,
    partner_id INT,
    destination_city VARCHAR(50),
    order_date DATE,
    promised_date DATE,
    actual_delivery_date DATE,
    FOREIGN KEY (partner_id) REFERENCES Partners(partner_id)
);

CREATE TABLE DeliveryLogs (
    log_id INT PRIMARY KEY,
    shipment_id INT,
    status VARCHAR(20),  -- 'Successful' or 'Returned'
    FOREIGN KEY (shipment_id) REFERENCES Shipments(shipment_id)
);

-----------------------------------------------------

-- 2. Insert Sample Data

INSERT INTO Partners VALUES
(1, 'FastExpress'),
(2, 'QuickShip'),
(3, 'SpeedLogistics');

INSERT INTO Shipments VALUES
(101, 1, 'Chennai', '2024-03-01', '2024-03-05', '2024-03-06'),
(102, 2, 'Bangalore', '2024-03-02', '2024-03-06', '2024-03-06'),
(103, 1, 'Chennai', '2024-03-10', '2024-03-15', '2024-03-18'),
(104, 3, 'Hyderabad', '2024-03-12', '2024-03-16', '2024-03-15'),
(105, 2, 'Chennai', '2024-03-15', '2024-03-20', '2024-03-25');

INSERT INTO DeliveryLogs VALUES
(1, 101, 'Successful'),
(2, 102, 'Successful'),
(3, 103, 'Returned'),
(4, 104, 'Successful'),
(5, 105, 'Returned');

-----------------------------------------------------

-- 3. Delayed Shipments Query

SELECT shipment_id, promised_date, actual_delivery_date
FROM Shipments
WHERE actual_delivery_date > promised_date;

-----------------------------------------------------

-- 4. Performance Ranking (Success vs Returned)

SELECT p.partner_name, d.status, COUNT(*) AS total
FROM DeliveryLogs d
JOIN Shipments s ON d.shipment_id = s.shipment_id
JOIN Partners p ON s.partner_id = p.partner_id
GROUP BY p.partner_name, d.status;

-----------------------------------------------------

-- 5. Zone Filter (Most Popular Destination City)

SELECT destination_city, COUNT(*) AS total_orders
FROM Shipments
WHERE order_date >= DATE_SUB(CURDATE(), INTERVAL 30 DAY)
GROUP BY destination_city
ORDER BY total_orders DESC;