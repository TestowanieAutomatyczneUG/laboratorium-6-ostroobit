class User:
    letters = "abcdefghijklmnopqrstuvwxyz"
    numbers = "0123456789"

    def valid_password(self, password):
        """
        >>> u = User()

        >>> u.valid_password("abc")
        False

        >>> u.valid_password("Abc")
        False

        >>> u.valid_password("Abc1")
        False

        >>> u.valid_password("Abc1*")
        False

        >>> u.valid_password("Abc*")
        False

        >>> u.valid_password("Abcdebfiewbfi1")
        False

        >>> u.valid_password("hewbuhbewhbf1*")
        False

        >>> u.valid_password("njenvjewovoew*")
        False

        >>> u.valid_password("Abcvewjvewvwevev(1")
        True

        """
        letters = 0
        numbers = 0
        schars = 0
        upper = 0
        for char in password:
            if char in self.letters:
                letters += 1
            elif char in self.numbers:
                numbers += 1
            elif char in self.letters.upper():
                upper += 1
                letters += 1
            else:
                schars += 1
        
        if letters < 8:
            return False
        if numbers < 1:
            return False
        if schars < 1:
            return False
        if upper < 1:
            return False
        return True

if __name__ == "__main__":
    import doctest
    doctest.testmod()