from email_validator import validate_email, EmailNotValidError

try:
    valid = validate_email("invalid-email@")
except EmailNotValidError as e:
    print(f"E-mail not valid: {str(e)}")