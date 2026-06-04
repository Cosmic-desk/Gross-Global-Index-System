# Gross Global Index Management System

## Overview

The Gross Global Index Management System is a Python-MySQL based database application developed to manage, analyze, and compare multi-year national economic indicators. The system enables efficient storage, retrieval, updating, deletion, and ranking of country-wise economic data through a menu-driven backend interface.

---

## Features

* Add and manage nation-wise economic records
* Perform CRUD operations using MySQL
* Comparative analysis of nations over multiple years
* Ranking system based on economic indicators
* Structured tabular data reporting
* Exception handling and input validation
* Optimized SQL queries using parameterized statements

---

## Technologies Used

* Python
* MySQL
* SQL
* DBMS Concepts

---

## Economic Indicators Included

* GDP Growth
* GNP Value
* Imports Percentage
* Exports Percentage
* Literacy Rate
* Life Expectancy

---

## Project Structure

```text
Gross-Global-Index-System/
│
├── main.py
├── README.md
└── database_schema.sql
```

---

## Database Schema

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

## Functional Modules

* Add Nation Data
* Display Records
* Update Records
* Delete Records
* Search Nation Performance
* Ranking System

---

## Key Concepts Applied

* Database Management System (DBMS)
* SQL Query Optimization
* Parameterized Queries
* Data Analytics
* Comparative Performance Analysis
* Backend Application Development

---

## Future Improvements

* GUI Integration
* Data Visualization Dashboard
* CSV/Excel Export
* Authentication System
* Streamlit Web Application
* Real-time Data Import

---

## Author

Avani Sharma

---

## License

This project is developed for academic and learning purposes.
