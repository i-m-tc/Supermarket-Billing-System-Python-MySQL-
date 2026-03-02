create database retail_project_more_supermarket;
use retail_project_more_supermarket;
show tables;

CREATE TABLE cust_details (
    c_id INT PRIMARY KEY AUTO_INCREMENT,
    c_name VARCHAR(255) NOT NULL,
    c_address VARCHAR(500) NOT NULL,
    c_ph_number BIGINT NOT NULL
);
SELECT * FROM cust_details;

INSERT INTO cust_details (c_name, c_address, c_ph_number)
VALUES ('Rahul Sharma', 'Kolkata, West Bengal', 9876543210);

TRUNCATE TABLE cust_details;

SELECT * FROM cust_details WHERE c_ph_number='9876543210';

CREATE TABLE product_details (
    p_id INT PRIMARY KEY AUTO_INCREMENT,
    P_name varchar(255) not null,
    p_price DECIMAL(10,2) NOT NULL,
    p_stock INT NOT NULL
);

INSERT INTO product_details (p_name, p_price, p_stock) VALUES ('Basmati Rice 5Kg', 449.00, 120);
INSERT INTO product_details (p_name, p_price, p_stock) VALUES ('Atta - Whole Wheat 5Kg', 235.00, 90);
INSERT INTO product_details (p_name, p_price, p_stock) VALUES ('Sugar 1Kg', 46.00, 150);
INSERT INTO product_details (p_name, p_price, p_stock) VALUES ('Salt - Iodized 1Kg', 20.00, 200);
INSERT INTO product_details (p_name, p_price, p_stock) VALUES ('Sunflower Oil 1L', 135.00, 80);
INSERT INTO product_details (p_name, p_price, p_stock) VALUES ('Mustard Oil 1L', 145.00, 75);
INSERT INTO product_details (p_name, p_price, p_stock) VALUES ('Toor Dal 1Kg', 155.00, 60);
INSERT INTO product_details (p_name, p_price, p_stock) VALUES ('Moong Dal 1Kg', 130.00, 50);
INSERT INTO product_details (p_name, p_price, p_stock) VALUES ('Chana Dal 1Kg', 78.00, 65);
INSERT INTO product_details (p_name, p_price, p_stock) VALUES ('Masoor Dal 1Kg', 90.00, 70);

INSERT INTO product_details (p_name, p_price, p_stock) VALUES ('Poha 1Kg', 55.00, 100);
INSERT INTO product_details (p_name, p_price, p_stock) VALUES ('Sooji 1Kg', 45.00, 95);
INSERT INTO product_details (p_name, p_price, p_stock) VALUES ('Besan 1Kg', 85.00, 85);
INSERT INTO product_details (p_name, p_price, p_stock) VALUES ('Rawa 1Kg', 52.00, 110);
INSERT INTO product_details (p_name, p_price, p_stock) VALUES ('Maida 1Kg', 40.00, 90);

INSERT INTO product_details (p_name, p_price, p_stock) VALUES ('Tea Powder 250g', 75.00, 70);
INSERT INTO product_details (p_name, p_price, p_stock) VALUES ('Coffee 200g', 130.00, 40);
INSERT INTO product_details (p_name, p_price, p_stock) VALUES ('Jaggery 1Kg', 72.00, 65);
INSERT INTO product_details (p_name, p_price, p_stock) VALUES ('Ghee 500ml', 310.00, 50);
INSERT INTO product_details (p_name, p_price, p_stock) VALUES ('Butter 100g', 52.00, 80);

INSERT INTO product_details (p_name, p_price, p_stock) VALUES ('Bread - White 400g', 38.00, 50);
INSERT INTO product_details (p_name, p_price, p_stock) VALUES ('Brown Bread 400g', 42.00, 45);
INSERT INTO product_details (p_name, p_price, p_stock) VALUES ('Eggs Pack of 6', 48.00, 70);
INSERT INTO product_details (p_name, p_price, p_stock) VALUES ('Milk 1L', 54.00, 100);
INSERT INTO product_details (p_name, p_price, p_stock) VALUES ('Curd 500g', 35.00, 90);

INSERT INTO product_details (p_name, p_price, p_stock) VALUES ('Onion 1Kg', 34.00, 200);
INSERT INTO product_details (p_name, p_price, p_stock) VALUES ('Potato 1Kg', 28.00, 180);
INSERT INTO product_details (p_name, p_price, p_stock) VALUES ('Tomato 1Kg', 32.00, 170);
INSERT INTO product_details (p_name, p_price, p_stock) VALUES ('Green Chilli 100g', 12.00, 90);
INSERT INTO product_details (p_name, p_price, p_stock) VALUES ('Garlic 250g', 42.00, 80);

INSERT INTO product_details (p_name, p_price, p_stock) VALUES ('Ginger 250g', 30.00, 75);
INSERT INTO product_details (p_name, p_price, p_stock) VALUES ('Banana (6 pcs)', 35.00, 120);
INSERT INTO product_details (p_name, p_price, p_stock) VALUES ('Apple 1Kg', 165.00, 60);
INSERT INTO product_details (p_name, p_price, p_stock) VALUES ('Orange 1Kg', 90.00, 70);
INSERT INTO product_details (p_name, p_price, p_stock) VALUES ('Mango 1Kg', 120.00, 50);

INSERT INTO product_details (p_name, p_price, p_stock) VALUES ('Biscuit - ParleG 250g', 35.00, 150);
INSERT INTO product_details (p_name, p_price, p_stock) VALUES ('Maggi 70g', 14.00, 200);
INSERT INTO product_details (p_name, p_price, p_stock) VALUES ('Pasta 500g', 85.00, 90);
INSERT INTO product_details (p_name, p_price, p_stock) VALUES ('Cornflakes 500g', 140.00, 60);
INSERT INTO product_details (p_name, p_price, p_stock) VALUES ('Pickle 500g', 95.00, 55);

select * from product_details;

create table bill_details(
sl_no int primary key auto_increment not null,
bill_id int not null,
product_id int not null,
product_name varchar(100) not null,
product_quantity int not null);

INSERT INTO bill_details (bill_id, product_id, product_name, product_quantity)
VALUES (101, 5, 'Basmati Rice 5Kg', 2);

select * from bill_details;

drop table analytics_table;
CREATE TABLE analytics_table (
    bill_id INT auto_increment not NULL,
    customer_id INT NOT NULL,
    customer_name VARCHAR(255) NOT NULL,
    total_bill_amount DECIMAL(10,2) NOT NULL,
    bill_timestamp DATETIME default current_timestamp,
    PRIMARY KEY (bill_id)
);

INSERT INTO analytics_table 
(customer_id, customer_name, total_bill_amount)
VALUES 
(301, 'Aditya Verma', 1450.60);

SELECT * FROM cust_details;
select * from product_details;

select * from bill_details;
select * from analytics_table;

select bill_id from analytics_table where bill_timestamp = 
(select max(bill_timestamp) from analytics_table);