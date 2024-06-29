import cx_Oracle
import csv

# Database connection details
dsn = cx_Oracle.makedsn('localhost', '1521', service_name='orclpdb1')
connection = cx_Oracle.connect(user='username', password='password', dsn=dsn)

# Open a cursor to perform database operations
cursor = connection.cursor()

# Open the text file
with open('data.csv', 'r') as file:
    csv_reader = csv.reader(file)
    
    # Skip the header row if there is one
    next(csv_reader, None)
    
    # Iterate over each row in the CSV file
    for row in csv_reader:
        # Prepare the SQL query
        query = """
            INSERT INTO my_table (name, id, join_date)
            VALUES (:1, :2, TO_DATE(:3, 'MM/DD/YYYY'))
        """
        
        # Execute the query
        cursor.execute(query, row)

# Commit the transaction
connection.commit()

# Close the cursor and the connection
cursor.close()
connection.close()