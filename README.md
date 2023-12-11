[![Lint code](https://github.com/juzor/password-validator/actions/workflows/lint.yml/badge.svg)](https://github.com/juzor/password-validator/actions/workflows/lint.yml) [![Run tests](https://github.com/juzor/password-validator/actions/workflows/test.yml/badge.svg)](https://github.com/juzor/password-validator/actions/workflows/test.yml)

# Password Validation Library

This Python library provides a flexible and extensible framework for validating passwords based on various rules. It includes predefined validation rules for length, uppercase letters, lowercase letters, numbers, special characters, and more.

## Usage
```python
from password_validator import PasswordValidator
from password_validator import (
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
print(validator.validate_password("ValidPassword123_")) # => True

print(validator.validate_password("weakpwd")) # => False

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
