import psycopg2
import csv

# Connect to the database
conn = psycopg2.connect(host='127.0.0.1', user='postgres', password='root', dbname='DBProject')

# Create a cursor
cur = conn.cursor()

# Execute a SELECT statement to retrieve the data
cur.execute("SELECT * FROM incident")

# Fetch all rows from the cursor
rows = cur.fetchall()

# Open a CSV file for writing
with open('data_quality_result.csv', 'w', newline='') as csvfile:
  # Create a CSV writer
  writer = csv.writer(csvfile)

  # Write the header row
  writer.writerow(['column1', 'column2', 'column3'])

  # Write the data rows
  for row in rows:
    writer.writerow(row)

# Close the cursor and connection
cur.close()
conn.close()
