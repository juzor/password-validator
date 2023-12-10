class PasswordValidator:
    """
    A class for validating passwords based on a set of validation rules.

    Attributes:
        rules (list): A list of validation rules to be applied to passwords.

    Methods:
        __init__(self, rules: list)
            Initializes the PasswordValidator with a list of validation rules.

        validate_password(self, password: str) -> bool
            Validates the given password against the defined validation rules.
    """

    def __init__(self, rules):
        """
        Initialize the PasswordValidator with a list of validation rules.

        Args:
            rules (list): A list of ValidationRule instances.
        """
        self.rules = rules

    def validate_password(self, password):
        """
        Validate the given password against the defined validation rules.

        Args:
            password (str): The password to be validated.

        Returns:
            bool: True if the password is valid, False otherwise.
        """
        for rule in self.rules:
            if not rule.validate(password):
                return False

        return True
