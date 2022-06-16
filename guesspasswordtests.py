import unittest
import datetime
import genetic
import guesspassword

class GuessPasswordTests(unittest.TestCase):   
    def test_HelloWorld(self):
        target = "Hello World!" 
        guess = guesspassword.guess_password(target)
        self.assertEqual(target,guess)
        
    def test_BruceLee(self):
        target = "BruceLee2021!" 
        guess = guesspassword.guess_password(target)
        self.assertEqual(target,guess)
        
    def test_For_I_am_fearfully_and_wonderfully_made(self):
        target = "For I am fearfully and wonderfully made."
        guess = guesspassword.guess_password(target)
        self.assertEqual(target,guess)
        
if __name__ == '__main__':     
     unittest.main()