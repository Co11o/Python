import random


def get_integer(prompt):
    """
    Get an integer from Standard Input (stdin).

    The function will continue looping and prompting
    the user, until a valid `int` is entered.
    :param prompt: The String that the user will see
        they're prompted to enter teh value
    :return: The integer that the user enters
    """
    while True:
        temp = input(prompt)
        if temp.isnumeric():
            return int(temp)
        else:
            print("{0} isn't a valid number".format(temp))


# help(get_integer)
# print("*"*80)
# print(get_integer.__doc__)
# print("*"*80)

highest = 1000
answer = random.randint(1, highest)
print(answer)  # TODO: Remove after testing

print("Please guess number between 1 and {}: ".format(highest))
print("Enter 0 to quit")
isCorrect = False
numAttempts = 1

while not isCorrect:
    guess = get_integer(": ")

    if guess != answer:
        if guess == 0:
            print("Goodbye!")
            break
        if guess < answer:
            print("Your guess is too low, try again: ")
        elif guess > answer:
            print("Your guess is too high, try again: ")
        numAttempts += 1
    else:
        if numAttempts == 1:
            print("First Try!")
        else:
            print("Correct, you took {0} attempt to guess the number {1} correctly".format(numAttempts, answer))
        isCorrect = True
