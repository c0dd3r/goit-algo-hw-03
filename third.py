import re

def normalize_phone(phone_number):
    phone_number = re.sub(r"[^0-9+]", "", phone_number)
    if not phone_number.startswith('+'):
        if phone_number.startswith('380'):
            phone_number = '+' + phone_number
        else:
            phone_number = '+38' + phone_number
    
    return phone_number
