from sys import getsizeof
import sys

def main():
    #say_hello()
    #test_out_primitives()
    #test_conditionals()
    #test_loops()
    #a = get_integer()
    #b = get_integer()
    #result = add_two_integers(a, b)
    #print(f"{result:.50f}")
    #print(do_you_accept_cookies())
    #print("Hello\n" * 3, end="")
    #print(average_student_results())
    #print_all_command_line_args()
    exit_if_no_command_line_args()


def exit_if_no_command_line_args():
    if(len(sys.argv) != 2):
        print("Usage: python python_intro.py <name>")
        sys.exit(1)
    else:
        print(f"hello, {sys.argv[1]}")
        sys.exit(0)

# Part 1 of homework
#def print_triangle():
def average_student_results():
    nathan_results = {"IoT" : 90, "Mobile Integration" : 100, "Algorithms and Data Structures" 
              : 55, "Data Science" : 70, "UDP" : 99}
    return sum(nathan_results.values())/len(nathan_results)


def convert_to_uppercase(before):
    return before.upper()


def command_line_arguments():
    if len(argv) == 2:
        print(f"hello, {argv[1]}")
    else:
        print("hello, world")


def print_all_command_line_args():
    for arg in argv:
        print(arg)
    





# Get user input and return True of they enter y or yes, False if they enter n or no
def do_you_accept_cookies():
    while True:
        answer = input("Do you accept cookies? ")
        if answer.lower() in ["y", "yes"]:
            return True
        elif answer.lower() in ["n", "no"]:
            return False
        else:
            print("I don't understand. Please try again.")



def get_integer():
    while True:
        try:
            return int(input("Enter an integer: "))
        except ValueError:
            print("That was not an integer. Try again.")

#a is less than, greater than or equal to b
def compare_two_numbers(a, b):
    if a < b:
        print(f"{a} is less than {b}")
    elif a > b:
        print(f"{a} is greater than {b}")
    else:
        print(f"{a} is equal to {b}")



def say_hello():
    name = input("What is your name? ")
    print(f"Hello, {name}")


def test_out_primitives():
    a = 4000000000000000000
    print(getsizeof(a))


def test_conditionals():
    a = 1
    b = 2
    if a < b:
        print("a is less than b")
    elif a > b:
        print("a is greater than b")
    else:
        print("a is equal to b")


def test_loops():
    for i in range(0, 10, 2):
        print(i, end=" ")


def add_two_integers(a, b):
    return a + b


main() 