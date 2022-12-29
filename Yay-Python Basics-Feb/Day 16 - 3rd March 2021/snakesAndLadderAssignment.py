###############################################################################
#                       Project 1 - Snake & Ladders                           #
###############################################################################
# * --------------------------------------------------------------------------*
# * AUTHOR: Rahul Bordoloi <rahul.bordoloi@highradius.com>                    *
# * Github: https://github.com/rahulbordoloi                                  *
# * Question: https://bit.ly/yay_project_1                                    *
# * --------------------------------------------------------------------------*
# * DATE CREATED: 3 March, 2021                                               *
# * ************************************************************************"""

# Importing Libraries
import random

# Snake Class
class Snake:

    """
    Class to Implement Snakes and Ladders Game.
    """

    # Default Constructor
    def __init__(self):

        print("###### Welcome to Snakes & Ladders Game ######")
        self.name = input("Enter the Name of Player 1 : ")
        self.comp = input("Enter the Name of Player 2 : ")
        print("###### Let us Start ######")
        self._game = [0, 0]    # Steps of the Players [Initial]

        # Goto Dictionaries [Given the Question]
        self.__pos_of_snakes = {17 : 7, 54 : 34, 62 : 19, 98 : 79}
        self.__pos_of_ladders = {3 : 38, 24 : 33,  42 : 93, 72 : 84}
    
    # Display Players' Name
    def displayName(self):

        print("Player 1's Name : {}, Player 2's Name : {}".format(self.name, self.comp))

    # Display Winner's Name
    def __displayWinner(self, number):

        if number == "1":   
            winner = self.name
        else:   
            winner = self.comp
        print("Player {} won the Game!".format(number))
        print("Congratulations {} !!".format(winner))
        print("###### Game Successfully Finished ######")
        exit(0)

    # Check for Any Snakes or Ladders in the current position
    def __checkSnakeLadder(self, position):

        if position in self.__pos_of_snakes.keys():    
            position = self.__pos_of_snakes.get(position)
        elif position in self.__pos_of_ladders.keys():     
            position = self.__pos_of_ladders.get(position)

        return position

    # Check for 'quit'
    def __quitGame(self, number):

        if number == "1":   
            self.__displayWinner("2")
        else:   
            self.__displayWinner("1")
        exit(0)
    
    # Check for Overflow Position
    def __checkMoreThanHundred(self, position, x):

        if (position + x) > 100:   
            pass                                        # Check for > 100
        else:   
            position += x

        return position
    
    # Check for the Range of Input in Manual Mode
    def __checkManualMode(self, inp, loop = 0):

        x = int(inp)
        if x not in range(2, 20):
            print("Invalid Input! The Number you Entered isn't within the range of between 1 and 20")
            try:
                x = int(input("Please Enter a Number within the given Range : "))
                self.__checkManualMode(x)
            except: 
                x = int(input("Please Enter a Valid Number within the given Range : "))
                self.__checkManualMode(x)

        return x

    # Check for the Move Input if it's Valid or Illegal
    def __checkMoveInput(self, number):

        inp = input("Player {} : ".format(number))
        if inp == "roll":                                    # Auto [Automatic]
            x = random.randint(1, 6)
        elif inp == "quit":     
            self.__quitGame(number)
        elif inp.isnumeric():                                # Manual [Betwen 1-20]
            x = self.__checkManualMode(inp)
        else:   
            print("Illegal Input, Please Input a Valid Input!")
            x = self.__checkMoveInput(number)
        print("You got a ", x)

        return x
    
    # Player Position Function
    def __playerPosition(self, number):
        
        pos = 0
        pos = self._game[int(number) - 1]
        x = self.__checkMoveInput(number)            # Check for Valid Input
        pos = self.__checkMoreThanHundred(pos, x)    # Check for the Validity of the Position
        pos = self.__checkSnakeLadder(pos)           # Check for Snakes and Ladder
        print(" Your Final Position is ", pos)
        if pos == 100:                               # Check for Winner
            self.__displayWinner(number)
        self._game[int(number) - 1] = pos            # Lastly assigning the step into the list

    # Snake Game Function
    def snakeGame(self):

        while True:
            self.__playerPosition('1')
            self.__playerPosition('2')

# Main Method
if __name__ == "__main__":

    # Using Exception Handling Techniques to Handle any unfavourable outcomes
    snake = Snake()
    snake.displayName()
    snake.snakeGame()                            # Game Method
    del snake                                    # Delete the Object


###############################################################################
#                                 END                                         #
###############################################################################