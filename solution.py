#Question 1: Write a function that determines whether a number is even or odd.
def even_or_odd(n: int) -> str:
    
    if not isinstance(n, int) or isinstance(n, bool): #checking input is integer or not
        raise TypeError("Enter only integer value. for example: 1,2,3 etc")
        
    if n % 2 == 0: #checking input is even or odd try to get remainder of input
        return "Even" #even if remainder is 0
    else:
        return "Odd" #odd if remainder is not 0
    
#Question 2: Write a function that calculates the total sum of a list of numbers.
def add_all(numbers: list) -> int:
    
    total = 0 #accumulator variable for sum
    
    for n in numbers: #looping through list of numbers
        total =total + n #adding each number to the accumulator variable
        
    return total #returning the sum of the numbers in the list


if __name__ == "__main__": #main function to run above functions
    print("--- Testing Question 1: Even or Odd ---")
    print(f"--> {even_or_odd(4)}")  # Expected: Even result
    print(f"--> {even_or_odd(9)}")  # Expected: Odd result
    print(f"--> {even_or_odd(0)}")  # Expected: Even (while 0 is even)

    print("\n--- Testing Question 2: Sum of a List ---")
    print(f"--> {add_all([1, 2, 3, 4, 5])}")  # Expected: sum is 15
    print(f"--> {add_all([10, -2, 11])}")          # Expected: sum is 13
    print(f"--> {add_all([])}")                            # Expected: sum is 0 (as there are no numbers in the list)