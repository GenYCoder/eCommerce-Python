import MySQLdb
from pyDes import *

k = des("DESCRYPT", CBC, "\0\0\0\0\0\0\0\0", pad=None, padmode=PAD_PKCS5)
options = {1:'Add Products', 2:'Remove Products', 3:'Modify Products', 4:'Customer Invoice'}

conn = MySQLdb.connect (
                        host = "localhost",
                        user = "root",
                        passwd = "root people know the password",
                        db = "business",
                        port = 3306)

main = conn.cursor()

#function use for single quoting strings in mysql
def quote(s):
    s = "'" + s + "'"
    return s

#adding the product function
def addProducts():
    #administrator input for new products
    itemName = input('Item name:').strip() 
    itemType = input('Item type:').upper().strip()
    price = float(input('Price:'))
    quantity = int(input('Quantity:'))
    
    #query use for inserting new products into mysql table for business
    query = ('INSERT INTO products VALUES(NULL, ' + quote(itemName) + ', ' + quote(itemType)
             + ', ' + str(price) + ', ' + str(quantity) + ', "yes")')
    main.execute(query)
    conn.commit()
    
    print('\nItem added into products table\n')

    return
    
#removing the products function    
def removeProducts():
    productList = {} #used for storing mysql data into the dictionary
    
    #query is used for selecting all the data within the products table
    query = 'SELECT * from products'
    main.execute(query)
    rows = main.fetchall()

    for row in rows: #loops through all the data and store them into productList dict
        productList[row[0]] = [row[0], row[1], row[2], row[3], row[4], row[5]]

    for key, value in productList.items(): #loops through productList dict and displays the products
        pattern = '{0:<6d}{1:60s}{2:<20s}${3:<7.2f}{4:6d}{5:>6s}'
        print(pattern.format(value[0],value[1],value[2],value[3],value[4], value[5]))

    print('Which products do you want to delete?')
    choices = input('Choice #:') #user can input a single number or multiple numbers following a space after it

    #this loops through the number choices that the user input and search whether the the choice was in the
    #productList. If it is then it deletes it. If not it displays choice does not exist
    for choice in choices.split():
        if int(choice) in productList:
            query = 'DELETE FROM products WHERE product_id = ' + choice
            main.execute(query)
            conn.commit()
        else:
            print('Choice #', choice, 'does not exist')

    return

#modifying the products function
def modifyProducts():
    productList = {}
    #a list of options to select for yes or no
    optionList = {'Item Name':'', 'Item Type':'', 'Price':'', 'Quantity':''}

    #query to select all the products
    query = 'SELECT * from products'
    main.execute(query)
    rows = main.fetchall()

    #display how the format of the text should be displayed
    pattern = '{0:<6d}{1:60s}{2:<20s}${3:<7.2f}{4:6d}{5:>6s}'

    for row in rows: #moving data from mysql table to python built in dictionary
        productList[row[0]] = [row[0], row[1], row[2], row[3], row[4], row[5]]

    for key, value in productList.items(): #loops and display the items in the productList
        print(pattern.format(value[0],value[1],value[2],value[3],value[4], value[5]))

    print('\nType in yes or no for what you want to modify')

    for options in optionList: #loops through the optionList and asking the user yes or no in which item they would like to modify
        print('Do you want to modify', options, '?')
        answer = input('Answer:').lower().strip()
        if answer == 'yes':
            optionList[options] = answer
        else:
            optionList[options] = 'no'

    #if no for all then get out of function
    if optionList['Item Name'] != 'yes' and optionList['Item Type'] != 'yes'and optionList['Price'] != 'yes' and optionList['Quantity'] != 'yes':
        return
        

    print()
    print('Which products do you want to modify')
    choices = input('Choice #:')

    #this loops the number of choices the user selected and modifying each one of them
    for choice in choices.split():
        query = 'UPDATE products SET'

        if int(choice) in productList:#condition to check if productID in productList
            #displays the item being modify 
            print()
            print('Modifying product#', choice)
            print(pattern.format(productList[int(choice)][0], productList[int(choice)][1], productList[int(choice)][2],
                                 productList[int(choice)][3], productList[int(choice)][4], productList[int(choice)][5]))

            #condition to combining string for each answer of yes
            if optionList['Item Name'] == 'yes': 
                itemName = input('Enter new item name:')
                query += ' item_name = ' + quote(itemName) + ', '
                
            if optionList['Item Type'] == 'yes':
                itemType = input('Enter new item type:')
                query += ' item_type = ' + quote(itemType) + ', '
                
            if optionList['Price'] == 'yes':
                Price = float(input('Enter new item price:'))
                query += ' price = ' + str(Price) + ', '
                
            if optionList['Quantity'] == 'yes':
                Quantity = int(input('Enter new quantity amount:'))
                query += ' quantity = ' + str(Quantity) + ', '

            query = query[:-2] #this gets rid of the comma in the end
            query += ' WHERE product_id = ' + choice
            main.execute(query)
            conn.commit()
            

            print('Finished modifying product #', choice)

    print()
    return

#query customers
def customerInvoice():
    #admin choices for customerInvoice function
    cOptions = {1:'Look up customer orders', 2:'Look up customer address', 3:'Exit'}
    print()

    while True: #format and displays cOptions
        for option in cOptions:
            pattern = '{0:4d}-{1}'
            print(pattern.format(option, cOptions[option]))

        while True: #input choice and error checker
                try:
                    while True:
                        choice = int(input('Choice #'))
                        if choice not in cOptions: #checks if option exists in cOptions
                            print('No option exists, please select another')
                        else:
                            break
                    break
                except ValueError: #choice must be a number
                    print('Please enter a number')

        if choice == 1: #Choice for looking up customer orders
            fname = input('Please enter first name of customer:')
            lname = input('Please enter last name of customer:')
            street = input('Please enter street:')
            city = input('Please enter city:')
            state = input('Please enter state:')
            country = input('Please enter country:')
            postal = input('Please enter postal code:')

            query = ('SELECT * from orders WHERE cust_id in (SELECT cust_id FROM address where fname regexp ' + quote(fname)
                     + ' AND lname regexp ' + quote(lname) + ' AND street regexp ' + quote(street) + ' AND city regexp ' + quote(city)
                     + ' AND state regexp ' + quote(state) + ' AND country regexp ' + quote(country)
                     + ' AND postal_code regexp ' + quote(postal) + ')')
            main.execute(query)
            rows = main.fetchall()

            print()
            if len(rows) == 0: #no rows diplay implies no matches found
                print('\nNo Matches Found\n')
            else:
                for row in rows: #format display 
                    pattern = '{0:<4d}{1:40s}{2:20s}{3:10.2f}{4:10d}{5:>27s}{6:>6s}'
                    print(pattern.format(row[0], row[2], row[3], row[4], row[5], row[6], row[7]))

        elif choice == 2: #choice to look up customer address
            fname = input('Please enter first name of customer:')
            lname = input('Please enter last name of customer:')
            birthDate = input('Please enter birthday:')

            #query to find customer address
            query = ('SELECT * FROM address where fname regexp ' + quote(fname) + ' AND lname regexp ' + quote(lname)
                     + ' AND birth_date regexp ' + quote(birthDate))
            main.execute(query)
            rows = main.fetchall()

            print()
            print('{0:<4s}{1:30s}{2:s}'.format('ID', 'Name', 'Address'))

            for row in rows: #displays the address of the customer
                pattern = '{0:<4d}{1:30s}{2:s}'
                address = row[5] + ' ' + row[6] + ' ' + row[7] + ' ' + row[8] + ' ' + row[9]
                name = row[1] + ' ' + row[2]
                print(pattern.format(row[0], name, address))
             

        elif choice == 3: #choice to exit customerinvoice function
            print()
            return
        
                 
        

#main option 
def mainloop(password):

    
    if k.decrypt(password) != k.decrypt(k.encrypt('backdoor')): #does not allow admin access if password is wrong
        print('Access Denied')
        return
    
    
    print('\nWelcome you are in administrator mode\n')


    while True: #loops the menu for administrator mode
        print('Please select the following option')

        for option in options:
            pattern = '{0:4d}-{1}'
            print(pattern.format(option, options[option]))

        while True: #input choice and error check for choice
            try:
                while True:
                    choice = int(input('Choice #'))
                    if choice not in options:
                        print('No option exists, please select another')
                    else:
                        break
                break
            except ValueError: 
                print('Please enter a number')

        if choice == 1: #for calling addProducts function
            addProducts()
        elif choice == 2: #for calling removeProducts function
            removeProducts()
        elif choice == 3: #for calling modifyProducts function
            modifyProducts()
        elif choice == 4: #for calling customerInvoice function
            customerInvoice()
        


    
    
    
    

    




    
    
        
    







