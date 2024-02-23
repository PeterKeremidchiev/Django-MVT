def username_validator(value):
    is_valid = all(ch.isalnum() or ch == '_' for ch in value)

    if not is_valid:
        raise ValueError('Ensure this value contains only letters, numbers, and underscore.')