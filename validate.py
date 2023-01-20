from datetime import datetime
from os.path import isfile


#################################################################

# Café


def validate_name(name: str) -> bool:
    if name.isalpha() and 50 >= len(name) >= 2:
        return True
    return False


def validate_address(address: str) -> bool:
    if 200 >= len(address) >= 5:
        return True
    return False


def validate_phone_number(phone_number: str) -> bool:
    if len(phone_number) == 10 and phone_number.startswith('0'):
        return True
    return False


def validate_work_time(work_time: str) -> bool:
    # '22:00'
    # '08:00'
    sep_time = work_time.split(':')
    # ['08', '00']
    if len(sep_time) == 2 and (len(sep_time[0]) == 2 and len(sep_time[1]) == 2) and \
        (sep_time[0].isdigit(), sep_time[1].isdigit()) and (0 <= int(sep_time[0]) < 24) and \
        (0 <= int(sep_time[1]) < 60):
        return True
    return False


def validate_days(work_days: str) -> bool:
    # 1,2,3,4,5,6,7
     #[1,2,3]

    EXAMPLE = (1, 2, 3, 4, 5, 6, 7)
    days = work_days.split(',')
    all_exist = all([day in EXAMPLE for day in days])
    return all_exist
    # all_exist = []
    # for day in days:
    #     all_exist.append(day in EXAMPLE)
    # return all(all_exist)


def validate_percent(percent: float) -> bool:
    if 1 >= percent >= 0:
        return True
    return False


def validate_status(status: str, EXAMPLE: dict) -> bool:
    keys = EXAMPLE.keys()
    return status in keys


def validate_update_time(time, create_time):
    if type(time) == datetime and create_time <= time:
        return True
    return False

#################################################################

# Employee


def validate_first_name(first_name: str) -> bool:
    if first_name.isalpha() and 20 >= len(first_name) >= 2:
        return True
    return False


def validate_last_name(last_name: str) -> bool:
    if last_name.isalpha() and 25 >= len(last_name) >= 2:
        return True
    return False


def validate_date_of_birth(date_of_birth: str) -> bool:
    sep_date = date_of_birth.split('.')
    if (len(sep_date[0]) == 2 and len(sep_date[1]) == 2 and len(sep_date[2]) == 4) and\
       (sep_date[0].isdigit() and sep_date[1].isdigit and sep_date[2].isdigit()) and\
       (1 <= int(sep_date[0]) <= 31) and (1 <= int(sep_date[1]) <= 12) and (1983 <= int(sep_date[2]) <= 2600):
        return True
    return False


def validate_password(password: str) -> bool:
    if 16 >= len(password) >= 8:
        return True
    return False


def validate_passport_id(passport_id: str) -> bool:
    if passport_id.isdigit() and len(passport_id) == 7:
        return True
    return False


def validate_work_date(work_date: str) -> bool:
    sep_date = work_date.split('.')
    if (len(sep_date[0]) == 2 and len(sep_date[1]) == 2 and len(sep_date[2]) == 4) and\
       (sep_date[0].isdigit() and sep_date[1].isdigit and sep_date[2].isdigit()) and\
       (1 <= int(sep_date[0]) <= 31) and (1 <= int(sep_date[1]) <= 12) and (2020 <= int(sep_date[2]) <= 3000):
        return True
    return False


def match_password(password_one, password_two):
    return password_one == password_two

#################################################################

# FOOD


def validate_image(image: str) -> bool:
    if isfile(image):
        return True
    return False


def validate_description(descriotion: str) -> bool:
    if len(descriotion) == 1000:
        return True
    return False


def validate_price(price: str) -> bool:
    if price.isdigit() and type(price) == float:
        return True
    return False


def validate_weight(weight: str) -> bool:
    if weight.isdigit() and 50 < int(weight) == 700:
        return True
    return False

#################################################################

# Menu


def validate_food(foods: str) -> bool:
    EXAMPLE = (1, 2, 3, 4, 5, 6, 7)


