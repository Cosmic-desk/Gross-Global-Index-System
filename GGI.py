
import mysql.connector

# =========================================================
# DATABASE CONNECTION
# =========================================================

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="YOURPASSWD",
    database="gross_global_index"
)

cursor = db.cursor()

if db.is_connected():
    print("Database connection successful.\n")


# =========================================================
# CREATE MAIN TABLE
# =========================================================

create_table_query = """
CREATE TABLE IF NOT EXISTS global_index (
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
)
"""

cursor.execute(create_table_query)
db.commit()


# =========================================================
# DISPLAY FUNCTION
# =========================================================

def display_table(data):

    headers = [
        "Year",
        "Nation",
        "Code",
        "GDP",
        "GNP",
        "Imports",
        "Exports",
        "Literacy",
        "Life Expectancy"
    ]

    print("-" * 140)

    print(
        "{:<10} {:<20} {:<10} {:<12} {:<12} {:<12} {:<12} {:<12} {:<15}".format(
            *headers
        )
    )

    print("-" * 140)

    for row in data:
        print(
            "{:<10} {:<20} {:<10} {:<12} {:<12} {:<12} {:<12} {:<12} {:<15}".format(
                *row
            )
        )

    print("-" * 140)


# =========================================================
# ADD DATA
# =========================================================

def add_record():

    try:

        year_recorded = int(input("Enter Year : "))
        nation_name = input("Enter Nation Name : ").title()
        nation_code = int(input("Enter Nation Code : "))

        gdp_growth = float(input("Enter GDP Growth (%) : "))
        gnp_value = float(input("Enter GNP Value (Trillion $) : "))
        imports_percent = float(input("Enter Imports (%) : "))
        exports_percent = float(input("Enter Exports (%) : "))
        literacy_rate = float(input("Enter Literacy Rate (%) : "))
        life_expectancy = float(input("Enter Life Expectancy : "))

        insert_query = """
        INSERT INTO global_index
        (
            year_recorded,
            nation_name,
            nation_code,
            gdp_growth,
            gnp_value,
            imports_percent,
            exports_percent,
            literacy_rate,
            life_expectancy
        )
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
        """

        values = (
            year_recorded,
            nation_name,
            nation_code,
            gdp_growth,
            gnp_value,
            imports_percent,
            exports_percent,
            literacy_rate,
            life_expectancy
        )

        cursor.execute(insert_query, values)
        db.commit()

        print("\nData inserted successfully.\n")

    except mysql.connector.Error as err:
        print("Database Error :", err)

    except ValueError:
        print("Invalid Input.\n")


# =========================================================
# DISPLAY ALL DATA
# =========================================================

def display_all_records():

    try:

        query = """
        SELECT
            year_recorded,
            nation_name,
            nation_code,
            gdp_growth,
            gnp_value,
            imports_percent,
            exports_percent,
            literacy_rate,
            life_expectancy
        FROM global_index
        """

        cursor.execute(query)

        records = cursor.fetchall()

        if records:
            display_table(records)
        else:
            print("No records found.\n")

    except mysql.connector.Error as err:
        print("Database Error :", err)


# =========================================================
# UPDATE DATA
# =========================================================

def update_record():

    try:

        nation_code = int(input("Enter Nation Code : "))

        print("\nSELECT FIELD TO UPDATE")
        print("1. GDP")
        print("2. GNP")
        print("3. Imports")
        print("4. Exports")
        print("5. Literacy Rate")
        print("6. Life Expectancy")

        choice = int(input("Enter Choice : "))

        field_mapping = {
            1: "gdp_growth",
            2: "gnp_value",
            3: "imports_percent",
            4: "exports_percent",
            5: "literacy_rate",
            6: "life_expectancy"
        }

        if choice not in field_mapping:
            print("Invalid Choice.\n")
            return

        new_value = float(input("Enter New Value : "))

        column_name = field_mapping[choice]

        update_query = f"""
        UPDATE global_index
        SET {column_name} = %s
        WHERE nation_code = %s
        """

        cursor.execute(update_query, (new_value, nation_code))
        db.commit()

        print("\nRecord updated successfully.\n")

    except mysql.connector.Error as err:
        print("Database Error :", err)

    except ValueError:
        print("Invalid Input.\n")


# =========================================================
# DELETE RECORD
# =========================================================

def delete_record():

    try:

        nation_code = int(input("Enter Nation Code to Delete : "))

        delete_query = """
        DELETE FROM global_index
        WHERE nation_code = %s
        """

        cursor.execute(delete_query, (nation_code,))
        db.commit()

        print("\nRecord deleted successfully.\n")

    except mysql.connector.Error as err:
        print("Database Error :", err)

    except ValueError:
        print("Invalid Input.\n")


# =========================================================
# SEARCH NATION OVER YEARS
# =========================================================

def search_nation():

    try:

        nation_code = int(input("Enter Nation Code : "))

        search_query = """
        SELECT
            year_recorded,
            nation_name,
            nation_code,
            gdp_growth,
            gnp_value,
            imports_percent,
            exports_percent,
            literacy_rate,
            life_expectancy
        FROM global_index
        WHERE nation_code = %s
        ORDER BY year_recorded
        """

        cursor.execute(search_query, (nation_code,))

        records = cursor.fetchall()

        if records:
            display_table(records)
        else:
            print("No records found.\n")

    except mysql.connector.Error as err:
        print("Database Error :", err)

    except ValueError:
        print("Invalid Input.\n")


# =========================================================
# RANKING SYSTEM
# =========================================================

def ranklist():

    try:

        print("\nSELECT RANKING CRITERIA")
        print("1. GDP")
        print("2. Literacy Rate")
        print("3. Life Expectancy")
        print("4. Exports")

        choice = int(input("Enter Choice : "))

        ranking_fields = {
            1: "gdp_growth",
            2: "literacy_rate",
            3: "life_expectancy",
            4: "exports_percent"
        }

        if choice not in ranking_fields:
            print("Invalid Choice.\n")
            return

        selected_field = ranking_fields[choice]

        query = f"""
        SELECT
            nation_name,
            {selected_field}
        FROM global_index
        ORDER BY {selected_field} DESC
        """

        cursor.execute(query)

        records = cursor.fetchall()

        print("\n" + "-" * 50)
        print("{:<10} {:<25} {:<10}".format("Rank", "Nation", "Value"))
        print("-" * 50)

        rank = 1

        for row in records:
            print("{:<10} {:<25} {:<10}".format(rank, row[0], row[1]))
            rank += 1

        print("-" * 50)

    except mysql.connector.Error as err:
        print("Database Error :", err)

    except ValueError:
        print("Invalid Input.\n")


# =========================================================
# MAIN MENU
# =========================================================

while True:

    print("\n")
    print("=" * 60)
    print("             GROSS GLOBAL INDEX SYSTEM")
    print("=" * 60)

    print("1. Add Nation Data")
    print("2. Display All Records")
    print("3. Update Record")
    print("4. Search Nation Performance")
    print("5. Ranking System")
    print("6. Delete Record")
    print("7. Exit")

    print("=" * 60)

    try:

        choice = int(input("Enter Your Choice : "))

        if choice == 1:
            add_record()

        elif choice == 2:
            display_all_records()

        elif choice == 3:
            update_record()

        elif choice == 4:
            search_nation()

        elif choice == 5:
            ranklist()

        elif choice == 6:
            delete_record()

        elif choice == 7:
            print("\nExiting Program...")
            break

        else:
            print("Invalid Choice.\n")

    except ValueError:
        print("Please enter numeric input only.\n")


# =========================================================
# CLOSE CONNECTION
# =========================================================

cursor.close()
db.close()

print("Database connection closed.")

