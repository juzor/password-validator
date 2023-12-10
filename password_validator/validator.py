class PasswordValidator:

    def validate_password(self, password):
        return (
            len(password) >= 8
        )
            