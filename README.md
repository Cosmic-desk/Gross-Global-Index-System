# Gross Global Index Management System

## Overview

The Gross Global Index Management System is a database-driven economic analytics application developed using Python and MySQL. The project is designed to manage, analyze, and compare multi-year national economic indicators through a structured backend system and optimized SQL operations.

The system allows users to perform CRUD operations, generate ranking reports, analyze nation-wise economic performance, and maintain organized economic datasets efficiently.

---

# Features

* Add and manage nation-wise economic records
* Perform CRUD operations using MySQL
* Comparative multi-year economic analysis
* Ranking system based on key economic indicators
* Optimized SQL query execution
* Exception handling and input validation
* Structured tabular data display
* Menu-driven backend application

---

# Technologies Used

* Python
* MySQL
* SQL
* DBMS
* Data Analytics

---

# Economic Indicators Included

* GDP Growth
* GNP Value
* Imports Percentage
* Exports Percentage
* Literacy Rate
* Life Expectancy

---

# Database Schema

```sql
CREATE TABLE global_index (
    id INT AUTO_INCREMENT PRIMARY KEY,
    year_recorded YEAR NOT NULL,
    nation_name VARCHAR(50) NOT NULL,
    nation_code INT UNIQUE NOT NULL,
    gdp_growth DECIMAL(10,2),
    gnp_value DECIMAL(12,2),
    imports_percent DECIMAL(10,2),
    exports_percent DECIMAL(10,2),
    literacy_rate DECIMAL(5,2),
    life_expectancy DECIMAL(5,2)
);
```

---

# Project Structure

```text
Gross-Global-Index-System/
│
├── main.py
├── README.md
├── database_schema.sql
│
├── screenshots/
│   └── img-run.png
│
└── requirements.txt
```

---

# Functional Modules

## 1. Add Nation Data

Allows insertion of nation-wise economic indicators into the database.

## 2. Display Records

Displays all stored records in a structured tabular format.

## 3. Update Records

Updates existing economic indicators for a selected nation.

## 4. Delete Records

Deletes records securely using nation code.

## 5. Search Nation Performance

Displays economic performance of a nation across multiple years.

## 6. Ranking System

Ranks nations based on:

* GDP Growth
* Literacy Rate
* Exports
* Life Expectancy

---

# Key Concepts Applied

* Database Management System (DBMS)
* SQL Query Optimization
* Parameterized Queries
* Comparative Data Analysis
* Backend Application Development
* Structured Data Management
* Ranking Algorithms
* Economic KPI Analysis

---

# Application Screenshots

<img width="1536" height="1024" alt="IMG-RUN" src="https://github.com/user-attachments/assets/e272f0f4-8058-4625-82cf-dc57b299cc10" />

---

# Installation & Execution

## Clone Repository

```bash
git clone https://github.com/yourusername/gross-global-index-system.git
```

## Install MySQL Connector

```bash
pip install mysql-connector-python
```

## Run Project

```bash
python main.py
```

---

# Future Improvements

* Streamlit Dashboard
* Graphical User Interface (GUI)
* Data Visualization
* CSV/Excel Export
* Authentication System
* Real-Time Data Integration

---

# Author

**Avani Sharma**

---

# License

This project is developed for academic and learning purposes.

---
