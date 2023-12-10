from abc import ABC, abstractmethod

class ValidationRule(ABC):
    @abstractmethod
    def validate(self, password):
        pass

class LengthRule(ValidationRule):
    def validate(self, password):
        return len(password) > 8

class PasswordValidator:

    def __init__(self, rules):
        self.rules = rules

    def validate_password(self, password):
        for rule in self.rules:
            if not rule.validate(password):
                return False
        
        return True
            