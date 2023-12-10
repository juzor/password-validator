from abc import ABC, abstractmethod


class ValidationRule(ABC):
    """
    Base class for password validation rules.

    Methods:
        validate(password: str) -> bool: Validates a password based on a specific rule.
    """

    @abstractmethod
    def validate(self, password):
        """
        Abstract method to validate a password based on a specific rule.

        Args:
            password (str): Password to be validated.

        Returns:
            bool: True if the password passes the validation, otherwise False.
        """
        pass  # pylint: disable=unnecessary-pass


class LengthRule(ValidationRule):
    """
    Validation rule for password length.

    Methods:
        validate(self, password: str) -> bool:
            Validates that the password meets the length requirement.
    """

    def __init__(self, length: int) -> None:
        self.length = length

    def validate(self, password):
        """
        Validates that the password meets the length requirement.

        Args:
            password (str): The password to be validated.

        Returns:
            bool: True if the password meets the length requirement, False otherwise.
        """
        return len(password) >= self.length


class UppercaseRule(ValidationRule):
    """
    Validation rule for at least one capital letter (i.e. uppercase).

    Methods:
        validate(self, password: str) -> bool:
            Validates that the password contains at least one capital letter (i.e. uppercase).
    """

    def validate(self, password):
        """
        Validates that the password contains at least one capital letter (i.e. uppercase).

        Args:
            password (str): The password to be validated.

        Returns:
            bool: True if the password contains at least one capital letter, False otherwise.
        """
        return any(char.isupper() for char in password)


class LowercaseRule(ValidationRule):
    """
    Validation rule for at least one small letter (i.e. lowercase).

    Methods:
        validate(self, password: str) -> bool:
            Validates that the password contains at least one small letter (i.e. lowercase).
    """

    def validate(self, password):
        """
        Validates that the password contains at least one small letter (i.e. lowercase).

        Args:
            password (str): The password to be validated.

        Returns:
            bool: True if the password contains at least one small letter, False otherwise.
        """
        return any(char.islower() for char in password)


class NumberRule(ValidationRule):
    """
    Validation rule for at least one number.

    Methods:
        validate(self, password: str) -> bool:
            Validates that the password contains at least one number.
    """

    def validate(self, password):
        """
        Validates that the password contains at least one number.

        Args:
            password (str): The password to be validated.

        Returns:
            bool: True if the password contains at least one number, False otherwise.
        """
        return any(char.isdigit() for char in password)


class SpecialCharacterRule(ValidationRule):
    """
    Validation rule for the presence of at least one symbol (including underscore).

    Methods:
        validate(self, password: str) -> bool
            Validates that the password contains at least one symbol.
    """

    def validate(self, password):
        """
        Validates that the password contains at least one symbol.

        Args:
            password (str): The password to be validated.

        Returns:
            bool: True if the password contains at least one symbol, False otherwise.
        """
        symbols = set("!@#$%^&*()-_+=<>?/,.:;[]{}|~")
        return any(char in symbols for char in password)


class NoSpaceRule(ValidationRule):
    """
    Validation rule that checks if a password contains spaces.
    If the password contains spaces, it is not valid.
    """

    def validate(self, password):
        """
        Validates whether the provided password contains spaces.

        Args:
            password (str): The password to be validated.

        Returns:
            bool: Whether the password contains spaces or not.
        """
        return " " not in password
