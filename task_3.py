import re

def normalize_phone(phone_number):
    f_numb = re.sub(r"[^\d+]", "", phone_number)
    
    if not f_numb.startswith("+"):
        if not f_numb.startswith("380"):
            f_numb = "+38" + f_numb
        else:
            f_numb = "+" + f_numb
            
    return f_numb


raw_numbers = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]

sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
print("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers)