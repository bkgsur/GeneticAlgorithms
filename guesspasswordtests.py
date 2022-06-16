import unittest
import datetime
import genetic
import guesspassword

class GuessPasswordTests(unittest.TestCase):   
    def test_HelloWorld(self):
        target = "Hello World!" 
        guess = guesspassword.guess_password(target)
        self.assertEqual(target,guess)
        print("-----------------------")
    def test_BruceLee(self):
        target = "BruceLee2021!" 
        guess = guesspassword.guess_password(target)
        self.assertEqual(target,guess)
        print("-----------------------")
if __name__ == '__main__':     
     unittest.main()