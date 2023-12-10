import unittest

class TestPasswordValidator(unittest.TestCase):
    
    def test_valid_password(self):
        rules = []
        validator = PasswordValidator(rules)

        valid_password = "V4lid_pass0rd"
        self.assertTrue(validator.validate_password(valid_password))