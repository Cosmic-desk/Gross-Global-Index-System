import mysql.connector as mycon

con=mycon.connect(host="127.0.0.1",user="root",password="Your_Password",database="gross_global_index")

if con.is_connected():
           print("Yes Connected")

do=con.cursor(buffered=True)
    

#displaying data


def displaying_data(typ):
            

#1          display number of rows entered
            def count_data():
                number=int(input("Enter number of rows to be fetched "))
                st= "Select * from gross_global_index.`ggi dataset`;"
                do.execute(st)


                
                coloumn_names= tuple(col[0] for col in do.description) 
                
                print("~"*182)
                print("{:^3}| {:^10}| {:^20}| {:^15}| {:^20}| {:^20}| {:^15}| {:^20}| {:^20}| {:^20}|".format(*coloumn_names))                           # '*' unpacks the tuple/list
                print("~"*182)
                data = do.fetchmany(number)


                
                for row in data:
                    print("{:^3}| {:^10}| {:^20}| {:^15}| {:^20}| {:^20}| {:^15}| {:^20}| {:^20}| {:^20}|".format(*row))
                print("~"*182)




                
#2          display record of particular year    
            def year_data():
                year=int(input("Enter the year "))
                st= """
                select *
                from gross_global_index.`ggi dataset`
                where Year = %s"""
                do.execute(st,(year,))


                
                coloumn_names= tuple(col[0] for col in do.description)
                print("~"*182)
                print("{:^3}| {:^10}| {:^20}| {:^15}| {:^20}| {:^20}| {:^15}| {:^20}| {:^20}| {:^20}|".format(*coloumn_names))
                print("~"*182)


                
                data=do.fetchall()


                
                for row in data:
                    print("{:^3}| {:^10}| {:^20}| {:^15}| {:^20}| {:^20}| {:^15}| {:^20}| {:^20}| {:^20}|".format(*row))
                print("~"*182)
                if do.rowcount == 0:
                        print()
                        print("*"*182)
                        print("Record does not exist.")
                    
            if typ==1:
                count_data()

            elif typ==2:
                  year_data()
            else:
                  print("Please enter from range given")

                


        




#editing the data


def update_data():
    
    
            country_name=input("Enter Country name whose data you want to update : ")
            data_fields={1:"ID",
                         2:"Country Code",
                         3:"GDP Growth %" ,
                         4:"GNI(Billion USD)",
                         5:"Imports % GDP",
                         6:"Exports % GDP",
                         7:"Literacy Rate %",
                         8:"Life Expectancy"}

            for row in data_fields:
                print(row,data_fields[row])

            choice=int(input("Enter your choice for data to be updated in : "))
   

            col_name= data_fields[choice]
            
            year_num=int(input("Enter the year for whose data is to be updated : "))
            try:

                    if choice == 1 or choice == 2 :
                          new_val=int(input("Enter the new value : "))
                    else :
                          new_val=float(input("Enter the new value : "))
                          
                    query=(
                    "UPDATE gross_global_index.`ggi dataset` "
                    "SET `{}` = {} "
                    "WHERE Country = '{}' AND Year = {}".format(
                        col_name, new_val, country_name, year_num
                    ))
                    #print(query)
                    do.execute(query)
                    con.commit()     #commit belongs to connection object not to cursor object
                    if do.rowcount > 0:
                        print()
                        print("*"*182)
                        print("Record Successfully Updated")
                    else:
                        print()
                        print("*"*182)
                        print("Record not found.")

                    
            except ValueError as ve:
                    print()
                    print("*"*182)
                    print("Invalid Input.\n")
                    return
    
           

#Displaying Ranklist
def ranklist():
            year_num=int(input("Enter Year for performance display : "))
            print("Enter the parameter for ranklist from given fields : ")
            data_fields={1:"ID",
                         2:"Country",
                         3:"Country Code",
                         4:"GDP Growth %" ,
                         5:"GNI(Billion USD)",
                         6:"Imports % GDP",
                         7:"Exports % GDP",
                         8:"Literacy Rate %",
                         9:"Life Expectancy"}
            for row in data_fields:
                print(row,data_fields[row])
            print()
            para=int(input())
            par=data_fields[para]
            query="Select Country, `{}` from gross_global_index.`ggi dataset`  where Year={} order by `{}` DESC ;".format(par,year_num,par)
            print(query)
            do.execute(query)

            
            coloumn_name=tuple(col[0] for col in do.description)
            print("-"*44)
            print("|{:^20} |{:^20}|".format(*coloumn_name))
            print("-"*44)     
            data=do.fetchall()
            for row in data:
                    print("|{:^20} |{:^20}|".format(*row))
            print("-"*44)  

#Adding A data
def adding_data():
     try:
        print("The following fields needs to be added to create a new record")
        data_fields={1:"ID",
                     2:"Year",
                    3:"Country",
                    4:"Country Code",
                    5:"GDP Growth %" ,
                    6:"GNI(Billion USD)",
                    7:"Imports % GDP",
                    8:"Exports % GDP",
                    9:"Literacy Rate %",
                    10:"Life Expectancy"}
        dict_1={}
        for row in data_fields:
                print(row,data_fields[row])
                if row == 3:
                    val=input("Enter The name here : ")
                elif row < 5:
                    val=int(input("Enter The value here : "))
                else:
                    val=float(input("Enter The value here : "))

                
                dict_1[data_fields[row]]=val
        
        query = """
        INSERT INTO gross_global_index.`ggi dataset`
        VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
        """

        do.execute(query, tuple(dict_1.values()))
        con.commit()
        print()
        print("*"*182)
        print("Record Added Succesfully")
     except ValueError:
        print()
        print("*"*182)
        print("Invalid Input.\n")

#Deleting a record

def delete_a_record():
    year_num=int(input("Enter year for which you want deletion : "))
    country=input("Enter country name for deletion : ")
    do.execute("DELETE FROM gross_global_index.`ggi dataset` Where Year = {} AND COUNTRY = '{}'".format(year_num,country))
    con.commit()
    if do.rowcount == 0:
        print("No matching record found.")
    else:
        print("Record deleted successfully.")
    



#Searching a nation
    
def search_nation():
    nation_name=input("Enter Nation's name you want to search : ")
    do.execute("SELECT * FROM gross_global_index.`ggi dataset` WHERE COUNTRY = '{}'".format(nation_name))
    col_name=tuple(col[0] for col in do.description)
    print("~"*182)
    print("{:^3}| {:^10}| {:^20}| {:^15}| {:^20}| {:^20}| {:^15}| {:^20}| {:^20}| {:^20}|".format(*col_name))
    print("~"*182)

    data=do.fetchall()
    for row in data:
        print("{:^3}| {:^10}| {:^20}| {:^15}| {:^20}| {:^20}| {:^15}| {:^20}| {:^20}| {:^20}|".format(*row))
    print("~"*182)
    if do.rowcount == 0:
                        print()
                        print("*"*182)
                        print("Record does not exist.")

        
#Main
while(True):
    print()
    print()
    print("*"*182)
    print()
    print()
    print('''This program performs data management and analysis operations on an existing Global Economic Indicators dataset stored in MySQL.
           Prerequisites:
            - MySQL Server
            - Database: gross_global_index
            - Table: ggi dataset''')
    
    print()
    print()
    print("*"*182)
    print("You Can perform the following functions : ")
    print("1. Displaying Data")
    print("2. Updating Existing Record")
    print("3. Display Ranklist")
    print("4. Add New Record")
    print("5. Search A Nation")
    print("6. Delete a particlar record")
    print("7. Exit")
    print("*"*182)
    print()

    chose=int(input("Enter operation to perform as numbers : "))
    print()
    print("*"*182)

    if chose==1 :
        print()
        print()
        print("Existing number of records are : ")
        query=("Select count(ID) FROM gross_global_index.`ggi dataset`")
        do.execute(query)
        val=do.fetchone()
        print(val[0])
        print()
        print("Select the type of display ")
        print("1. By your entered number of rows")
        print("2. By your entered number of year")
        
        val=int(input("Enter your choice "))

        displaying_data(val)
        print()
        print()
    elif chose==2:
        update_data()
        print()
        
        print()
        print()
    elif chose==3:
        print()
        ranklist()
        print()
    elif chose==4:
        print()
        adding_data()
        print()
        
        print()
    elif chose==5:
        print()
        search_nation()
        print()
    elif chose==6:
        print()
        delete_a_record()
        
        print()
    elif chose==7:
        print("Terminated")
        break
    else:
        print("Unvalid Entry")
        print()
        print()


con.close()












        
