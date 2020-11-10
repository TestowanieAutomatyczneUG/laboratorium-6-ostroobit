class User:
    def valid_password(self, password):
        if len(password) == 1:
            return False
