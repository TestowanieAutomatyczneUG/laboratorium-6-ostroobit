class User:
    letters = "abcdefghijklmnopqrstuvwxyz"
    numbers = "0123456789"

    def valid_password(self, password):
        letters = 0
        numbers = 0
        schars = 0
        for char in password:
            if char in self.letters:
                letters += 1
            elif char in self.numbers:
                numbers += 1
            else:
                schars += 1
        if letters < 8:
            return False
