from django.core.exceptions import ValidationError

FORBIDDEN_NICKNAMES = [
    'me',
    'admin',
    'moderator',
    'support',
    'helpdesk',
    'root',
    'guest',
    'anonymous',
    'bot',
    'system',
    'banned',
    'deleted'
]


def validate_username(value):
    """Username должен быть строкой и не должен быть в FORBIDDEN_NICKNAMES."""
    if not isinstance(value, str):
        raise ValidationError(
            'username должен иметь тип str'
        )
    if value.lower() in FORBIDDEN_NICKNAMES:
        raise ValidationError(
            f'username не может быть "{value}"'
        )
    return value
