from validate import validate_name, validate_address, validate_phone_number, \
    validate_first_name, validate_last_name, validate_date_of_birth, validate_work_date, \
    validate_passport_id, validate_password, match_password, validate_image, \
    validate_description, validate_price, validate_weight, validate_status

from moduls import Cafe, Employee, Food, Menu, Order, Receipt
from database import CAFE, EMPLOYEE, FOOD, MENU, ORDER, RECEIPT, SESSION_USER
from datetime import datetime


#################################################

# Get current user

def get_current_user(session_user: dict):
    if session_user['user'] < 1:
        return Employee(
            id=0,
            cafe_id=1,
            first_name='Admin',
            last_name='Admin',
            phone_number='+996777222111',
            password='admin',
            date_of_birth='01.01.0001',
            passport_id='1111111',
            work_start_date='01.01.0001',
            work_end_date='31.12.2999',
        )
    return session_user['user']


#################################################


#################################################
# Cafe
def crate_cafe(cafe_id: dict):
    name = input("Enter cafe name: ")
    address = input("Enter address cafe: ")
    phone_number = input("Enter cafe phone number (0555770778): ")
    is_valid_name = validate_name(name=name)
    is_valid_address = validate_address(address=address)
    is_valid_phone_number = validate_phone_number(phone_number=phone_number)

    if all([is_valid_name, is_valid_address, is_valid_phone_number]):
        cafe = Cafe(
            id=cafe_id['id'],
            name=name,
            address=address,
            phone_number=phone_number
        )
        CAFE[cafe_id['id']] = cafe
        cafe_id['id'] += 1
        print("Cafe created success!")
    else:
        print("Incorrect value!")


def update_cafe():
    cafe_id = input("Enter cafe №: ")
    if cafe_id.isdigit():
        cafe = CAFE.get(int(cafe_id))
        if cafe is not None:
            help_text = ''
            all_attr = enumerate(cafe.__dict__.keys(), 1)
            all_attr = list(all_attr)
            for number, attr in all_attr:
                help_text += f"Enter {number} to update {attr}: \n"
            update_attr = input(help_text)
            if update_attr.isdigit() and len(all_attr) >= int(update_attr):
                index = int(update_attr) - 1
                attr = all_attr[index][-1]
                update_value = input("Enter new value: ")
                setattr(cafe, attr, update_value)
            else:
                print("Incorrect attr !")
        else:
            print("Cafe not found!")
    else:
        print("Incorrect ID!")


def get_cafe():
    cafe_id = input("Enter cafe №: ")
    if cafe_id.isdigit():
        cafe = CAFE.get(int(cafe_id))
        if cafe is not None:
            print(
                f"cafe name is {cafe.name}\n"
                f"Cafe address is {cafe.address}\n"
                f"Cafe phone number is {cafe.phone_number}\n"
                            )

        else:
            print("Cafe not found!")
    else:
        print("Incorrect ID!")


#################################################


#################################################
# Employee
def create_employee(emp_id: dict):
    first_name = input("Enter first name: ").strip()
    last_name = input("Enter last name: ").strip()
    date_of_birth = input("Enter date of birth (01.12.2004): ").strip()
    passport_id = input("Enter passport (ID/AN) (1234567): ").strip()
    phone_number = input("Enter cafe phone number (0555770778): ").strip()
    work_start_date = input("Enter start work date (23.01.2023): ").strip()
    work_end_date = input("Enter start end date (31.12.2024): ").strip()
    password_one = input("Enter password: ").strip()
    password_two = input("Confirm password: ").strip()
    is_valid_first_name = validate_first_name(first_name=first_name)
    is_valid_last_name = validate_last_name(last_name=last_name)
    is_valid_phone_number = validate_phone_number(phone_number=phone_number)
    is_valid_date_of_birth = validate_date_of_birth(date_of_birth=date_of_birth)
    is_valid_passport_id = validate_passport_id(passport_id=passport_id)
    is_valid_work_start_date = validate_work_date(work_date=work_start_date)
    is_valid_work_end_date = validate_work_date(work_date=work_end_date)
    is_valid_password = validate_password(password=password_one)
    is_match = match_password(password_one=password_one, password_two=password_two)
    if is_match:
        if all([is_valid_first_name, is_valid_last_name, is_valid_phone_number,
                is_valid_date_of_birth, is_valid_work_start_date, is_valid_passport_id,
                is_valid_work_end_date, is_valid_password]):
            employee = Employee(
                id=emp_id['id'],
                cafe_id=list(CAFE.keys())[0],
                first_name=first_name,
                last_name=last_name,
                date_of_birth=date_of_birth,
                passport_id=passport_id,
                password=password_two,
                phone_number=phone_number,
                work_start_date=work_start_date,
                work_end_date=work_end_date
            )
            EMPLOYEE[emp_id['id']] = employee
            emp_id['id'] += 1
            return print("Employee created success!")

        return print("Incorrect value!")
    return print("Password is missmatch")


def get_employee_info():
    employee_id = input("Enter employee №: ")
    if employee_id.isdigit():
        employee = EMPLOYEE.get(int(employee_id))
        if employee is not None:
            print(
                f"employee  ID: {employee.id}"
                f"Name is employee: {employee.first_name}\n "
                f"Last name: {employee.last_name}\n"
                f"Date of birth: {employee.date_of_birth}\n"
                f"Phone number: {employee.phone_number}\n"
                f"Started work in: {employee.work_start_date}\n"

            )

        return print("Employee not found!")
    return print("Incorrect ID!")
#################################################


#################################################

# Food

def create_food(food_id: dict, user: Employee):
    name = input("Enter food name: ")
    image = input("Enter image path! Example(/home/User/Pictures/Camera/IMG_7353.JPG):")
    description = input("Enter description")
    price = input("Enter food price: ")
    weight = input("Enter food weight: ")
    category = input(f"Choose category \n\n{FOOD.CATEGORY}: ")  # validate getting
    employee_id = user.id
    is_valid_name = validate_name(name=name)
    is_valid_image = validate_image(image=image)
    is_valid_description = validate_description(descriotion=description)
    is_valid_price = validate_price(price=price)
    is_valid_category = validate_status(
        status=category,
        EXAMPLE=Food.CATEGORY
    )
    if all([is_valid_name, is_valid_image, is_valid_description, is_valid_price, is_valid_category]):
        food = Food(
            id=food_id['id'],
            name=name,
            image=image,
            description=description,
            price=price,
            weight=weight,
            category=category,
            employee_id=employee_id
        )
        FOOD[food_id['id']] = food
        FOOD[food_id['id']] += 1
        return print("Food created success!")
    return print("Food is incorrect!")
#################################################


#################################################
# Menu
def create_menu(menu_id: dict, user: Employee):
    all_foods = FOOD

    name = input("Enter cafe name: ")
    print(f'\n\n{all_foods}\n\n')
    foods = input("Enter foods number 1,2,3: ")
    foods.split(',')
    start_date = input("Enter start date (23.13.2023): ")
    end_date = input("Enter start end date (23.13.2023): ")
    employee_id = user.id
    is_valid_name = validate_name(name=name)
    is_valid_foods = ...
    menu = Menu(
        id=menu_id['id'],
        name=name,
        foods=foods,
        start_date=start_date,
        end_date=end_date,
        employee_id=employee_id
    )
    MENU[menu_id['id']] = menu
    MENU[menu_id['id']] += 1


def show_menu():
    if len(MENU.values()) > 0:
        all_menu = [f"{key}, {value}" for key, value in MENU.items()]
        all_menu = ', '.join(all_menu)
        print(f'\n\n{all_menu}\n\n')
        menu_number = int(input("Enter menu number: "))
        menu = MENU.get(menu_number, 'This menu does`nt exist! ')
        if type(menu) != str:
            menu.info(all_foods=FOOD)


#################################################

def create_order(order_id: dict, receipt_id: dict, user: Employee):
    all_foods = FOOD
    user = get_current_user(session_user=user)
    foods = get_all_foods_to_order(all_foods=all_foods)
    total = get_foods_total_cost(foods=foods)
    employee_id = user.id
    cafe_id = user.cafe_id
    order = Order(
        id=order_id['id'],
        foods=foods,
        total=total,
        employee_id=employee_id,
        cafe_id=cafe_id
    )
    ORDER[order_id['id']] = order

    ordered_foods = ''

    for ordered_food in foods:
        food = FOOD[int(ordered_food[0])]
        quantity = int(ordered_food[1])
        ordered_foods += f"""Food: {food.name}
                             Price: {food.price}
                             Quantity: {quantity}
                             Subtotal price: {food.price * int(ordered_food[1])}
                             """
        cafe = CAFE[user.cafe_id]
        total_service_percent = total * cafe.service_percent
        print(f"""
              {cafe.name}
              
              Order  №{order_id}
              
              {ordered_foods}
              Service percent: {cafe.service_percent * 100} %
            
              Order total: {total} $
              Total service percent: {total_service_percent} $
              Total: {total + total_service_percent} $
                
             water: {user.full_name()}
             order time: {datetime.now().strftime('%H:%M %d-%m-%Y')}
                
              Address: {cafe.address}
              Phone number: {cafe.phone_number}
              Open at: {cafe.work_start_time}
              Close at: {cafe.work_end_time}
                
              Work days: {cafe.work_days}
        
        """)
        receipt = Receipt(
                id=receipt_id['id'],
                order_id=order_id['id']
            )
        RECEIPT[receipt_id['id']] = receipt
        order_id['id'] += 1
        receipt_id['id'] += 1

def get_all_foods_to_order(all_foods: dict):
    order_foods = []

    all_foods = [f"{key}: {value}" for key,value in all_foods.items()]
    all_foods = ', '.join(all_foods)
    while True:
        action = input("Enter 1 to add food\n"
                       "Enter 2 to commit order")
        if action == '1':
            print(f"\n\n{all_foods}\n\n")
            food = input("Enter food number: ")
            quantity = input("Enter quantity: ")
            order_foods.append([food, quantity])
        elif action == '2':
            if len(order_foods) > 0:
                print("Your order commited!")
                break
            print("You can`t commit order because no foods selected!")
        else:
            wrong_command()

    return order_foods


def get_foods_total_cost(foods: list):
    total = 0
    for food in foods:
        quantity = int(food[1])
        food = FOOD[int(food[0])]
        total += food.price * quantity
    return total

#################################################


#################################################
# Receipt
def create_receipt(receipt_id: dict, order_id: int):


    receipt = Receipt(
            id=receipt_id['id'],
            order_id=order_id
        )

    RECEIPT[receipt_id['id']] = receipt
    receipt_id['id'] += 1


def update_receipt_status():
    order_id = input("Enter order id: ")
    all_receipt = RECEIPT.values()
    for receipt in all_receipt:
        if receipt.order_id == order_id:
            status = input(f"Choose one of status below:\n {Receipt.STATUS}\n\n ")
            if status in Receipt.STATUS.keys():
                receipt.status = status
                return print("Status edited success!")
            return print("Please enter correct number!")
#################################################


# Others
def wrong_command():
    print("Please enter correct command!")
