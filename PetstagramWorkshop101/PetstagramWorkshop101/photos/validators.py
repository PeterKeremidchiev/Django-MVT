from django.core.exceptions import ValidationError


def validate_file_size(image_object):
    if image_object.size > 524880:
        raise ValidationError('File too large. Size should not exceed 5 MB.')