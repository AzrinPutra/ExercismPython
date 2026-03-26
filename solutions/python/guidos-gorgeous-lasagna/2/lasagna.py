"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language:
https://en.wikipedia.org/wiki/Guido_van_Rossum

This is a module docstring, used to describe the functionality
of a module and its functions and/or classes.
"""


#TODO: define your EXPECTED_BAKE_TIME (required) and PREPARATION_TIME (optional) constants below.
EXPECTED_BAKE_TIME = 40
PREPARATION_TIME = 2

#TODO: Remove 'pass' and complete the 'bake_time_remaining()' function below.
def bake_time_remaining(current_bake_time):
    """Calculate the bake time remaining.

    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """
    bake_time_remaining = EXPECTED_BAKE_TIME - current_bake_time
    return bake_time_remaining


#TODO: Define the 'preparation_time_in_minutes()' function below.
# To avoid the use of magic numbers (see: https://en.wikipedia.org/wiki/Magic_number_(programming)), you should define a PREPARATION_TIME constant.
# You can do that on the line below the 'EXPECTED_BAKE_TIME' constant.
# This will make it easier to do calculations, and make changes to your code.

def preparation_time_in_minutes(number_of_layers):
    """Calculate total preparation time.

    :param number_of_layers: int - number of layers of the lasagna
    :return: int - total preparation time(in minutes) derived from 'PREPARATION TIME' constant

    Function that takes the number of layers of the lasagna as an argument and returns the total preparation time based on the 'PREPARATION_TIME' of each layer 
    """
    total_preparation_time = PREPARATION_TIME * number_of_layers
    return total_preparation_time

#TODO: define the 'elapsed_time_in_minutes()' function below.

def elapsed_time_in_minutes(number_of_layers, current_bake_time):
    """Calculate the elapsed cooking time

    :param number_of_layers: int - number of layers in the lasagna
    :param current_bake_time: int - elapsed cooking time
    :return: int - total time elapsed(in minutes) preparing and cooking

    Function takes two integers and representing the number of lasagna layers and the time already spent baking and calculates the total elapsed minutes spent cooking the lasagna
    """
    total_preparation_time = preparation_time_in_minutes(number_of_layers)
    total_time_in_kitchen = total_preparation_time + current_bake_time

    return total_time_in_kitchen

# TODO: Remember to go back and add docstrings to all your functions
#  (you can copy and then alter the one from bake_time_remaining.)
