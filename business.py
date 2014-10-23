import MySQLdb

class Business:
    grid = ''
    custID = 0
    userCategorychoice = 0
    itemSearch = ''
    itemList = {}
    main = ''
    conn = ''
    
    def __init__(self, hostname='localhost', username='root', password='root', database='business', portnumber=3306):
        Business.conn = MySQLdb.connect (
                        host = hostname,
                        user = username,
                        passwd = password,
                        db = database,
                        port = portnumber)

        Business.main = Business.conn.cursor()
        self.loadcategory()

    def welcome(self, message='Techie Store'):
        print('Welcome to the', message)
        print()

    def quote(self, s):
        self.s = "'" + s + "'"
        return self.s

    def loadcategory(self):
        count = 0
        
        Business.main.execute("select distinct item_type from products order by item_type")
        rows = Business.main.fetchall()

        while count < len(rows):
            Business.itemList[count] = rows[count][0]
            count += 1

        Business.itemList[count] = 'SHOPPING CART'

        #this print the grid line
        for num in range(115):  
            Business.grid += '='

        
    def displaycategory(self):
        print('\nPlease select the following categories')
        for item in Business.itemList:
            pattern = '{0:4d}-{1}'
            print(pattern.format(item, Business.itemList[item]))

        print('\nPlease select a choice')
       
        while True: #input choice and error checker
                try:
                    while True:
                        
                        choice = int(input('Choice:'))
                        if choice not in Business.itemList: 
                            print('No option exists, please select another')
                        else:
                            break
                    break
                except ValueError: #choice must be a number
                    print('Please enter a number')
            
        Business.userCategorychoice = choice
        #shopping cart option
        if choice == len(Business.itemList) - 1:
            self.shoppingcart()

        else:
            self.displayitem(choice)

        

    def displayitem(self, choice, regexp='NONE'):
        temp = {}
        decisions = {0:'Buy', 1:'Search', 2:'Go Back'} 
        counter = 0
        currentcategory = self.itemList[choice]


        if regexp != 'NONE': #will only enable if user is searching for an item
        #query used for finding an item
            query = ('SELECT item_name, price, quantity, in_stock FROM products WHERE item_type = '
                         + self.quote(Business.itemList[choice]) + ' AND item_name REGEXP ' + self.quote(Business.itemsearch))
            Business.main.execute(query)
            rows = Business.main.fetchall()

            if len(rows) == 0: #if there's nothing found
                print()
                print(Business.grid)
                print('No Matches Found')
                print(Business.grid)
                print()
                self.displaycategory()
        else: #if there's no search term it will show all the items
            query = 'select item_name, price, quantity, in_stock from products where item_type = ' + self.quote(Business.itemList[choice])
            Business.main.execute(query)
            rows = Business.main.fetchall()

        print(Business.grid)
        print('{0:40s}{1:36s}{2:10s}{3:10s}  {4:11s}'.format('Choice', 'Item Name', 'Price', 'Quantity', 'In Stock'))
        print(Business.grid)

        #displays the products
        for row in range(len(rows)):
            temp[counter] = rows[row][0]
            print('{0:4d}     |{1:60s}  |   {2:.2f}   |{3:6d}    |   {4:3s}'.format(counter, rows[row][0], rows[row][1],rows[row][2],rows[row][3]))
            counter += 1

        print()
        print()
        print('What would you like to do')
        for decision in decisions:
            pattern = '{0:4d}-{1}'
            print(pattern.format(decision, decisions[decision]))
        
        
        while True: #input choice and error checker
            try:
                while True:
                    choice = int(input('Choice:'))
                    if choice not in decisions: 
                        print('No option exists, please select another')
                    else:
                        break
                break
            except ValueError: #choice must be a number
                print('Please enter a number')
    
        if choice == 0: #if selected ask the user what item to buy and how many
            print()
            print('what item do you want to buy?')

            itemchoice = int(input('Enter choice #:')) 
            while itemchoice > len(rows) - 1 or itemchoice < 0: #keeps looping if there's no item for that choice
                print('Warning no item choice of that selection. Please select another')
                itemchoice = int(input('choice #:'))
            
            amount = int(input('How many do you want to buy:'))
            
            self.buyitems(temp[itemchoice], amount, currentcategory)

        elif choice == 1: #option for searching a term
            Business.itemsearch = input('Enter a search term:')
            while len(Business.itemsearch) == 0: #if the user enter nothing for search term it will ask them to enter something
                Business.itemsearch = input('You enter nothing please enter a search term:')

            self.displayitem(Business.userCategorychoice, Business.itemsearch) #calls back the function again for searching the term
            
            
        elif choice == 2: #for displaying category again
            self.displaycategory()


    def buyitems(self, choice, quantity, categorychoice):
        newList = True

        #shows everything in the product table where item_name and item_type are the same from what the user pick
        query = 'SELECT * FROM products WHERE item_name = ' + self.quote(choice) + ' AND item_type = ' + self.quote(categorychoice)
        Business.main.execute(query)
        rows = Business.main.fetchall()

        #moving mysql data into python variables
        productID = str(rows[0][0])
        dbQuantity = rows[0][4]
        price = str(rows[0][3])
        
       
        #checks quantity in mysql and user input
        while quantity > dbQuantity:
            print('The value you enter exceeds the quantity amount in our Store')
            quantity = int(input('Pleae enter another amount:'))

        query = 'SELECT product_id, quantity from orders where cust_id = ' + str(Business.custID) + ' AND paid = "NO"'
        Business.main.execute(query)
        rows = Business.main.fetchall()

        
        temporarycontainer = [[int(row[0]), int(row[1])] for row in rows]
        
        #this checks to see if the items is already in order list. If so updates it rather than add a new one. 
        for number in range(len(temporarycontainer)):
            if int(productID) == temporarycontainer[number][0]:
                temporarycontainer[number][1] = quantity + temporarycontainer[number][1]
                query = ('UPDATE orders SET quantity = ' + str(temporarycontainer[number][1]) + ' WHERE product_id = '
                         + productID + ' AND cust_id = ' + str(Business.custID) + ' AND paid = "NO"') 
                Business.main.execute(query)
                Business.conn.commit()
                newList = False
                break
                        
                
            
        #this is for adding new item into shopping cart
        while(newList):
            timeformat = '%c-%d-%Y at %h:%i%p' #MM DD YYYY at HH:MM PM/AM
            #query to insert items the user brought
            query = 'INSERT INTO orders VALUES(' + (str(Business.custID) + ', ' + productID + ', ' + self.quote(choice) +  ', ' + self.quote(categorychoice)
                                                    + ', ' + price + ', ' +  str(quantity) + ', ' + 'date_format(now(),' +
                                                    self.quote(timeformat) + '), "NO")')
          
            Business.main.execute(query)
            Business.conn.commit()
            newList = False #for stopping the loop

        #change the quantity amount in the db
        quantity = dbQuantity - quantity
                
        #updating the products in the database
        if quantity == 0:
            #changing the in_stock into no if there's 0 in the quantity
            query = 'UPDATE products SET quantity = ' + str(quantity) + ',  in_stock = "no" WHERE item_name = ' + self.quote(choice) + ' AND item_type = ' + self.quote(categorychoice)
            Business.main.execute(query)
            Business.conn.commit()
        else: #if there's items then it's in stock
            query = 'UPDATE products SET quantity = ' + str(quantity) + ', in_stock = "yes" WHERE item_name = ' + self.quote(choice) + ' AND item_type = ' + self.quote(categorychoice)
            Business.main.execute(query)
            Business.conn.commit()

        print()
        self.displaycategory()

    #function for the shopping cart storage. 
    def shoppingcart(self):
        items = {} 
        totalAmount = 0 #amount of all items
        totalItems = 0 #number of items in total
        number = 0 #used for choice data
        shoppingchoice = {0:'Checkout',1:'Remove Item',2:'Continue Shopping'}

        #query for extracting data that the customer brought based on customer ID
        query = ('SELECT item_name, item_type, price, quantity, date_submit, product_id FROM orders WHERE cust_id = '
                 + self.quote(str(Business.custID)) + ' AND paid = "NO"')  
        Business.main.execute(query)
        rows = Business.main.fetchall()

        #format of the display for shopping cart
        print()
        print(Business.grid)
        print('{0:8s}{1:40s}{2:20s}{3:>10s}{4:>14s}{5:>20s}'.format('Item#','Item Name','Item Type','Price','Quantity','Time Submitted'))
        print(Business.grid)

        for row in rows:
            totalAmount += row[2] * row[3]
            totalItems += row[3]
            items[number] = row[5]
            print('{0:<8d}{1:40s}{2:20s}{3:10.2f}{4:10d}{5:>27s}'.format(number, row[0],row[1],row[2],row[3],row[4]))
            number += 1

        print()
        print('{0:>104s}{1}'.format('Total Items:', totalItems))
        print('{0:>105s}{1:>.2f}'.format('Grand Total:$',totalAmount))

        while(True): 
            print('What would you like to do')
            
            for number in shoppingchoice:
                print('{0:2d}-{1}'.format(number, shoppingchoice[number]))

            while True: #input choice and error checker
                try:
                    while True:
                        choice = int(input('Choice:'))
                        if choice not in shoppingchoice: 
                            print('No option exists, please select another')
                        else:
                            break
                    break
                except ValueError: #choice must be a number
                    print('Please enter a number')
                

            choice = int(input('Choice:'))

            if choice == 0: #option for checking out 
                if len(items) == 0: #no items implies no checkout
                    print()
                    print('There is nothing to check out \n')
                else: #confirmation for checkout
                    #query used for finding the customer address
                    query = 'SELECT fname, street, city, state, postal_code FROM address WHERE cust_id = ' + str(Business.custID)
                    Business.main.execute(query)
                    rows = Business.main.fetchall()
                    print()
                    print(Business.grid)
                    print('Thank you for shopping with us', rows[0][0], '\n')
                    
                    print('Your order will be shipped to:')
                    print(rows[0][1])
                    print(rows[0][2], rows[0][3], rows[0][4], '\n')
                    print(Business.grid)

                    #used for updating the customer orders if they paid 
                    query = 'UPDATE orders set paid = "YES" where cust_id = ' + str(Business.custID) + ' AND paid = "NO"'
                    Business.main.execute(query)
                    Business.conn.commit()

                    self.displaycategory()

                
            elif choice == 1: #this removes the item and add on to the product table quantity from # of removal
                print('What item from item# do you want to remove?')
                itemchoice = int(input('Item#:')) #input for which item they want to remove

                if itemchoice > len(items) - 1: #error checker if item# not in the cart
                    print()
                    print('ERROR! ITEM# NOT IN CART')
                else: 
                    #getting the quantity amount from the orders
                    query = ('SELECT quantity FROM orders where product_id = ' +
                             str(items[itemchoice]) + ' AND cust_id = ' + str(Business.custID) +
                             ' AND paid = "NO"')
                    Business.main.execute(query)
                    rows = Business.main.fetchall()
                    quantityamount = rows[0][0] #updating the quantity amount based on data extraction in mysql

                    #updates quantity in products table
                    query = 'SELECT quantity FROM products where product_id = ' + str(items[itemchoice])
                    Business.main.execute(query)
                    rows = Business.main.fetchall()
                    productquantity = rows[0][0]

                    #updating the quantity in products table
                    query = 'UPDATE products SET quantity = ' + str(productquantity + quantityamount) + ' WHERE product_id = ' + str(items[itemchoice])
                    Business.main.execute(query)
                    Business.conn.commit()

                    #deleting the orders in mysql based on product id number the user picked
                    query = 'DELETE from orders WHERE product_id = ' + str(items[itemchoice]) + ' AND cust_id = ' + str(Business.custID)
                    Business.main.execute(query)
                    Business.conn.commit()

                    self.shoppingcart() #displaying the shopping cart again
                    
                    
            elif choice == 2: #going back to display the category
                print()
                self.displaycategory()

    def users(self):
        self.welcome()
        options = {0:'Sign In', 1:'Register'}
        storage = [] #temporary storage for username
        
        #query to select all data from users table
        query = 'SELECT * FROM users'
        Business.main.execute(query)
        rows = Business.main.fetchall()

        for row in rows: #adding data from users table to storage array
            storage.append(row[1])
            
        print('Please select the following from below')

        for option in options: #format display for users
            pattern = '{0:4d}-{1}'
            print(pattern.format(option, options[option]))
            
        
        choice = int(input('choice:'))

        if choice == 0: #sign in
            
            username = input('UserName:')

            #if username == 'administrator': #secret access to administrator mode
                #password = input('Enter password for administrative access:')
                #d = k.encrypt(password)
                #administratormode.mainloop(d)
            #else:
            password = input('PassWord:')

            #query for finding the cust_id based on the username and password
            query = 'SELECT cust_id from users WHERE username = ' + self.quote(username) + ' AND password = ' + self.quote(password)
            Business.main.execute(query)
            rows = Business.main.fetchall()

            
            if len(rows) == 0: #when the result is nothing
                print('There is no existing account\n')
                self.users()
            elif len(rows) == 1: #if there's a result 
                print()
                Business.custID = rows[0][0] #set custID based on the query
                print('Welcome Back')
                self.displaycategory()

        elif choice == 1: # registering a new user
            while True: #checks if a username was taken and ask to enter a different one
                username = input('UserName:')
                if username in storage:
                    print('UserName already taken. Please select something else')
                elif username not in storage:
                    break
            password = input('Password:')
            query = 'INSERT INTO users VALUES(NULL, ' + self.quote(username) + ', ' + self.quote(password) + ')'
            Business.main.execute(query)
            Business.conn.commit()

            query = 'SELECT cust_id from users WHERE username = ' + self.quote(username) + ' AND password = ' + self.quote(password)
            Business.main.execute(query)
            rows = Business.main.fetchall()

            Business.custID = rows[0][0]
           
            print()
            print('Please input the following infomation')
            fname = input('First Name:')
            lname = input('Last Name:')

            gender = input('Gender (please enter male or female):') 
            while gender != 'male' and gender != 'female': #error check to make sure they enter male or female
                gender = input('invalid entry. please enter male or female')

            #input data for address    
            birthdate = input('Birthdate (please enter in this format YYYY-MM-DD):')
            street = input('Street:')
            city = input('City:')
            state = input('State:')
            country = input('Country:')
            postal_code = input('Postal Code:')

            #inserting address data into mysql
            query = 'INSERT INTO address VALUES(' + (str(self.custID) + ', ' + self.quote(fname) + ', ' + self.quote(lname) + ', ' + self.quote(gender) + ', ' + self.quote(birthdate)
                                                     + ', ' + self.quote(street) + ', ' + self.quote(city) + ', ' + self.quote(state) + ', ' + self.quote(country) + ', '
                                                     + self.quote(postal_code) + ')')
            
            Business.main.execute(query)
            Business.conn.commit()

            print()
            print('Please enter credit information')

            #input data for credit card information
            card_number = input('Card Number:')
            cardtype = input('Card Type(visa, mastercard, etc):')
            expcode = input('ExpCode:')
            security = input('SecurityCode:')

            #inputing credit card information into mysql
            query = 'INSERT INTO payment VALUES(' + (str(self.custID) + ', ' + self.quote(card_number) + ', ' + self.quote(cardtype) + ', ' +
                                                     self.quote(expcode) + ', ' + self.quote(security) + ')')

            Business.main.execute(query)
            Business.conn.commit()

            print()
            print('Thank you for registering from our store')
            self.displaycategory()
                
            
            
        


test = Business()
test.users()

        


        
