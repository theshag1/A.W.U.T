from rest_framework.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


def Passport_validate(value):
    if not value.startswith(('AD',)):
        raise ValidationError(_('Passport must be start "AD"'))

