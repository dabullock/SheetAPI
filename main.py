from sheet_api import *

fileName = raw_input("Enter Sheet Name: ")

site = raw_input("""
					  Choose Site:

					  1 = Adidas
					  2 = Nike

					  """)

if site == '2':
	password = raw_input("Enter Password to the accounts: ")
else:
	password = ''


pid = raw_input("Enter PID: ")

address = raw_input("Enter Address: ")

address2 = raw_input("Do you have a required Address2? [y/n]: ")

if address2 == 'y':
	address2 = raw_input("Enter Address 2: ")
elif address2 == 'n':
	address2 = ''

city = raw_input("Enter City: ")
state = raw_input("Enter State (spelled out): ")
zipCode = raw_input("Enter Postal code: ")
country = raw_input("Enter Country: ")

cardType = raw_input("Card Type: ")

amount = int(raw_input("Enter the amount of tasks for this sheet: "))

SheetWriter(fileName, site, password, pid, address, address2, city, state, zipCode, country, cardType, amount)

print "Sheet Created"

