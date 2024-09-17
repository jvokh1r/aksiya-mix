from rest_framework.exceptions import ValidationError


def validate_phone_number(phone_number: str) -> None:
    if not (len(phone_number) == 13 and phone_number.startswith('+998') and phone_number[1:].isdigit()):
        raise ValidationError('Phone number is not valid!')