# Question 1:
# Write a function to print "hello_USERNAME!" USERNAME is the input of the
#    of the function. The first line of the code has been defined as below. 
#    def hello_ name(user_name):

def hello_name(user_name):
    user_name = input("Enter Username: ")
    print(f"hello_{user_name.upper()}")

hello_name("")

# Question 2:
# Write a Python function, first_odds that prints the odd numbers from 1-100
#    and returns nothing 
#    def first_odds():

def first_odds():
    num = 1
    while num <= 100:
        if num % 2 == 1:
            print(num)
        num += 1

first_odds()

# Question 3:
# Please write a Python function, max_num_in_list to return the max number of
#    a given list. The first line of the code has been defined as below. 
#    def max_num_in_list(a_list):

def max_num_in_list(a_list):
    num = [a_list]
    print(max(a_list))

max_num_in_list([])

# Question 4:
# Write a function to return if the given year is a leap year. A leap year is
#    divisible by 4, but not divisible by 100, unless it is also divisible by 
#    400. The return should be boolean Type(true/false). 
#    def is_leap_year(a_year):

def is_leap_year(a_year):
    num = a_year
    if num % 400 == 0:
        print(True)
    elif num % 4 == 0 and num % 100 != 0:
        print(True)
    else:
        print(False)


is_leap_year()


# Question 5:
# Write a function to check to see if all numbers in the list are consecutive
#    numbers. For example, [2,3,4,5,6,7] are consecutive numbers, but [1,2,4,5]
#    are not consecutive numbers. The return should be boolean Type.
#    def is_consecutive(a_list):

def is_consecutive(a_list):
    sorted_list = sorted(a_list)
    range_list = list(range(min(a_list), max(a_list) + 1))
    if sorted_list == range_list:
        print(True)
    else:
        print(False)

is_consecutive([])
