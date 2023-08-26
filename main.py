import random
import unittest
class GuessGame:
    

       #generates a random number
    def __init__(self):
        self.number = self.random()
        
       #random number will be in range of 1000 to 9999
    def random(self):
        return random.randint(1000, 9999)
    
    def check(self, x):
        # this line checks whether the input is of 4 digit or not
        target_value = []
        for i in str(self.number):
            number = int(i)
            target_value.append(number)

      # Transform the digits of x into a list referred to as guess_value.
        guess_value = []
        for i in str(x):
            number = int(i)
            guess_value.append(number)

        # corresponding check the digits of target_value and guess_value
        circles = 0
        for t_digit, g_digit in zip(target_value, guess_value):
            if t_digit == g_digit:
                circles += 1
        
        # set of commondigitvalues between the target_value and guess_value
        # & set of intersection of two sets
        commondigitvalues = [digit for digit in target_value if digit in guess_value]
        
        # count of guessed numbers which was correct but has been placed in a wrong position
        count = len(commondigitvalues) - circles
      
        
        output = f"{circles} (circles) {count} (x)"
        return output

#additional feature
#it will print the random number after 15 wrong attempts
    def printnumber(self):
        print(f"----------------------The number is {self.number}----------------------------------")
        return self.number

if __name__ == '__main__':
    print("-------------------------------------------Welcome to the guess the number game!--------------------------------------------")
    
    while True:
        game = GuessGame() 
        count = 0

        while True:
            #to find the number, enter your guess, or press e to exit the game
            user = input("--------- Write your guess (to exit press e): ")
            if user.lower() == 'e':
                break
               
               #the lenght of digits must be of 4, if number is less or more thqan 4, display the below message 
            if not user.isdigit() or len(user) != 4:
                print("!!!!!!!!!!!!!!!!!!!!Wrong Input! Please Enter the correct 4 digit number...!!!!!!!!!!!!!!!!")
                continue

            x = int(user)
            prediction = game.check(x)  
            print(prediction)
            count += 1
            
            #after 15 wrong attempts, it will print the random number
            if count >= 15:
                game.printnumber()


           #after successfully guessing 4 circles, you will recive the below message 
            if prediction == "4 (circles) 0 (x)": 
                print(f"----------------------Woah...! You guessed the correct number in {count} attempts.----------------------------------")
                break
            
            
       #Condition whether user wants to play again or not 
        playagain = input("You wanna play again? press y to YES, n to NO: ")
        if playagain.lower() != 'y':
            break
