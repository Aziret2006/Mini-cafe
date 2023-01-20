
from config import CAFE_ID, EMPLOYEE_ID, FOOD_ID, MENU_ID, ORDER_ID, RECEIPT_ID, SESSION_USER
from view import (crate_cafe, update_cafe, get_cafe, wrong_command,
                  create_employee, get_employee_info, create_food, get_current_user,
                  create_menu, create_order, create_receipt, show_menu)


def main():
    user = get_current_user(session_user=SESSION_USER)
    while True:
        action = input("""
                 Press 1 to show 1 show Menu
                 Press 2 to order
                 Press 3 to exit 
                 -> """)

        if action == '1':
            show_menu()
        elif action == '2':
            create_order(order_id=ORDER_ID, user=user)
        elif action == '3':
            print("Bye, bye!")
        elif action == '11':
            action = input("""
                          Enter 1 if you want create employee,
                          Enter 2 if you want update employee,      
                          Enter 3 to get info employee
                                  """)
            if action == '1':
                create_employee(emp_id=EMPLOYEE_ID)
            elif action == '2':
                pass
            elif action == '3':
                get_employee_info()
            else:
                wrong_command()
        elif action == '22':
            action = input("""
                          Enter 1 if you want create food,
                          Enter 2 if you want update food,      
                          Enter 3 to get info food
                                  """)
            if action == '1':
                pass
            elif action == '2':
                pass
            elif action == '3':
                pass
            else:
                wrong_command()
        elif action == '33':
            action = input("""
                        Enter 1 if you want create cafe,
                        Enter 2 if you want update cafe,      
                        Enter 3 to get info cafe
                                """)
            if action == '1':
                crate_cafe(cafe_id=CAFE_ID)
            elif action == '2':
                update_cafe()
            elif action == '3':
                get_cafe()
            else:
                wrong_command()
        elif action == '44':
            action = input("""
                          Enter 1 if you want create Menu,
                          Enter 2 if you want update Menu,      
                          Enter 3 to get info Menu
                                  """)
            if action == '1':
                create_menu(menu_id=MENU_ID, user=user)
            elif action == '2':
                pass
            elif action == '3':
                pass
            else:
                wrong_command()
        elif action == '55':
            action = input("""
                          Enter 1 if you want create receipt,
                          Enter 2 if you want update receipt,      
                          Enter 3 to get info receipt
                                  """)
            if action == '1':
                pass
            elif action == '2':
                pass
            elif action == '3':
                pass
            else:
                wrong_command()
        elif action == '66':
            break
        else:
           wrong_command()


if __name__ == '__main__':
    main()