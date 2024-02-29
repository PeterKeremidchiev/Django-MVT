def fruit_name_validator(value):
    is_alpha = all([ch.isalpha() for ch in value])
    if not is_alpha:
        raise ValueError('Fruit name should contain only letters!')

