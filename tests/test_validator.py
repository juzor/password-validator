import unittest
from password_validator.validator import PasswordValidator
from password_validator.validator import (
    LengthRule,
)

class TestPasswordValidator(unittest.TestCase):
    
    def test_valid_password(self):
        validator = PasswordValidator()

        valid_password = "V4lid_pass0rd"
        self.assertTrue(validator.validate_password(valid_password))

    def test_invalid_password_length(self):
        rules = [LengthRule()]
        validator = PasswordValidator(rules)

        invalid_password = "Asc11"
        self.assertFalse(validator.validate_password(invalid_password))

    def test_invalid_password_no_uppercase(self):
        validator = PasswordValidator()

        invalid_password = "n0_uppercase"
        self.assertFalse(validator.validate_password(invalid_password))

    def test_invalid_password_no_lowercase(self):
        validator = PasswordValidator()

        invalid_password = "N0_L0WERCASE"
        self.assertFalse(validator.validate_password(invalid_password))

    def test_invalid_password_no_number(self):
        validator = PasswordValidator()

        invalid_password = "No_Number"
        self.assertFalse(validator.validate_password(invalid_password))

    def test_invalid_password_no_underscore(self):
        validator = PasswordValidator()

        invalid_password = "N0underSc0re"
        self.assertFalse(validator.validate_password(invalid_password))