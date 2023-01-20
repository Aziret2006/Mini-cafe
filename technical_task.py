# 1. Create some class (min 5 attr , min 3 methods)(create 5 class objects should be privade)
#
#


# Project name
# Mini cafe

# Purpose: create a solution to change R-keeper to own cafe system

# cafe
# Employee
# Food
# Menu
# Order
# Receipt

# Cafe
# - Name
# - addres
# - phone number
# - work start date
# - work end date
# - SERVERS percent (default - 8.05 %)
# - status (Work, Unwork, Repair, Cleaning day)
# - is active (True, False)
# - create date
# - update date


# Employee
# - id
# - Cafe ID
# - Last_name
# - First name
# - phone number
# - password
# - date of birth
# - passport id
# - status (Work, Unwork, Sick, Decree, Dismissed, Holiday)
# - work start date
# - work end date


# Food
# - id
# - name
# - image
# - description
# - price (10.00)
# - weight (gram)
# - category (First, Second, Candy, Hot drink, Drink, Breakfast, Salad, Snacks)
# - employee id
# - create date
# - update date

# Menu
# - id
# - name
# - [food_id, food_id]
# - start date
# - end date
# - is active( True, False )
# - employee id
# create date
# update date

# Order
# - id
# - employee id
# - foods [
#    [food_id, quantity],
#    [food_id, 3]
# ]
# - total
# - cafe id
# - create date
# - update date

# Receipt
# - id
# - order id
# - status (Payed, Unpayed, Rejection, Free)
# - create date
# - update date

# Cafe, Employee, Food, Menu
# - Create
# - Update

# Order, Receipt
# - Create


# Bussness process
# It s command for client
# 1 Show menu (by categoties)
# 2 Create order
#      get food and quontity
#      after order create show to client order detail
#      after order create automaticly create receipt

# It s command for employee
# 11 Create Employee or update
# 22 Create Food or update
# 33 Create Cafe or update
# 44 Create Menu or update
# 55 break
# 66 Update receipt status (order id)

# Google help, Internet help
