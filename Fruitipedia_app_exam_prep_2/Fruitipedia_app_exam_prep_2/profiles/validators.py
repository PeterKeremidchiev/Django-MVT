

def name_validator(value):
    if not value[0].isalpha():
        raise ValueError('Your name must start with a letter!')

