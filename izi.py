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
	print '6. How much each individual animal fed per day on average'
	print '7. How many times per day are animals fed on average'
	print '8. Wastage details'
	print '9. Overfed and underfed detaisl'
	print '10. Exit'
	#print '\n Enter a choice'
	#menu_choice= int(raw_input('Enter a choice:'))
	menu_choice=getMenuChoice(0)
	

def showInventoryUpdateMenu():

	global inventory_menu_choice
	print '1. Update the running inventory with horse food quantity'
	print '2. Update the running inventory with zebra food quantity'
	print '3. Update the running inventory with lion food quantity'
	print '4. Update the running inventory with tiger food quantity'
	print '5. Exit'
	#inventory_menu_choice=int(raw_input('Enter a choice:'))
	inventory_menu_choice=getMenuChoice(1)
	


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


def getMenuChoice(flag):
      while 1:
         try:
            s = raw_input('Enter your choice: ')
         except KeyboardInterrupt:
            sys.exit()
         try:
            n = int(s)
            if flag==1:
            	if n > 5 or n < 1:
            		print 'Please enter a valid choice !'
            		#break
            	else:
            		return n
            elif flag==0:
            	if n > 10 or n < 1:
            		print 'Please enter a valid choice !'	
            	else:
            		return n		
         except ValueError, e:
            print e



            	
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
while menu_choice !=10:
	
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
	
	elif menu_choice==2: #Insert values into animal_feed and update running inventory
	
		insert_sql = """insert into animal_feed (animal_id, animal_name,f_id,qty, feeding_time,feeding_date) values (%s,%s,%s,%s,%s,%s)"""
		animalId=int(raw_input('Enter animal id:'))
		animalName=raw_input('Enter animal name:')
		fId=int(raw_input('fId: '))
		qty=int(raw_input('qty:'))
		feedTime= raw_input('Enter feed time (hh:mm:ss)') #21:30:45'
		feedDate= raw_input('Enter feed date (yyyy-mm-dd)') #2016-03-15'

		try:
			rows_affected = cur.execute(insert_sql, (animalId,animalName,fId,qty,feedTime,feedDate))
			#db.commit()
			logging.warn("%d", rows_affected)
			if rows_affected > 0:
				print('Record inserted successfully !')
			#If insert happens successfully correspondingly update the food quantity by subtracting it from running inventory
			update_sql="""update running_inventory set food_qty= food_qty - %s where food_id= %s"""
			new_qty=qty
			food_id=fId
			try:
				rows_affected = cur.execute(update_sql,(new_qty,food_id))
				if rows_affected > 0:
					db.commit()	 #If both insert and update are true commit the changes
					print 'Updated the inventory successfully !'
				
			except MySQLdb.Error as e:
				print e	
				db.rollback() #Rollback if insert succeeds and update fails
				logging.warn("Update failed !")
				sys.exit()
				
		except MySQLdb.IntegrityError as e:
			print e
			logging.warn("Failed to insert record !")
		#choice=getInput()
		showMainMenu()
		
		'''I am simplifying it here and assuming whatever the input given would be the value that will be updated. This is similar to the description in the problme where the worker manually enters the stock for syncing actual inventory and running inventory. I was thinking of doing this by taking value from actual inventory table but I don't have time'''
	
		'''Similar to the previous one except update here will be the actual input provided and not the input plus the previous value which was the case with 1'''
	elif menu_choice==3:  
		showInventoryUpdateMenu()
		while inventory_menu_choice !=5:
			if inventory_menu_choice==1:
				quantity=getInput()
				fid=1 #Setting the food id so that I can know which record needs to be updated
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
				update_sql="""update running_inventory set food_qty=%s where food_id=%s"""
				rows_affected=cur.execute(update_sql,(quantity,fid))
				if rows_affected > 0:
					db.commit()	
					print 'Updated the inventory successfully !'
					
			except MySQLdb.Error as e:
				print e	
				logging.warn("Update failed !")
				sys.exit()	
			showInventoryUpdateMenu()	
	 	showMainMenu()
	
	elif menu_choice==4:   #Display the running inventory details
		
		try:
			select_sql="select * from running_inventory"
			rows_affected=cur.execute(select_sql)
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
			select_sql="select * from animal_feed"
			rows_affected=cur.execute(select_sql)
			if rows_affected > 0:
				for row in cur.fetchall():
					print row[0], row[1],row[2],row[3],row[4],row[5]
					print '=========================================='	
			showMainMenu()
		except MySQLdb.Error as e:
			print e
			logging.warn("select statement failed to execute.please check your query")
			sys.exit()	
			
	elif menu_choice==6:   #Display how much each individual animal was fed per day on avg
		
		try:
			select_sql="select temp.animal_name, avg(temp.daily_qty) from ( select animal_name,sum(qty) as daily_qty from animal_feed group by animal_name, feeding_date)as temp group by temp.animal_name;"
			rows_affected=cur.execute(select_sql)
			if rows_affected > 0:
				for row in cur.fetchall():
					print row[0], row[1]
					print '=========================================='	
			showMainMenu()
		except MySQLdb.Error as e:
			print e
			logging.warn("select statement failed to execute.please check your query")
			sys.exit()		
	elif menu_choice==7:   #Display the animal feed table details
		
		try:
			select_sql="select * from animal_feed"
			rows_affected=cur.execute(select_sql)
			if rows_affected > 0:
				for row in cur.fetchall():
					print row[0], row[1],row[2],row[3],row[4],row[5]
					print '=========================================='	
			showMainMenu()
		except MySQLdb.Error as e:
			print e
			logging.warn("select statement failed to execute.please check your query")
			sys.exit()								