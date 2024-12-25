import re

def normalize_phone(phone_number: str):
    pattern = r'[\D]'
    replacement = ''
    result = re.sub(pattern, replacement, phone_number)
    code = '+38'
    if not result.startswith(code):
        result = result.replace("+", "")
        result = code + result
    return str(result)


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
print("Normalized phone numbers for SMS sending:", sanitized_numbers)
