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
	#print 'Test connection successfull !'                 	      
except MySQLdb.Error as e:
	print e
	sys.exit()

#On successful connection create a cursor for all the database operations

cur = db.cursor()

'''Processing based on the different options chosen from the main menu
Re-used some exception handling statements for MySQL from old code due to lack of time'''

#Unless user wants to exit keep processing and keep displaying menu after every operation
while menu_choice !=6:
	
	if menu_choice==1:   #Update the running inventory with the stock
		showInventoryUpdateMenu()
		while inventory_menu_choice !=5:
			if inventory_menu_choice==1:
				quantity=getInput()
				fid=1
			elif inventory_menu_choice==2:	
				quantity=getInput()
				fid=2
			elif inventory_menu_choice==3:	
				quantity=getInput()
				fid=3	
			elif inventory_menu_choice==4:	
				quantity=getInput()
				fid=4
			try:
				update_sql="""update running_inventory set food_qty=food_qty + %s where food_id=%s"""
				rows_affected=cur.execute(update_sql,(quantity,fid))
				if rows_affected > 0:
					db.commit()	
					print 'Updated the inventory successfully !'
					showInventoryUpdateMenu()
			except MySQLdb.Error as e:
				print e	
				logging.warn("Update failed !")
				sys.exit()	
	
		showMainMenu()
	
	 
	
	elif menu_choice==4:   #Display the running inventory details
		
		try:
			rows_affected=cur.execute("select * from running_inventory")
			if rows_affected > 0:
				for row in cur.fetchall():
					print row[0], row[1], row[2], row[3]
					print '============================='	
			showMainMenu()
		except MySQLdb.Error as e:
			print e
			logging.warn("select statement failed to execute.please check your query")
			sys.exit()
	elif menu_choice==5:   #Display the animal feed table details
		
		try:
			rows_affected=cur.execute("select * from animal_feed")
			if rows_affected > 0:
				for row in cur.fetchall():
					print row[0], row[1],row[2],row[3],row[4],row[5]
					print '=========================================='	
			showMainMenu()
		except MySQLdb.Error as e:
			print e
			logging.warn("select statement failed to execute.please check your query")
			sys.exit()		