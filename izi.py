import MySQLdb
import sys
import logging

def showMainMenu():

	global menu_choice
	print '1. Update the running inventory with the shipment arrival'
	print '2. Enter the feeding times and quantity and update running inventory'
	print '3. Adjust the running inventory'
	print '4. Display running inventory'
	print '5. Display animal feed table'
	print '6. Exit'
	#print '\n Enter a choice'
	menu_choice= int(raw_input('Enter a choice:'))
	

def showInventoryUpdateMenu():

	global inventory_menu_choice
	print '1. Update the running inventory with horse food quantity'
	print '2. Update the running inventory with zebra food quantity'
	print '3. Update the running inventory with lion food quantity'
	print '4. Update the running inventory with tiger food quantity'
	print '5. Exit'
	inventory_menu_choice=int(raw_input('Enter a choice:'))
	


#Citation : Error handling code in try and except is something I had used for another assignment and I am using it here #

def getInput():   #Function to get integer inputs 
      while 1:
         try:
            s = raw_input('Enter your input: ')
         except KeyboardInterrupt:
            sys.exit()
         try:
            n = int(s)
         except ValueError, e:
            print e
         else:
            return n

	
showMainMenu()	

#Check database connectivity

try:
	db = MySQLdb.connect(host="localhost",user="root",passwd="password",db="izi") 
	print 'Test connection successfull !'                 	      
except MySQLdb.Error as e:
	print e
	sys.exit()

#On successful connection create a cursor for all the database operations

cur = db.cursor()


#Processing based on the different options chosen from the main menu #


#Unless user wants to exit keep processing and keep displaying menu after every operation
while menu_choice !=6:
	
	if menu_choice==1:
		showInventoryUpdateMenu()
	


	