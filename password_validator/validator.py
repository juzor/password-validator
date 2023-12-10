from abc import ABC, abstractmethod

class ValidationRule(ABC):
    @abstractmethod
    def validate(self, password):
        pass

class LengthRule(ValidationRule):
    def validate(self, password):
        return len(password) > 8
    
class UppercaseRule(ValidationRule):
    def validate(self, password):
        return any(char.isupper() for char in password)
    
class LowercaseRule(ValidationRule):
    def validate(self, password):
        return any(char.islower() for char in password)
    
class NumberRule(ValidationRule):
    def validate(self, password):
        return any(char.isdigit() for char in password)
    
class UnderscoreRule(ValidationRule):
    def validate(self, password):
        return '_' in password
    
class NoSpaceRule(ValidationRule):
    def validate(self, password):
        return ' ' not in password

class PasswordValidator:

    def __init__(self, rules):
        self.rules = rules

    def validate_password(self, password):
        for rule in self.rules:
            if not rule.validate(password):
                return False
        
        return True
            