from django.core.validators import RegexValidator


post_code_validator = RegexValidator("\d{2}\-\d{3}", "'Invalid post code'")
