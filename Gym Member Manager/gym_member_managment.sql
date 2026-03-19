-- Create Database
CREATE DATABASE IF NOT EXISTS gym_management;
USE gym_management;

-- Plans Table
CREATE TABLE IF NOT EXISTS plans (
    plan_id INT AUTO_INCREMENT PRIMARY KEY,
    plan_name VARCHAR(50),
    duration_months INT,
    price DECIMAL(10,2)
);

-- Insert Default Plans
INSERT INTO plans (plan_name, duration_months, price) VALUES
('1 Month', 1, 1000),
('3 Months', 3, 2500),
('6 Months', 6, 4500),
('12 Months', 12, 8000);

-- Members Table
CREATE TABLE IF NOT EXISTS members (
    member_id INT AUTO_INCREMENT PRIMARY KEY,
    full_name VARCHAR(100),
    phone VARCHAR(15),
    email VARCHAR(100),
    gender VARCHAR(10),
    age INT,
    plan_id INT,
    join_date DATE,
    expiry_date DATE,
    status VARCHAR(20),
    FOREIGN KEY (plan_id) REFERENCES plans(plan_id)
);

-- Payments Table
CREATE TABLE IF NOT EXISTS payments (
    payment_id INT AUTO_INCREMENT PRIMARY KEY,
    member_id INT,
    amount DECIMAL(10,2),
    payment_date DATE,
    FOREIGN KEY (member_id) REFERENCES members(member_id)
);


USE gym_management;

CREATE TABLE IF NOT EXISTS attendance (
    attendance_id INT AUTO_INCREMENT PRIMARY KEY,
    member_id INT,
    attendance_date DATE,
    FOREIGN KEY (member_id) REFERENCES members(member_id)
);


SET SQL_SAFE_UPDATES = 0;


-- Insert Demo Members

INSERT INTO members
(full_name, phone, email, gender, age, plan_id, join_date, expiry_date, status)
VALUES
('Rahul Sharma','9876543210','rahul@gmail.com','Male',25,1,'2025-01-01','2025-02-01','Expired'),
('Amit Verma','9123456780','amit@gmail.com','Male',28,2,'2025-01-15','2025-04-15','Active'),
('Sneha Patil','9988776655','sneha@gmail.com','Female',23,3,'2025-02-01','2025-08-01','Active'),
('Priya Singh','9012345678','priya@gmail.com','Female',30,4,'2024-12-01','2025-12-01','Active'),
('Rohit Kulkarni','9090909090','rohit@gmail.com','Male',27,1,'2024-12-01','2025-01-01','Expired');

-- Insert Demo Payments
INSERT INTO payments (member_id, amount, payment_date) VALUES
(1,1000,'2025-01-01'),
(2,2500,'2025-01-15'),
(3,4500,'2025-02-01'),
(4,8000,'2024-12-01'),
(5,1000,'2024-12-01');

-- Insert Demo Attendance
INSERT INTO attendance (member_id, attendance_date) VALUES
(2,CURDATE()),
(3,CURDATE()),
(4,CURDATE());

