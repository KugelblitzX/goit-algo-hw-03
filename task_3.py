import re

def normalize_phone(phone_number):
    regex = r"[\d\+]+"
    phone_number = "".join(re.findall(regex, phone_number))
    if len(phone_number) == 10:
        phone_number = "+38" + phone_number
    elif len(phone_number) == 12:
        phone_number = "+" + phone_number
    return phone_number

raw_numbers = [
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
    "432 11 222 22 22"
]
for phone in raw_numbers:
    print(normalize_phone(phone))