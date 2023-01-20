from datetime import datetime, date
from validate import (validate_name, validate_address, validate_phone_number, validate_work_time,
                      validate_days, validate_percent, validate_status, validate_update_time,
                      validate_first_name, validate_last_name, validate_password, validate_date_of_birth,
                      validate_passport_id, validate_work_date, validate_description, validate_price, validate_weight,
                      validate_food, validate_image
                      )


class Base:

    def __init__(self, id: int):
        self.__id = id
        self.__created_date = datetime.now()
        self.__updated_date = datetime.now()

    @property
    def id(self):
        return self.__id

    @property
    def create_date(self):
        return self.__created_date

    @property
    def update_date(self):
        return self.__updated_date

    @update_date.setter
    def update_date(self, update_date: datetime):
        is_valid = validate_update_time(
            time=update_date,
            create_time=self.__created_date
        )
        if is_valid:
            self.__updated_date = update_date
            print("Update date success!")
        else:
            print("Update date is incorrect!")


class Cafe(Base):
    STATUS_TYPES = {
        '1': 'Work',
        '2': 'Unwork',
        '3': 'Repair',
        '99': 'Cleaning day'
    }

    # Register attribute

    def __init__(self, id: int, name: str,
                 address: str, phone_number: str):
        super().__init__(id)
        self.__name = name
        self.__address = address
        self.__phone_number = phone_number
        self.__work_start_time = '10:00'
        self.__work_end_time = '18:00'
        self.__work_days = ('1', '2', '3', '4', '5')
        self.__service_percent = 0.05
        self.__status = '1'
        self.__is_active = True

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        is_valid = validate_name(name=name)
        if is_valid:
            self.__name = name
            print("Name edited success!")
        else:
            print("Name is incorrect!")

    @property
    def address(self):
        return self.__address

    @address.setter
    def address(self, address):
        is_valid = validate_address(address=address)
        if is_valid:
            self.__address = address
            print("Address edited success!")
        else:
            print("Address is incorrect")

    @property
    def phone_number(self):
        return self.__phone_number

    @phone_number.setter
    def phone_number(self, phone_number):
        is_valid = validate_phone_number(phone_number=phone_number)
        if is_valid:
            self.__phone_number = phone_number
            print("Phone number edited success!")
        else:
            print("Phone number is incorrect!")

    @property
    def work_start_time(self):
        return self.__work_start_time

    @work_start_time.setter
    def work_start_time(self, work_start_time):
        is_valid = work_start_time(work_start_time=work_start_time)
        if is_valid:
            self.__work_start_time = work_start_time
            print("Work start time edited success!")
        else:
            print("Work start time entered is incorrect!Example 'HH:mm' '08:00'!!!")

    @property
    def work_end_time(self):
        return self.__work_end_time

    @work_end_time.setter
    def work_end_time(self, work_end_time: str):
        is_valid = validate_work_time(work_time=work_end_time)
        if is_valid:
            self.__work_end_time = work_end_time
            print('Work end time edited success!')
        else:
            print('Work end time is inccorect! Example "HH:mm" "08:00"!!!')

    @property
    def work_days(self):
        return self.__work_days

    @work_days.setter
    def work_days(self, work_days: str):
        is_valid = validate_days(work_days=work_days)
        if is_valid:
            self.__work_days = work_days
            print("Work days edited success!")
        else:
            print("Work days is incorrect! Example: '1,2,3,4,5,6,7'! ")

    @property
    def service_percent(self):
        return self.__service_percent

    @service_percent.setter
    def service_percent(self, service_percent: float):
        is_valid = validate_percent(percent=service_percent)
        if is_valid:
            self.__service_percent = service_percent
            print('Service percent edited success!')
        else:
            print('Service percent is inccorect! format 2% -> 0.02')

    @property
    def status(self):
        status = self.STATUS_TYPES.get(self.__status, 'No status')
        return status

    @status.setter
    def status(self, status):
        is_valid = validate_status(
            status=status,
            EXAMPLE=self.STATUS_TYPES
        )
        if is_valid:
            self.__status = status
            print('Status edited success!')
        else:
            print(f'Status is incorrect! {self.STATUS_TYPES}')

    @property
    def is_active(self):
        return self.__is_active


class Employee(Base):
    STATUS = {
        '1': 'Work',
        '2': 'Unwork',
        '3': 'Sick',
        '4': 'Decree',
        '5': 'Dismissed',
        '6': 'Holiday'
    }

    # Register attribute
    def __init__(self, id: int, cafe_id: int, first_name: str, last_name: str,
                 phone_number: str, password: str, date_of_birth: date,
                 passport_id: int, work_start_date: date,
                 work_end_date: date, status=list(STATUS.keys())[0], is_active=True) -> None:
        super().__init__(id)
        self.__cafe_id = cafe_id
        self.__first_name = first_name
        self.__last_name = last_name
        self.__phone_number = phone_number
        self.__password = password
        self.__date_of_birth = date_of_birth
        self.__passport_id = passport_id
        self.__status = status
        self.__work_start_date = work_start_date
        self.__work_end_date = work_end_date
        self.__is_active = is_active

    def full_name(self):
        return self.__first_name, self.__last_name

    @property
    def first_name(self):
        return self.__first_name

    @first_name.setter
    def first_name(self, first_name):
        is_valid = validate_first_name(first_name=first_name)
        if is_valid:
            self.__first_name = first_name
            print("First Name edited success!")
        else:
            print("First Name is incorrect!")

    @property
    def last_name(self):
        return self.__last_name

    @last_name.setter
    def last_name(self, last_name):
        is_valid = validate_last_name(last_name=last_name)
        if is_valid:
            self.__last_name = last_name
            print("Last name edited success!")
        else:
            print("Last name is incorrect!")

    @property
    def date_of_birth(self):
        return self.__date_of_birth

    @date_of_birth.setter
    def date_of_birth(self, date_of_birth):
        is_valid = validate_date_of_birth(date_of_birth=date_of_birth)
        if is_valid:
            self.date_of_birth = date_of_birth
            print("Date of birth edited success!")
        else:
            print("Date of birth is incorrect! Example '01.01.2021'")

    @property
    def phone_number(self):
        return self.__phone_number

    @phone_number.setter
    def phone_number(self, phone_number):
        is_valid = validate_phone_number(phone_number=phone_number)
        if is_valid:
            self.__phone_number = phone_number
            print("Phone number edited success!")
        else:
            print("Phone number is incorrect!")

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, password):
        is_valid = validate_password(password=password)
        if is_valid:
            self.__password = password
            print("Password edited success!")
        else:
            print("Password is incorrect!")

    @property
    def passport_id(self):
        return self.__password

    @passport_id.setter
    def passport_id(self, passport_id):
        is_valid = validate_passport_id(passport_id=passport_id)
        if is_valid:
            self.__passport_id = passport_id
            print("Passport ID edited success!")
        else:
            print("Passport ID is incorrect!")

    @property
    def status(self):
        status = self.STATUS.get(self.__status, 'No status')
        return status

    @status.setter
    def status(self, status):
        is_valid = validate_status(
            status=status,
            EXAMPLE=self.STATUS
        )
        if is_valid:
            self.__status = status
            print('Status edited success!')
        else:
            print(f'Status is incorrect! {self.STATUS}')

    @property
    def work_start_date(self):
        return self.__work_start_date

    @work_start_date.setter
    def work_start_date(self, work_start_date):
        is_valid = validate_work_date(work_date=work_start_date)
        if is_valid:
            self.__work_start_date = work_start_date
            print("Work start time edited success!")
        else:
            print("Work start time entered is incorrect!Example '31.12.2023'!!!")

    @property
    def work_end_date(self):
        return self.__work_end_date

    @work_end_date.setter
    def work_end_date(self, work_end_date):
        is_valid = validate_work_date(work_date=work_end_date)
        if is_valid:
            self.__work_end_date = work_end_date
            print("Work end date edited success!")
        else:
            print("Work end date entered is incorrectExample '31.12.2023'!!!!")


class Food(Base):
    CATEGORY = {
        '1': 'First',
        '2': 'Second',
        '3': 'Candy',
        '4': 'Hot drink',
        '5': 'Drink',
        '6': 'Breakfast',
        '7': 'Salad',
        '8': 'Snacks'

    }

    # Register attribute

    def __init__(self, id: int, name: str, image: str,
                 description: str, category: str,
                 employee_id: int, weight=0, price=0) -> None:
        super().__init__(id)
        self.__name = name
        self.__image = image
        self.__description = description
        self.__category = category
        self.__employee_id = employee_id
        self.__weight = weight
        self.__price = price

    def __str__(self):
        return str(self.__name)

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        is_valid = validate_name(name=name)
        if is_valid:
            self.__name = name
            print("Food name edited success!")
        else:
            print("Food name is incorrect!")

    @property
    def image(self):
        return self.__image

    @image.setter
    def image(self, image):
        is_valid = validate_image(image=image)
        if is_valid:
            self.__image = image
            print("Image edited success!")
        else:
            print("Image is incorrect")

    @property
    def description(self):
        return self.__description

    @description.setter
    def description(self, description):
        is_valid = validate_description(descriotion=description)
        if is_valid:
            self.__description = description
            print("Description edited success!")
        else:
            print("Description is incorrect")

    @property
    def category(self):
        return self.__category

    @category.setter
    def category(self, category):
        is_valid = validate_status(
            status=category,
            EXAMPLE=self.CATEGORY
        )
        if is_valid:
            self.__category = category
            print("Category edited success!")
        else:
            print("Category is incorrect")

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price):
        is_valid = validate_price(price=price)
        if is_valid:
            self.__price = price
            print("Price edited success!")
        else:
            print("Price is incorrect! Example '50.0'")

    @property
    def weight(self):
        return self.__weight

    @weight.setter
    def weight(self, weight):
        is_valid = validate_weight(weight=weight)
        if is_valid:
            self.__weight = weight
            print("Weight edited success!")
        else:
            print("Weight is incorrect")

    @property
    def employee_id(self):
        return self.__employee_id


class Menu(Base):

    # Register attribute

    def __init__(self, id: int, name: str, foods: list,
                 start_date: datetime, end_date: datetime,
                 employee_id: int, is_active=True):
        super().__init__(id)
        self.__name = name
        self.__foods = foods
        self.__start_date = start_date
        self.__end_date = end_date
        self.__employee_id = employee_id
        self.__is_active = is_active

    def info(self, all_foods):
        foods_menu_description = ''

        for food in self.__foods:
            food = all_foods[int(food)]
            foods_menu_description += (f"""
            
                Foods name - {food.__name}
                Price - {food.__price}
                Weight - {food.__weight}
                Type - {Food.CATEGORY[food.category]} 
                
                Img: {food.image}
                
                Description: {food.description}
                
                ------------------------------
            """)
            print(f"Menu name:"
                  f"{self.__name}\n\n{foods_menu_description}")

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        is_valid = validate_name(name=name)
        if is_valid:
            self.__name = name
            print("Name edited success!")
        else:
            print("Name is incorrect!")

    @property
    def foods(self):
        return self.__foods

    @foods.setter
    def foods(self, foods: str):
        is_valid = validate_food(foods=foods)
        if is_valid:
            self.__foods = foods
            print("Foods edited success!")
        else:
            print("Foods is incorrect!")

    @property
    def start_date(self):
        return self.__start_date

    @start_date.setter
    def start_date(self, start_date: str):
        is_valid = validate_work_date(work_date=start_date)
        if is_valid:
            self.__start_date = start_date
            print("Start date edited success!")
        else:
            print("Start date is incorrect! Example 01.01.2023")

    @property
    def end_date(self):
        return self.__end_date

    @end_date.setter
    def end_date(self, end_date: str):
        is_valid = validate_work_date(work_date=end_date)
        if is_valid:
            self.__end_date = end_date
            print("End date edited success!Example 01.01.2023")
        else:
            print("End date is incorrect!")

    @property
    def employee_id(self):
        return self.__employee_id

    @property
    def is_active(self):
        return self.__is_active


class Order(Base):

    # Register attribute

    def __init__(self, id: int, employee_id: int,
                 foods: list, total: float, cafe_id: int) -> None:
        super().__init__(id)
        self.__employee_id = employee_id
        self.__foods = foods
        self.__total = total
        self.__cafe_id = cafe_id

    @property
    def employee_id(self):
        return self.__employee_id

    @property
    def foods(self):
        return self.__foods

    @foods.setter
    def foods(self, foods: str):
        is_valid = validate_food(foods=foods)
        if is_valid:
            self.__foods = foods
            print("Foods edited success!")
        else:
            print("Foods is incorrect!")

    @property
    def total(self):
        return self.__total

    @property
    def cafe_id(self):
        return self.__cafe_id


class Receipt(Base):

    STATUS = {
        '1': 'Payed',
        '2': 'Unpaid',
        '3': 'Rejection',
        '4': 'Free'
    }

    # Register attribute

    def __init__(self, id: int, order_id: int, status=list(STATUS.keys())[0]):
        super().__init__(id)
        self.__order_id = order_id
        self.__status = status

    @property
    def order_id(self):
        return self.__order_id

    @property
    def status(self):
        return self.__status

    @status.setter
    def status(self, status):
        is_valid = validate_status(
            status=status,
            EXAMPLE=self.STATUS_TYPES
        )
        if is_valid:
            self.__status = status
            print("Status edited success!")

        else:
            print("Status is incorrect!")
