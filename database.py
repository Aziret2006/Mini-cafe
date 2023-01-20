from moduls import Cafe, Employee
CAFE = {
    0: Cafe(
        id=0,
        name='Faisa',
        address='Bishkek',
        phone_number='0500060402')
        }
EMPLOYEE = {
    0: Employee(
        id=0,
        cafe_id=0,
        first_name='Arthur',
        last_name='Akimov',
        phone_number='0500060402',
        date_of_birth='01.01.2000',
        passport_id='3311161',
        work_start_date='01.01.2000',
        work_end_date='01.01.2040',
        password='12345'
    )

}
FOOD = {}
MENU = {}
ORDER = {}
RECEIPT = {}

SESSION_USER = {'user': 0}
