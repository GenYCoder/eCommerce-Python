eCommerce-Python
================

Basic eCommerce Program using CRUD on command line
Purpose: The program will let users make an account or sign in to let them buy products. The primary purpose is to let users browse around the store and finding products they would like to buy. It is a transaction program. Included is an administrator mode where the owner can look up customers, add products, remove them, or modify them. The program will keep track on the items being purchased by customers using a database. 

How it works: The program allows users to make an account to login. The users should be able to browse around the products that are being sold through the database. After they pick out all their products they want to buy they can go to the checkout area in the shopping cart. There the user can finish the transaction of purchasing the product. Depending on what the user selected, program will respond accordingly like updating the database. There is also an administrator mode where the admin can add products, remove, modify, or look up customer information using the database. 

The tables that are used in making this program: There are 5 tables in the database used with python to make the program behave as it does.

USER TABLE
create table users(
cust_id smallint unsigned auto_increment,
username varchar(30),
password varchar(20),
primary key(cust_id));

PRODUCTS TABLE
create table products(
product_id smallint unsigned auto_increment,
item_name varchar(100),
item_type varchar(50),
price float(10,2) unsigned,
quantity smallint,
instock enum(‘yes’,’no’)
primary key(product_id));

ADDRESS TABLE
create table address(
cust_id smallint unsigned,
fname varchar(30),
lname varchar(30),
gender enum(‘male’,’femail’),
birth_date date,
street varchar(40),
city varchar(20),
state varchar(30),
postal_code varchar(6),
foreign key(cust_id) references users(cust_id));

ORDERS TABLE
create table orders(
cust_id smallint unsigned,
product_id small int unsigned,
item_type varchar(50),
price float(10,2) unsigned,
quantity smallint,
date_submit datetime,
paid enum(‘YES’,’NO’)
foreign key(cust_id) references users(cust_id),
foreign key(product_id) references product(product_id));


PAYMENT TABLE
create table payment(
cust_id smallint unsigned,
card_number varchar(20),
cardtype varchar(20),
expcode varchar(5),
securitycode varchar(3),
primary key(cust_id, card_number),
foreign key(cust_id) references users(cust_id));

How to use this program:
When the business program first starts up it asks the user to either sign in or register for an account. If the user didn’t make an account before the program will ask the user to enter information for a new customer. After logging or registering for a new account, the user is then shown a list of categories to choose from. The last part of the categories is always the shopping cart. The user can navigate to the program and select the following number. There is an error checking option so they user will have to select a number that is shown on the screen. After they pick a category of a product type, they are shown with all the items of that type. They have 3 options to choose from. They can buy the item, search for an item, or go back to the category screen. If they select buy they are ask to choose from an item on the product based on that type. There is also an error check in place so they won’t choose a number that doesn’t appear on the list. After choosing the item, they are asked how much they want to buy and the program will automatically go to the product table. If the user chooses search for an item, the program will ask them to enter a search term and it will go find that term based on the product type in the page. After buying they can go to the shopping cart section of the program. It will show them what they have in the cart, how many items in the cart, and the grand total. They have 3 options to choose from, such as checkout, remove item, and continue shopping. The remove item option allows the user to remove the item from the cart if they don’t want the item and updates the database accordingly. If they select to buy them item they should be given a message that their order went through the database and their transaction was completed. They can shop more if they want to. 

Administrator mode:
In the administrator mode of the program the owner can add, remove, modify, and check up customer inquiries. To access it the program will need to enter the username administrator and will need to enter the password to get into that mode, which is ‘backdoor’. The program is already encrypted so it will be difficult to find the password in administrator mode, because there is no decompiler program yet. In the add product option the owner would need to enter information of that product. After the information is entered the product should be in the products table. The  second option is removing products. The owner can enter a single number or multiple number to remove the products. For example ‘4’ would remove the product that has the product_id = 4 or ‘1 2 3’ would remove products that have the product ids of 1 2 and 3. The modifying product option lets the user modify the products in the product table. The program will ask what part they want to modify and the owner would have to answer yes of they want to modify that part or no if they don’t want to. Then they are asked to select what product they want to modify through their numbers. The owner can enter multiple numbers such as ‘1 2 3 4’ and the program will loop to ask them what they want to modify and the program will modify it. In the customer invoice option in the administrator mode program, the owner can look up the orders of the customer or the address. They would need to enter the information in so if it matches with the database it will show the display the customer information. 


User functions:
Welcome()
Quotes(s)
Loadcategory()
Errorcheckchoice(keylist)
Users()
Displaycategory()
Shoppingcart()
Displayitem()
Buyitems()

Administrator functions:
Quotes(s)
addProducts()
removeProducts()
modifyProducts()
customerInvoice()
mainloop(password)

