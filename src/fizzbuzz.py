import unittest

class FizzBuzz:
    def game(self, num):
        """
        >>> fb = FizzBuzz()
        
        >>> fb.game(5)
        'Buzz'
        >>> fb.game(10)
        'Buzz'
        
        >>> fb.game(3)
        'Fizz'
        >>> fb.game(12)
        'Fizz'

        >>> fb.game(15)
        'FizzBuzz'
        >>> fb.game(30)
        'FizzBuzz'

        >>> fb.game("haha")
        Traceback (most recent call last):
            File "/usr/lib/python3.8/doctest.py", line 1336, in __run
                exec(compile(example.source, filename, "single",
            File "<doctest __main__.FizzBuzz.game[7]>", line 1, in <module>
                fb.game("haha")
            File "fizzbuzz.py", line 43, in game
                raise Exception("Error in FizzBuzz")
        Exception: Error in FizzBuzz
        
        >>> fb.game(False)
        Traceback (most recent call last):
            File "/usr/lib/python3.8/doctest.py", line 1336, in __run
                exec(compile(example.source, filename, "single",
            File "<doctest __main__.FizzBuzz.game[8]>", line 1, in <module>
                fb.game(False)
            File "fizzbuzz.py", line 54, in game
                raise Exception("Error in FizzBuzz")
        Exception: Error in FizzBuzz

        """
        if type(num) == int or type(num) == float:
            if num % 5 == 0 and num % 3 == 0:
                return "FizzBuzz"
            elif num % 5 == 0:
                return "Buzz"
            elif num % 3 == 0:
                return "Fizz"
            elif num % 5 != 0 and num % 3 != 0:
                return str(num)
        else:
            raise Exception("Error in FizzBuzz")
        
        
if __name__ == "__main__":
    
    import doctest
    doctest.testmod()

