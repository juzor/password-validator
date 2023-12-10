# Password Validation Library

This Python library provides a flexible and extensible framework for validating passwords based on various rules. It includes predefined validation rules for length, uppercase letters, lowercase letters, numbers, special characters, and more.

## Usage
```python
from password_validation_library import (
    PasswordValidator, LengthRule, UppercaseRule, 
    LowercaseRule, NumberRule, SpecialCharacterRule, NoSpaceRule
)

# Define validation rules
length_rule = LengthRule(length=8)
uppercase_rule = UppercaseRule()
lowercase_rule = LowercaseRule()
number_rule = NumberRule()
special_char_rule = SpecialCharacterRule()
no_space_rule = NoSpaceRule()

# Create a PasswordValidator instance with the desired rules
validator = PasswordValidator(
    rules=[
        length_rule, uppercase_rule, lowercase_rule, 
        number_rule, special_char_rule, no_space_rule
    ]
)

# Validate a password
password_to_check = "SecurePassword123!"
is_valid = validator.validate_password(password_to_check)

if is_valid:
    print("Password is valid!")
else:
    print("Password does not meet the validation criteria.")

```

## Validation Rules

### LengthRule
Ensures that the password meets a specified length requirement.

### UppercaseRule
Validates that the password contains at least one uppercase letter.

### LowercaseRule
Validates that the password contains at least one lowercase letter.

### NumberRule
Validates that the password contains at least one number.

### SpecialCharacterRule
Validates that the password contains at least one special character (including underscore).

### NoSpaceRule
Ensures that the password does not contain any spaces.
