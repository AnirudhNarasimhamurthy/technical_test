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
	choice= int(raw_input('Enter a choice:'))
	
showMainMenu()	

#Check database connectivity

try:
	db = MySQLdb.connect(host="localhost",user="root",passwd="password",db="izi") 
	print 'Test connection successfull !'                 	      
except MySQLdb.Error as e:
	print e
	sys.exit()