"""
######################
### REPRESENTATION ###
	1. Natural Language
Generate a list of 1000 random numbers.
	a. Print prime numbers and their position inside the list
	b. Print odd numbers from even positions inside list
	c. Print even numbers from odd positions inside list
	d. Print sum of prime numbers that have control number between 3 and 7

"""
import math
def is_prime(n):
    ##################################################################
    ### steps area ###
    """
    response to a.:
	Step 1: Loop through all the elements in the given range.
	Step 2: Check for each number if it has any factor between 1 and itself.
	Step 3: If yes, then the number is not prime, and it will move to the next number.
	Step 4: If no, it is the prime number, and the program will print it and check for the next number.
###########################################################################################################
    response to b. + c.:
    Step_1: Iterate over each element in the list created above, using enumerate() to get both the index
        and the value. For the odd numbers from even positions, we check if the index is even and if the number is odd.
        If both conditions are met, we print the number.
    Step_2:Similarly, for the even numbers from odd positions, we check if the index is odd and if the number is even.
        If both conditions are met, we print the number.
###########################################################################################################
	response to d.:
	Step_1: It define a helper function that calculates and control a given number.
	Step_2: It converts the number to a string, iterates over its digits, converts them back to integers,
and sums them up.
    Step_3: It iterate over each number in the list and check if the controled number is between 3 and 7
and if it's prime.If both conditions are met, it adds the prime number to the sum_of_primes_numbers variable.
    Step4: Print the original list and the sum of prime numbers with a control number between 3 and 7.

    """
    ##################################################################

    ##################################################################
    ### code area ###
    if n < 2:
        return False
    for i in range(2, math.isqrt(n) + 1):
        if n % i == 0:
            return False
    return True
    ### returns TRUE or FALSE ###


##################################################################


##################################################################


def main():
    print("|-----------------------------------------------|")
    print("|                 Main Function                 |")
    print("|-----------------------------------------------|")

    ##########################################################

    print("|-----------------------------------------------|")
    print("|                 Prime Numbers                 |")
    print("|-----------------------------------------------|")
    my_list_x = list(range(1, 1001))
    print(my_list_x)
    #########################################################
    print("|-----------------------------------------------|")
    print("|                Prime Nr. Position             |")
    print("|-----------------------------------------------|")
    for index, number in enumerate(my_list_x):
        if is_prime(number):
            print(f"Prime number: {number}, Position: {index}")
    ############################################################
    print("|-----------------------------------------------|")
    print("|          Odd numbers from even positions      |")
    print("|-----------------------------------------------|")
    for index, number in enumerate(my_list_x):
        if index % 2 == 0 and number % 2 != 0:
            print(number)
    ###########################################################
    print("|-----------------------------------------------|")
    print("|        Even numbers from odd positions        |")
    print("|-----------------------------------------------|")
    for index, number in enumerate(my_list_x):
        if index % 2 != 0 and number % 2 == 0:
            print(number)
    #############################################################################
    print("|-----------------------------------------------------------------|")
    print("|  Sum of prime numbers that have control number between 3 and 7  |")
    print("|-----------------------------------------------------------------|")

    def controller_nr(n):
        return sum(int(digit) for digit in str(n))

    sum_of_primes_numbers = 0
    for number in my_list_x:
        control_number = controller_nr(number)
        if 3 <= control_number <= 7 and is_prime(number):
            sum_of_primes_numbers += number

    print("Sum of prime numbers with control number between 3 and 7:", sum_of_primes_numbers)
    #############################################################################


if __name__ == '__main__':
    main()
