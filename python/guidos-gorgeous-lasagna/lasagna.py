"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language:
https://en.wikipedia.org/wiki/Guido_van_Rossum

This is a module docstring, used to describe the functionality
of a module and its functions and/or classes.
"""


EXPECTED_BAKE_TIME = 40
PREPARATION_TIME = 40

def bake_time_remaining(time):
    """Calculate the bake time remaining.

    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """
    return EXPECTED_BAKE_TIME - time



def preparation_time_in_minutes(number_of_layers):
    """Calculate the preparation time in minutes

    :param number_of_layers: int - Number of layers needed to prepare.
    :return: int - Time (in minutes) it takes to prepare the layers .

    function that takes the number_of_layers you want to add to the lasagna as an argument and returns how many       minutes you would spend making them. Assume each layer takes 2 minutes to prepare.
    """
    return number_of_layers * 2


def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """Calculate the elapsed time in minutes.

    :param number_of_layers: int - Number of layers needed to prepare.
    :param elapsed_bake_time: int - elapsed bake time (in minutes).
    :return: int - total minutes you have been in the kitchen cooking
    
    Function that return the total minutes you have been in the kitchen cooking — your preparation time layering      + the time the lasagna has spent baking in the oven.
    """
    preparation_time = preparation_time_in_minutes(number_of_layers)
    return preparation_time + elapsed_bake_time
