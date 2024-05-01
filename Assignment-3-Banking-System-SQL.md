# Assignment 3 - SQL & OOPS Banking System

## Tasks 1: Database Design:

**1. Create the database named "HMBank"**

```sql
CREATE DATABASE HMBank
USE HMBank
```

**2. Define the schema for the Customers, Accounts, and Transactions tables based on the provided schema.**
- ***Customers Table***
    - `customer_id`: Unique identifier for each customer, primary key of the table.
    - `first_name`: First name of the customer, stored as a string.
    - `last_name`: Last name of the customer, stored as a string.
    - `DOB`: Date of birth of the customer, with a check constraint to ensure it falls between '1900-01-01' and '2020-12-31'.
    - `email`: Email address of the customer, stored as a string.
    - `phone_number`: Phone number of the customer, stored as a 10-digit integer with a check constraint.
    - `perm_address`: Permanent address of the customer, stored as a string.

- ***Accounts Table***
    - `account_id`: Unique identifier for each account, primary key of the table.
    - `customer_id`: Identifier for the customer associated with the account, a foreign key referencing the customer_id column in the Customers table.
    - `account_type`: Type of the account, stored as a string. For example, Savings, Current, etc.
    - `balance`: Balance of the account, stored as an integer with a default value of 0 and a check constraint to ensure it's non-negative.

- ***Transactions Table***
    - `transaction_id`: Unique identifier for each transaction, primary key of the table.
    - `account_id`: Identifier for the account associated with the transaction, a foreign key referencing the account_id column in the Accounts table.
    - `transaction_type`: Type of the transaction, stored as a string. For example, Withdrawl, Deposit, etc.
    - `amount`: Amount of the transaction, stored as an integer with a check constraint to ensure it's positive and not null.
    - `transaction_date`: Date of the transaction, stored as a date.

**4. Create an ERD (Entity Relationship Diagram) for the database.**

![Entity Relationship Diagram](.\Resources\ERD-HMBank.png)

**5. Create appropriate Primary Key and Foreign Key constraints for referential integrity.**

### Primary Keys:
- **Customers**: `customer_id`
- **Accounts**: `account_id`
- **Transactions**: `transaction_id`

### Foreign Keys:
- **Accounts** references **Customers**: `customer_id`
- **Transactions** references **Accounts**: `account_id`

**6. Write SQL scripts to create the mentioned tables with appropriate data types, constraints, and relationships.**
- ***Customers***
- ***Accounts***
- ***Transactions***

> Creating Customers Table
```sql
CREATE TABLE [Customers] (
  [customer_id] INTEGER,
  [first_name] TEXT,
  [last_name] TEXT,
  [DOB] DATE CHECK (DOB >= '1900-01-01' AND DOB <= '2020-12-31'),
  [email] VARCHAR(255),
  [phone_number] BIGINT CHECK(LEN(phone_number) = 10),
  [perm_address] VARCHAR(255),
  PRIMARY KEY ([customer_id])
);
```

> Creating Accounts Table
```sql
CREATE TABLE [Accounts] (
  [account_id] INTEGER,
  [customer_id] INTEGER,
  [account_type] VARCHAR(255),
  [balance] INTEGER DEFAULT 0 CHECK(balance >= 0),
  PRIMARY KEY ([account_id]),
  CONSTRAINT [FK_Accounts.customer_id]
    FOREIGN KEY ([customer_id])
      REFERENCES [Customers]([customer_id])
);
```

> Creating Transactions Table
```sql
CREATE TABLE [Transactions] (
  [transaction_id] INTEGER,
  [account_id] INTEGER,
  [transaction_type] VARCHAR(255),
  [amount] INTEGER NOT NULL CHECK (amount > 0),
  [transaction_date] DATE,
  PRIMARY KEY ([transaction_id]),
  CONSTRAINT [FK_Transactions.account_id]
    FOREIGN KEY ([account_id])
      REFERENCES [Accounts]([account_id])
);
```
---

## Tasks 2: Select, Where, Between, AND, LIKE: 

**1. Insert at least 10 sample records into each of the following tables.**   
- *Customers*  
  ```sql
  INSERT INTO Customers (customer_id, first_name, last_name, DOB, email, phone_number, perm_address) 
  VALUES 
    (1, 'John', 'Smith', '1990-05-15', 'john.smith@example.com', 1234567890, '123 Main St, City'),
    (2, 'Alice', 'Johnson', '1985-10-22', 'alice.johnson@example.com', 2345678901, '456 Elm St, Town'),
    (3, 'Michael', 'Brown', '1978-03-30', 'michael.brown@example.com', 3456789012, '789 Oak St, Village'),
    (4, 'Emily', 'Davis', '1995-12-10', 'emily.davis@example.com', 4567890123, '567 Pine St, Hamlet'),
    (5, 'Jessica', 'Miller', '1982-07-08', 'jessica.miller@example.com', 5678901234, '890 Maple St, County'),
    (6, 'Robert', 'Wilson', '1970-09-25', 'robert.wilson@example.com', 6789012345, '901 Cedar St, City'),
    (7, 'Sarah', 'Moore', '1988-11-17', 'sarah.moore@example.com', 7890123456, '234 Birch St, Town'),
    (8, 'David', 'Taylor', '1980-04-05', 'david.taylor@example.com', 8901234567, '345 Oak St, Village'),
    (9, 'Jennifer', 'Anderson', '1975-01-20', 'jennifer.anderson@example.com', 9012345678, '678 Pine St, Hamlet'),
    (10, 'James', 'Thomas', '1992-08-12', 'james.thomas@example.com', 1234567890, '789 Maple St, County'),
    (11, 'Mary', 'White', '1987-06-28', 'mary.white@example.com', 2345678901, '901 Cedar St, City'),
    (12, 'Daniel', 'Martinez', '1973-02-14', 'daniel.martinez@example.com', 3456789012, '123 Pine St, Hamlet');
  ```
- *Accounts*
  ```sql
  INSERT INTO Accounts (account_id, customer_id, account_type, balance) 
  VALUES 
    (1011, 1, 'savings', 10000),
    (1012, 1, 'current', 50000),
    (1023, 2, 'zero_balance', 200),
    (1032, 3, 'current', 30000),
    (1041, 4, 'savings', 25000),
    (1053, 5, 'zero_balance', 0),
    (1061, 6, 'savings', 15000),
    (1062, 6, 'current', 60000),
    (1071, 7, 'savings', 25000),
    (1081, 8, 'savings', 18000),
    (1091, 9, 'savings', 40000),
    (1092, 9, 'current', 22000),
    (1103, 10, 'zero_balance', 0),
    (1112, 11, 'current', 70000),
    (1121, 12, 'savings', 27000);
  ```
- *Transactions*
  ```sql
  INSERT INTO Transactions (transaction_id, account_id, transaction_type, amount, transaction_date)
  VALUES 
    (101101, 1011, 'debit', 200, '2024-04-01'),
    (101102, 1011, 'credit', 200, '2024-04-01'),
    (102301, 1023, 'debit', 50, '2024-04-02'),
    (102302, 1023, 'credit', 500, '2024-04-02'),
    (106101, 1061, 'debit', 1000, '2024-04-03'),
    (106102, 1061, 'credit', 100, '2024-04-03'),
    (107101, 1071, 'debit', 300, '2024-04-04'),
    (107102, 1071, 'credit', 350, '2024-04-04'),
    (103201, 1032, 'debit', 400, '2024-04-05'),
    (103202, 1032, 'credit', 300, '2024-04-05'),
    (109101, 1091, 'debit', 150, '2024-04-06'),
    (109102, 1091, 'credit', 200, '2024-04-06'),
    (106201, 1062, 'debit', 500, '2024-04-07'),
    (106202, 1062, 'credit', 400, '2024-04-07'),
    (109201, 1092, 'debit', 100, '2024-04-08'),
    (109202, 1092, 'credit', 150, '2024-04-08'),
    (104101, 1041, 'debit', 200, '2024-04-09'),
    (111201, 1112, 'credit', 700, '2024-04-10'),
    (108101, 1081, 'debit', 100, '2024-04-11'),
    (112101, 1121, 'credit', 270, '2024-04-12');
  ```

**2. Write SQL queries for the following tasks:** 

*1. Write a SQL query to retrieve the name, account type and email of all customers.* 
  ```sql
  SELECT CONCAT(c.first_name, ' ',c.last_name) AS Name, a.account_type, c.email 
  FROM Customers c INNER JOIN Accounts a
  ON c.customer_id = a.customer_id;
  ```
  ### *Output*
  | Name            | account_type | email                     |
  |-----------------|--------------|---------------------------|
  | John Smith      | savings      | john.smith@example.com   |
  | John Smith      | current      | john.smith@example.com   |
  | Alice Johnson   | zero_balance| alice.johnson@example.com|
  | Michael Brown   | current      | michael.brown@example.com|
  | Emily Davis     | savings      | emily.davis@example.com  |
  | Jessica Miller  | zero_balance| jessica.miller@example.com|
  | Robert Wilson   | savings      | robert.wilson@example.com|
  | Robert Wilson   | current      | robert.wilson@example.com|
  | Sarah Moore     | savings      | sarah.moore@example.com  |
  | David Taylor    | savings      | david.taylor@example.com  |
  | Jennifer Anderson | savings    | jennifer.anderson@example.com|
  | Jennifer Anderson | current    | jennifer.anderson@example.com|
  | James Thomas    | zero_balance| james.thomas@example.com  |
  | Mary White      | current      | mary.white@example.com    |
  | Daniel Martinez| savings      | daniel.martinez@example.com|
  ||
  

*2. Write a SQL query to list all transaction corresponding customer.*
  ```sql
  SELECT CONCAT(c.first_name, ' ', c.last_name) AS Customer_Name, 
         t.transaction_id, 
         t.transaction_type, 
         t.amount, 
         t.transaction_date
  FROM Customers c 
  INNER JOIN Accounts a ON c.customer_id = a.customer_id
  INNER JOIN Transactions t ON a.account_id = t.account_id;
  ```
  ### *Output*
  | Customer_Name   | transaction_id | transaction_type | amount | transaction_date |
  |-----------------|----------------|------------------|--------|------------------|
  | John Smith      | 101101         | debit            | 200    | 2024-04-01       |
  | John Smith      | 101102         | credit           | 200    | 2024-04-01       |
  | Alice Johnson   | 102301         | debit            | 50     | 2024-04-02       |
  | Alice Johnson   | 102302         | credit           | 500    | 2024-04-02       |
  | Robert Wilson   | 106101         | debit            | 1000   | 2024-04-03       |
  | Robert Wilson   | 106102         | credit           | 100    | 2024-04-03       |
  | Sarah Moore     | 107101         | debit            | 300    | 2024-04-04       |
  | Sarah Moore     | 107102         | credit           | 350    | 2024-04-04       |
  | Michael Brown   | 103201         | debit            | 400    | 2024-04-05       |
  | Michael Brown   | 103202         | credit           | 300    | 2024-04-05       |
  | Jennifer Anderson | 109101       | debit            | 150    | 2024-04-06       |
  | Jennifer Anderson | 109102       | credit           | 200    | 2024-04-06       |
  | Robert Wilson   | 106201         | debit            | 500    | 2024-04-07       |
  | Robert Wilson   | 106202         | credit           | 400    | 2024-04-07       |
  | Jennifer Anderson | 109201       | debit            | 100    | 2024-04-08       |
  | Jennifer Anderson | 109202       | credit           | 150    | 2024-04-08       |
  | Emily Davis     | 104101         | debit            | 200    | 2024-04-09       |
  | Mary White      | 111201         | credit           | 700    | 2024-04-10       |
  | David Taylor    | 108101         | debit            | 100    | 2024-04-11       |
  | Daniel Martinez | 112101         | credit           | 270    | 2024-04-12       |
  ||

*3. Write a SQL query to increase the balance of a specific account by a certain amount.* 
  ```sql
  UPDATE Accounts
  SET balance = balance + 2000
  WHERE account_id = 1011;
  ```

*4. Write a SQL query to Combine first and last names of customers as a full_name.*
  ```sql
  SELECT CONCAT(first_name, ' ', last_name) AS full_name
  FROM Customers;
  ``` 
  ### *Output*
  | full_name      |
  |----------------|
  | John Smith     |
  | Alice Johnson  |
  | Michael Brown  |
  | Emily Davis    |
  | Jessica Miller |
  | Robert Wilson  |
  | Sarah Moore    |
  | David Taylor   |
  | Jennifer Anderson |
  | James Thomas   |
  | Mary White     |
  | Daniel Martinez|
  ||

*5. Write a SQL query to remove accounts with a balance of zero where the account type is savings.* 
  ```sql
  DELETE FROM Accounts
  WHERE balance = 0
  AND account_type = 'savings';
  ```

*6. Write a SQL query to Find customers living in a specific city.* 
  ```sql
  SELECT *
  FROM Customers
  WHERE perm_address LIKE '%City%';
  ```
  ### *Output*
  | customer_id | first_name | last_name |    DOB     |         email         | phone_number |    perm_address    |
  |-------------|------------|-----------|------------|-----------------------|--------------|--------------------|
  |     1       |   John     |   Smith   | 1990-05-15 | john.smith@example.com|  1234567890  | 123 Main St, City  |
  |     6       |  Robert    |  Wilson   | 1970-09-25 | robert.wilson@example.com |  6789012345  | 901 Cedar St, City |
  |    11       |   Mary     |   White   | 1987-06-28 | mary.white@example.com|  2345678901  | 901 Cedar St, City |


*7. Write a SQL query to Get the account balance for a specific account.* 
  ```sql
  SELECT balance
  FROM Accounts
  WHERE account_id = 1061;
  ```
  ### *Output*
  | balance |
  |---------|
  | 15000   |
  ||


*8. Write a SQL query to List all current accounts with a balance greater than $1,000.* 
  ```sql
  SELECT *
  FROM Accounts
  WHERE account_type = 'current'
  AND balance > 1000;
  ```
  ### *Output*
  | account_id | customer_id | account_type | balance |
  |------------|-------------|--------------|---------|
  |    1012    |      1      |   current    |  50000  |
  |    1062    |      6      |   current    |  60000  |
  |    1071    |      7      |   current    |  25000  |
  |    1092    |      9      |   current    |  22000  |
  |    1112    |     11      |   current    |  70000  |
  ||

*9. Write a SQL query to Retrieve all transactions for a specific account.*
  ```sql
  SELECT *
  FROM Transactions t
  JOIN Accounts a ON t.account_id = a.account_id
  WHERE a.account_id = 1092;
  ```
  ### *Output*
  | transaction_id | account_id | transaction_type | amount | transaction_date | account_id | customer_id | account_type | balance |
  |----------------|------------|------------------|--------|------------------|------------|-------------|--------------|---------|
  |     109201     |    1092    |      debit       |  100   |   2024-04-08     |    1092    |      9      |   current    |  22000  |
  |     109202     |    1092    |     credit       |  150   |   2024-04-08     |    1092    |      9      |   current    |  22050  |
  ||

*10. Write a SQL query to Calculate the interest accrued on savings accounts based on a given interest rate.* 
  ```sql
  SELECT account_id, balance*(0.04) AS interest_accrued
  FROM Accounts
  WHERE account_type = 'savings';
  ```
  ### *Output*
  | account_id | interest_accrued |
  |------------|------------------|
  |    1011    |       400.00     |
  |    1041    |      1000.00     |
  |    1061    |       600.00     |
  |    1071    |      1000.00     |
  |    1081    |       720.00     |
  |    1091    |      1600.00     |
  |    1121    |      1080.00     |
  ||


*11. Write a SQL query to Identify accounts where the balance is less than a specified overdraft limit.* 
  ```sql
  SELECT *
  FROM Accounts
  WHERE balance < 15000;
  ```
  ### *Output*
  | account_id | customer_id | account_type  | balance |
  |------------|-------------|---------------|---------|
  | 1011       | 1           | savings       | 12000   |
  | 1023       | 2           | zero_balance  | 200     |
  | 1053       | 5           | zero_balance  | 0       |
  | 1103       | 10          | zero_balance  | 0       |
  ||


*12. Write a SQL query to Find customers not living in a specific city.* 
  ```sql
  SELECT *
  FROM Customers
  WHERE perm_address NOT LIKE '%Hamlet%';
  ```
  ### *Output*
  | customer_id | first_name | last_name | DOB        | email                     | phone_number | perm_address        |
  |-------------|------------|-----------|------------|---------------------------|--------------|---------------------|
  | 1           | John       | Smith     | 1990-05-15 | john.smith@example.com    | 1234567890   | 123 Main St, City  |
  | 2           | Alice      | Johnson   | 1985-10-22 | alice.johnson@example.com | 2345678901   | 456 Elm St, Town   |
  | 3           | Michael    | Brown     | 1978-03-30 | michael.brown@example.com | 3456789012   | 789 Oak St, Village|
  | 5           | Jessica    | Miller    | 1982-07-08 | jessica.miller@example.com| 5678901234   | 890 Maple St, County|
  | 6           | Robert     | Wilson    | 1970-09-25 | robert.wilson@example.com | 6789012345   | 901 Cedar St, City |
  | 7           | Sarah      | Moore     | 1988-11-17 | sarah.moore@example.com   | 7890123456   | 234 Birch St, Town |
  | 8           | David      | Taylor    | 1980-04-05 | david.taylor@example.com  | 8901234567   | 345 Oak St, Village|
  | 10          | James      | Thomas    | 1992-08-12 | james.thomas@example.com  | 1234567890   | 789 Maple St, County|
  | 11          | Mary       | White     | 1987-06-28 | mary.white@example.com    | 2345678901   | 901 Cedar St, City |
  ||

---

## Tasks 3: Aggregate functions, Having, Order By, GroupBy and Joins: 

**1. Write a SQL query to Find the average account balance for all customers.**   
```sql
SELECT AVG(balance) AS avg_balance
FROM Accounts;
```

**2. Write a SQL query to Retrieve the top 10 highest account balances.** 
```sql
SELECT TOP 10 *
FROM Accounts
ORDER BY balance DESC;
```

**3. Write a SQL query to Calculate Total Deposits for All Customers in specific date.**
```sql
SELECT SUM(amount) AS total_deposits
FROM Transactions
WHERE transaction_type = 'credit'
AND transaction_date = '2024-04-05';
```

**4. Write a SQL query to Find the Oldest and Newest Customers.**
```sql
SELECT MIN(DOB) AS oldest_customer_DOB, MAX(DOB) AS newest_customer_DOB
FROM Customers;
```

**5. Write a SQL query to Retrieve transaction details along with the account type.**
```sql
SELECT t.*, a.account_type
FROM Transactions t
INNER JOIN Accounts a ON t.account_id = a.account_id;
```

**6. Write a SQL query to Get a list of customers along with their account details.** 
```sql
SELECT CONCAT(c.first_name, ' ', c.last_name) AS full_name , a.*
FROM Customers c
INNER JOIN Accounts a ON c.customer_id = a.customer_id;
```

**7. Write a SQL query to Retrieve transaction details along with customer information for a specific account.** 
```sql
SELECT t.*, c.*
FROM Transactions t
INNER JOIN Accounts a ON t.account_id = a.account_id
INNER JOIN Customers c ON a.customer_id = c.customer_id
WHERE a.account_id = 1071;
```

**8. Write a SQL query to Identify customers who have more than one account.** 
```sql
SELECT c.customer_id, 
       CONCAT(c.first_name, ' ', 
       c.last_name) AS full_name
FROM Customers c
WHERE c.customer_id IN (
    SELECT customer_id
    FROM Accounts
    GROUP BY customer_id
    HAVING COUNT(*) > 1
);
```

**9. Write a SQL query to Calculate the difference in transaction amounts between deposits and withdrawals.**
```sql
SELECT account_id, 
       SUM(CASE WHEN transaction_type = 'credit' THEN amount ELSE -amount END) AS transaction_difference
FROM Transactions
GROUP BY account_id;
```

**10. Write a SQL query to Calculate the average daily balance for each account over a specified period.**
```sql
SELECT 
    account_id,
    AVG(balance) AS avg_daily_balance
FROM (
      SELECT 
          a.account_id,
          t.transaction_date,
          SUM(CASE WHEN t.transaction_type = 'debit' THEN -t.amount ELSE t.amount END) AS balance
      FROM Accounts a
      LEFT JOIN Transactions t ON a.account_id = t.account_id
      WHERE t.transaction_date BETWEEN '2024-04-01' AND '2024-04-12'
      GROUP BY a.account_id, t.transaction_date
    ) AS daily_balances
GROUP BY account_id;
```

**11. Calculate the total balance for each account type.**
```sql
SELECT account_type, 
       SUM(balance) AS total_balance
FROM Accounts
GROUP BY account_type;
```

**12. Identify accounts with the highest number of transactions order by descending order.**
```sql
SELECT account_id, 
       COUNT(*) AS transaction_count
FROM Transactions
GROUP BY account_id
ORDER BY transaction_count DESC;
```

**13. List customers with high aggregate account balances, along with their account types.** 
```sql
SELECT * 
FROM Accounts a INNER JOIN (SELECT c.customer_id, 
						  SUM(a.balance) AS aggregate_balance
						  FROM Customers c INNER JOIN Accounts a
						  ON c.customer_id = a.customer_id
						  GROUP BY c.customer_id) s
ON a.customer_id = s.customer_id;
```

**14. Identify and list duplicate transactions based on transaction amount, date, and account.**
```sql
SELECT t1.*
FROM Transactions t1
JOIN Transactions t2 ON t1.amount = t2.amount AND t1.transaction_date = t2.transaction_date AND t1.account_id = t2.account_id
WHERE t1.transaction_id <> t2.transaction_id;
```
---

## Tasks 4: Subquery and its type: 

**1. Retrieve the customer(s) with the highest account balance.**
```sql
SELECT c.*
FROM Customers c
INNER JOIN Accounts a ON c.customer_id = a.customer_id
WHERE a.balance = (SELECT MAX(balance) FROM Accounts);
```
### *Output*
| customer_id | first_name | last_name |    DOB     |          email          |  phone_number  |    perm_address    |
|-------------|------------|-----------|------------|-------------------------|----------------|--------------------|
|     11      |   Mary     |   White   | 1987-06-28 | mary.white@example.com | 2345678901 | 901 Cedar St, City |
||

**2. Calculate the average account balance for customers who have more than one account.**
```sql
SELECT AVG(avg_balance) AS avg_balance
FROM (
    SELECT AVG(balance) as avg_balance
    FROM Accounts
    GROUP BY customer_id
    HAVING COUNT(*) > 1
) AS s;
```
### *Output*
| avg_balance |
|-------------|
|    33166    |
||

**3. Retrieve accounts with transactions whose amounts exceed the average transaction amount.**
```sql
SELECT a.*
FROM Accounts a
INNER JOIN Transactions t ON a.account_id = t.account_id
WHERE t.amount > (SELECT AVG(amount) FROM Transactions);
```
### *Output*
| account_id | customer_id | account_type | balance |
|------------|-------------|--------------|---------|
|    1023    |      2      | zero_balance |   200   |
|    1032    |      3      |   current    |  30000  |
|    1061    |      6      |   savings    |  15000  |
|    1062    |      6      |   current    |  60000  |
|    1062    |      6      |   current    |  60000  |
|    1071    |      7      |   savings    |  25000  |
|    1112    |     11      |   current    |  70000  |
||

**4. Identify customers who have no recorded transactions.**
```sql
SELECT c.*
FROM Customers c
LEFT JOIN Accounts a ON c.customer_id = a.customer_id
LEFT JOIN Transactions t ON a.account_id = t.account_id
WHERE t.transaction_id IS NULL;
```
### *Output*
| customer_id | first_name | last_name |    DOB     |             email             | phone_number |     perm_address     |
|-------------|------------|-----------|------------|------------------------------|--------------|----------------------|
|      1      |    John    |   Smith   | 1990-05-15 | john.smith@example.com       |  1234567890  | 123 Main St, City    |
|      5      |  Jessica   |  Miller   | 1982-07-08 | jessica.miller@example.com   |  5678901234  | 890 Maple St, County |
|     10      |   James    |  Thomas   | 1992-08-12 | james.thomas@example.com     |  1234567890  | 789 Maple St, County |
||

**5. Calculate the total balance of accounts with no recorded transactions.**
```sql
SELECT SUM(balance) AS total_balance
FROM Accounts a
LEFT JOIN Transactions t ON a.account_id = t.account_id
WHERE t.transaction_id IS NULL;
```
### *Output*
| total_balance |
|---------------|
|     50000     |
||

**6. Retrieve transactions for accounts with the lowest balance.**
```sql
SELECT t.*
FROM Transactions t
INNER JOIN Accounts a ON t.account_id = a.account_id
WHERE a.balance = (SELECT MIN(balance) FROM Accounts);
```
### *Output*
| transaction_id | account_id | transaction_type | amount | transaction_date |
|----------------|------------|------------------|--------|------------------|
|                |            |                  |        |                  |


**7. Identify customers who have accounts of multiple types.**
```sql
SELECT c.*
FROM Customers c
INNER JOIN (
    SELECT customer_id
    FROM Accounts
    GROUP BY customer_id
    HAVING COUNT(DISTINCT account_type) > 1
) AS multi_type ON c.customer_id = multi_type.customer_id;
```
### *Output*
| customer_id | first_name | last_name |    DOB     |              email              | phone_number |      perm_address       |
|-------------|------------|-----------|------------|--------------------------------|--------------|-------------------------|
|      1      |    John    |   Smith   | 1990-05-15 |   john.smith@example.com       |  1234567890  |    123 Main St, City    |
|      6      |   Robert   |   Wilson  | 1970-09-25 | robert.wilson@example.com      |  6789012345  |    901 Cedar St, City   |
|      9      |  Jennifer  |  Anderson | 1975-01-20 | jennifer.anderson@example.com  |  9012345678  |  678 Pine St, Hamlet    |
||


**8. Calculate the percentage of each account type out of the total number of accounts.**
```sql
SELECT account_type, 
       COUNT(*) * 100.0 / (SELECT COUNT(*) FROM Accounts) AS percentage
FROM Accounts
GROUP BY account_type;
```
### *Output*
| account_type  |     percentage     |
|---------------|--------------------|
|    current    | 33.333333333333%  |
|    savings    | 46.666666666666%  |
| zero_balance  | 20.000000000000%  |
||

**9. Retrieve all transactions for a customer with a given customer_id.**
```sql
SELECT t.*
FROM Transactions t
INNER JOIN Accounts a ON t.account_id = a.account_id
WHERE a.customer_id = 2;
```
### *Output*
| transaction_id | account_id | transaction_type | amount | transaction_date |
|----------------|------------|------------------|--------|------------------|
|    102301      |    1023    |      debit       |   50   |   2024-04-02     |
|    102302      |    1023    |     credit       |  500   |   2024-04-02     |
||

**10. Calculate the total balance for each account type, including a subquery within the SELECT clause.**
```sql
SELECT account_type,
	  (SELECT SUM(balance) 
	   FROM Accounts a 
	   WHERE a.account_type = outerQuery.account_type) AS total_balance
FROM (SELECT DISTINCT account_type 
      FROM Accounts) AS outerQuery;
```
### *Output*
| account_type  | total_balance |
|---------------|---------------|
|    current    |    232000     |
|    savings    |    162000     |
| zero_balance  |      200      |
||