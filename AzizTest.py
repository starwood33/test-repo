import requests
import sqlite3
from getpass import getpass

# Connect to the SQLite database (it will be created if it doesn't exist)
conn = sqlite3.connect('customer_payments.db')
c = conn.cursor()

# Create table
c.execute('''CREATE TABLE IF NOT EXISTS payments
             (customer_name text, card_number text, expiry_date text, cvv text)''')

# Get customer payment information
customer_name = input("Enter customer name: ")
card_number = getpass("Enter card number: ")
expiry_date = input("Enter expiry date (MM/YY): ")
cvv = getpass("Enter CVV: ")

# Insert a row of data
c.execute("INSERT INTO payments VALUES (?,?,?,?)",
          (customer_name, card_number, expiry_date, cvv))

# Save (commit) the changes and close the connection to the database
conn.commit()
conn.close()

# Use the AzizServices API
api_key = 'sk_live_4eC39HqLyjWDarjtT1zdp7dcTYooMQauvdEDq54NiTphI7jx'
headers = {'Authorization': 'Bearer ' + api_key}
response = requests.get('https://api.azizservices.com/payments', headers=headers)

if response.status_code == 200:
    print("Payment information sent successfully!")
else:
    print("Failed to send payment information.")
