"""
Complete the following functions based on the description in their docstring.

When functions are underspecified, implement them so that the tests pass.
"""

def square(n):
    """
    Return the square of input `n`

    :param n: The number to square
    :return: The square of `n`
    """
    return n*n

assert(square(0) == 0)
assert(square(1) == 1)
assert(square(2) == 4)
assert(square(25) == 625)


def letter_grade(percentage):
    """
    Return a letter grade from a supplied percentage
    
    :param percentage: Grade a percentage
    :return: Letter grade as a string (e.g. "B+")
    
    This function uses the following grading scale:

    Letter Grade   Percentage
    ------------   ----------
    A              93-100%
    A-             90-93%
    B+             87-90%
    B              83-87%
    B-             80-83%
    C+             77-80%
    C              73-77%
    C-             70-73%
    D+             67-70%
    D              63-67%
    D-             60-63%
    F              0-60%
    ------------   --------
    """
    
    if 93 <= percentage <= 100:
        return "A"
    elif 90 <= percentage < 93:
        return "A-"
    elif 87 <= percentage < 90:
        return "B+"
    elif 83 <= percentage < 87:
        return "B"
    elif 80 <= percentage < 83:
        return "B-"
    elif 77 <= percentage < 80:
        return "C+"
    elif 73 <= percentage < 77:
        return "C"
    elif 70 <= percentage < 73:
        return "C-"
    elif 67 <= percentage < 70:
        return "D+"
    elif 63 <= percentage < 67:
        return "D"
    elif 60 <= percentage < 63:
        return "D-"
    elif 0 <= percentage < 60:
        return "F"

assert(letter_grade(100) == "A")
assert(letter_grade(90) == "A-")
assert(letter_grade(87) == "B+")
assert(letter_grade(83) == "B")
assert(letter_grade(80) == "B-")
assert(letter_grade(77) == "C+")
assert(letter_grade(73) == "C")
assert(letter_grade(70) == "C-")
assert(letter_grade(67) == "D+")
assert(letter_grade(63) == "D")
assert(letter_grade(60) == "D-")
assert(letter_grade(59) == "F")
assert(letter_grade(84.5) == "B")
assert(letter_grade(79.9) == "C+")


def get_age(birth_year, birth_month, birth_day,
            current_year, current_month, current_day):
    """ Returns an person's age given their birthdate

    :param birth_year: Birth year as an integer
    :param birth_month: Birth month as an integer
    :param birth_day: Birth day as an integer
    :param current_year: Current year as an integer
    :param current_month: Current month as an integer
    :param current_day: Current day as an integer
    """

    age = current_year - birth_year

    if (current_month < birth_month): 
       age = age - 1
    
    elif (current_day < birth_day):
        age = age - 1
    
    return age
 

assert(get_age(1906,1,1,2006,1,1) == 100)
assert(get_age(2030,1,1,2030,1,1) == 0)
assert(get_age(2030,1,1,2031,1,1) == 1)
assert(get_age(2030,6,1,2031,1,1) == 0)
assert(get_age(2030,6,6,2036,6,6) == 6)
assert(get_age(2030,6,6,2036,6,5) == 5)
assert(get_age(2030,6,6,2036,5,6) == 5)
assert(get_age(2030,4,6,2036,5,6) == 6)


# TODO: Create a custom function below of your choosing.
#
# The function should do something meaningful and use branches **and** arithmetic.
#
# Include meaningful tests using `assert`.




def tempature(tempature):
    
    if tempature >= 150:
        return "Never mind you are probably dead"
    elif tempature <= 50:
        return "You should probably wear pants"
    elif tempature >= 50:
        return "You will be just fine with shorts"

    
assert(tempature(20) == "You should probably wear pants")
assert(tempature(55) == "You will be just fine with shorts")
assert(tempature(200) == "Never mind you are probably dead")


