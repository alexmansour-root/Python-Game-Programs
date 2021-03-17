"""This program defines the Die class. We then define and  implement the __init__, __str__, roll, and 
get_value methods. We play a game of two rounds of dice rolls and we print the values of each round. """

import sys
import random

__author__ 	= "Alex Mansour"
__license__ = "GPL"
__version__ = "1.0.1"
__date__ 	= "June 13, 2020"


class Die:
	""" We define the Die class"""
	
	def __init__(self, side):
		"""We instantiate the attribute of the Die class
		Args:
			side (int): Integer value of the side of each die
		"""
						# Side attribute is instantiated
		self.side = side

	def __str__(self):
		"""Gets the string representation of a Die object.
		Returns:
			str: String representation of a Die object.
		"""
						# string adaptation of the attribute
						
		return str(self.side)
		
	def roll(self):
		"""Sets the integer value of a Die object."""
		
			# We generate random numbers using the randint function.
			
		self.side=random.randint(1,6)
		
	def get_value(self):
		"""Gets the random integer value from a dice roll.
		Returns:
			int: Internal Integer value of a Die object.
		"""
		
			# Here, we retrieve the value of the two objects after the dice rolls a random number.
	
		return self.side



def main(argv):



	"""Main function of the script.
	Args:
		argv (list): Contains command-line arguments passed to the script.
	Returns:
        int: Error code after execution (0 if OK).
	"""
	error_code = 0
	
	# We instantiate the two objects, die1 and die 2, and we set the default value at 1.
	
	die1=Die(1)
	die2=Die(1)
	
	# Here, we print the intitial value of both objects, defaulted to 1.
	
	print(str(die1.get_value()))
	print(str(die2.get_value()))
	
	# We roll the dice and we generate a random number for both objects.
	
	die1.roll()
	die2.roll()
	
	# We get the integer value of the first dice roll.
	
	first_roll =(die1.get_value(), die2.get_value())
	
	# We print the result of the first dice roll, for both objects.
	
	print(str(first_roll[0]))
	print(str(first_roll[1]))
	
	# We roll the dice a second time and we genarate a random number for both objects.
	
	die1.roll()
	die2.roll()
	
	# We get the integer value of the second dice roll.
	
	second_roll = (die1.get_value(), die2.get_value())
	
	# We print the result of the second dice roll, for both objects.
	
	print(str(second_roll[0]))
	print(str(second_roll[1]))
	
	# We print the combined value of two rounds of dice rolls.
	
	print("The combined value of both dice for first roll = ",sum(first_roll))
	print("The combined value of both dice for second roll = ",sum(second_roll))
	
	return error_code

if __name__ == '__main__':
	error_code = main(sys.argv[1:])
	print('[+] Terminated with code: ' + str(error_code))
	sys.exit(error_code)
