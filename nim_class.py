# CMPUT 396 Assignment 5 
# Nim class 

class Nim:

    def __init__(self, list_of_stones):
        self.game = list_of_stones 
        self.num_of_piles = len(list_of_stones)

    def print_game(self):
        print(' '.join(map(str,self.game)))

    def update(self, num_of_stones, pile):
        self.game[pile - 1] = self.game[pile - 1] - num_of_stones
        self.print_game()

    def check_end_game(self):
    	for item in self.game:
    		if item != 0:
    			return False 
    	return True 

    def return_state(self):
        return self.game
