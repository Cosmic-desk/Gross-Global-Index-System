# Gross Global Index Management System

## Overview

The Gross Global Index Management System is a Python-MySQL based economic analytics application developed to manage, analyze, and compare multi-year national economic indicators.

This repository contains **two implementations** of the project:

- **GGI.py** – Creates the database and table from scratch before performing complete CRUD operations.
- **SQL - python GGI Dynamic Version.py** – Performs data management and analysis on an existing MySQL database with enhanced dynamic functionality.

The project demonstrates SQL database management, Python-MySQL integration, data retrieval, reporting, and analytical operations through a menu-driven console application.

---

# Features

## Database Management

- Create database and table (GGI.py)
- Insert new economic records
- Update existing records
- Delete records
- Search nation-wise records

## Data Analysis

- Display complete dataset
- Display selected number of records
- Generate dynamic ranking reports
- Compare economic indicators across countries
- Analyze nation-wise economic performance

## General Features

- Dynamic column header generation
- Dynamic table formatting
- Exception handling and input validation
- Menu-driven backend application
- Optimized SQL query execution

---

# Technologies Used

- Python
- MySQL
- SQL
- DBMS
- Data Analytics
- Power BI

---

# Economic Indicators Included

- GDP Growth %
- GNI (Billion USD)
- Imports % GDP
- Exports % GDP
- Literacy Rate %
- Life Expectancy

---

# Database Schema

```sql
CREATE TABLE global_index (
    id INT AUTO_INCREMENT PRIMARY KEY,
    year_recorded YEAR NOT NULL,
    nation_name VARCHAR(50) NOT NULL,
    nation_code INT UNIQUE NOT NULL,
    gdp_growth DECIMAL(10,2),
    gni_value DECIMAL(12,2),
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
├── GGI.py
├── SQL - python GGI Dynamic Version.py
├── README.md
├── database_schema.sql
├── requirements.txt
│
├── Dataset/
│   ├── GGI Dataset.csv
│   ├── GGI Dataset excel.xlsx
│   └── gross_global_index.sql
│
├── Power BI Dashboard/
│   └── GGI Dashboard.pbix
│
└── Screenshots/
```

---

# Functional Modules

## GGI.py

- Create database
- Create table
- Insert records
- Display records
- Update records
- Delete records
- Search nation performance

---

## SQL - python practice.py

### Display Records

- Display complete dataset
- Display selected number of records

### Update Records

- Update selected economic indicators

### Delete Records

- Delete records based on user input

### Search Nation Performance

Display complete economic history of a selected nation.

### Ranking System

Generate rankings based on:

- GDP Growth %
- GNI (Billion USD)
- Imports % GDP
- Exports % GDP
- Literacy Rate %
- Life Expectancy

for any selected year.

---

# Recent Updates

The latest implementation introduces several improvements over the original version.

### New Features

- Dynamic extraction of column names using `cursor.description`
- Automatic table header generation
- Dynamic table formatting for queries returning different numbers of columns
- Dictionary-driven input collection for record insertion
- Improved ranking system with user-selected economic indicators
- Row count verification after UPDATE and DELETE operations
- Enhanced input validation
- Cleaner console output formatting
- Improved code modularity and maintainability

### Repository Updates

- Added Power BI dashboard and report files
- Uploaded synthetic dataset files (.csv and .xlsx)
- Included SQL database dump used as the Power BI data source
- Updated project documentation
- Improved repository organization

---

# Prerequisites

## For GGI.py

No existing database is required.

The program automatically creates:

- Database
- Tables
- Schema

before performing CRUD operations.

---

## For SQL - python GGI Dynamic Version.py

An existing MySQL database is required.

Database Name

```
gross_global_index
```

Table Name

```
ggi dataset
```

The program performs operations on the existing dataset stored in the MySQL environment.

---

# Key Concepts Applied

- Database Management System (DBMS)
- SQL CRUD Operations
- Python-MySQL Integration
- Cursor Metadata (`cursor.description`)
- Dynamic SQL Query Execution
- Dictionary-based Data Collection
- Dynamic Console Table Formatting
- Ranking Algorithms
- Comparative Economic Analysis
- Exception Handling
- Data Visualization
- SQL Database Integration
- Power BI Dashboard Development

---

# Application Screenshots
GGI.py
<img width="1347" height="896" alt="Screenshot 2026-06-30 151830" src="https://github.com/user-attachments/assets/352210f6-0091-4fca-b27b-49bdabc9f77e" />
SQL- python GGI Dynamic Version.py 
<img width="2087" height="1112" alt="Picture3" src="https://github.com/user-attachments/assets/ab839c87-b0f8-4660-8c3c-3e84b54aae97" />
<img width="1866" height="879" alt="Picture2" src="https://github.com/user-attachments/assets/c66ec5c6-8b40-4f35-853e-37e147e75fa1" />




---

# Installation & Execution

## Clone Repository

```bash
git clone https://github.com/yourusername/gross-global-index-system.git
```

## Install Dependencies

```bash
pip install mysql-connector-python
```

## Database Password

Before running either program, replace:

```python
password="YOUR_PASSWORD"
```

with your local MySQL password.

## Run Project

```bash
python GGI.py
```

or

```bash
python "SQL - python GGI Dynamic Version.py"
```

---

# Workflow

Synthetic Data Generation → MySQL Database → Python CRUD & Analysis Application → Power BI Dashboard → GitHub Repository

---

# Author

**Avani Sharma**

---

# License

This project was developed for academic learning and portfolio purposes.
---
