"""
 *****************************************************************************
   FILE: REPL.PY

   AUTHOR: Amin Babar

   ASSIGNMENT: Homework 1: Arithmetic REPL

   DATE: 08/30/18

   DESCRIPTION: This REPL program handles the multiplication, division,
   subtraction and addition operations. The input should be in a certain format
    or else the program will print out an error statement. The program prints
    out an error if the input is not spaced correctly; all the numbers and
    operators should have exactly a single space in between. Only the use of
    +-/*01234567890 is allowed. All other symbols will result in an error
    message. The / symbol acts like python's // symbol. Multiplication and
    division are prioritized over addition and subtraction. All operations
    are applied from left to right. Input of an empty string will quit the
    program!

 *****************************************************************************
"""


def read(input_text):
    """
    This function goes over the input_text, separates the numbers and operators
    and puts them in different lists. It also checks for errors related to
    format and division by 0 in the input_text.
    """

    # number_list and operators_list are declared
    number_list, operators_list = [], []

    # i is declared. Keeps track of the position in the while loop.
    i = 0

    # If a negative number is input, negative_number turns true
    negative_numbers = False

    # The total length of the numbers in the input
    total_length_numbers = 0

    # If an error is found in the input, this turns true.
    error = False

    # Goes over character by character on the input_text.
    while i < len(input_text):

        # If there is any error in the input text, error will turn True, and
        # the while loop will break
        if error:
            break

        # If the input text is a number, it will be appended to the number_list
        if input_text[i] in "1234567890":

            # Handles negative numbers. If a negative number is input, the
            # negative operator is removed from the operators_list
            if i > 0 and input_text[i - 1] == "-":
                operators_list.pop()
                negative_numbers = True

            # The variable number is declared. This variable is assigned the
            # value of different numbers found in the input_text.
            number = ""

            # reads through the input text for numbers, and assigns the
            # variable number the number found in the input text
            while i < len(input_text) and input_text[i] in "1234567890":
                number = number + input_text[i]
                i += 1
                total_length_numbers += 1

            # It converts the number from the input_string into a integer,
            # and then converts it back to a string to compare the length of
            # the two numbers. If there is a difference between the lengths and
            # if the number is not 0, it will turn the error message true. This
            # makes sure that numbers starting in 0, unless the number is 0,
            # are treated as errors.
            if len(number) != len(str(int(number))) and int(number) != 0:
                error = True

            # If negative_number is true, the number found in the input text is
            # multiplied by -1, and it's appended to the number list.
            # negative_number is turned back to the false state.
            if negative_numbers:
                number_list.append(int(number) * -1)
                negative_numbers = False
                total_length_numbers += 1

                # Keeps track of the order of the operators and numbers. If two
                # consecutive numbers are input or two consecutive operators
                # are input, the error will turn true.
                if len(number_list) != (len(operators_list) + 1):
                    error = True

            # if number is not negative, it's appended to the number list, here
            else:
                number_list.append(int(number))

                # Same test for the order of operators and numbers is performed
                # again for non-negative numbers.
                if len(number_list) != (len(operators_list) + 1):
                    error = True

            # If an input number is 0, and a divide symbol precedes it,
            # error is turned true. Division by 0 will return an error.
            if operators_list != [] and number_list[len(number_list) - 1] == 0:
                if operators_list[len(operators_list) - 1] == "/":
                    error = True

        # If the input_text consists of an operator -, *, / or +, it's appended
        # to the operator list.
        elif i < len(input_text) and input_text[i] in "-+/*":
            operators_list.append(input_text[i])
            i += 1

        # If a space is found, i is increased by 1.
        else:
            i += 1

    # Keeps track of the number of spaces in the input text by comparing the
    # length of the input text, with the length of the numbers in the
    # number_list, and 3 times the length of the operators in the operator_list
    # which accounts for the length of the operator, and the space before and
    # after the operator. If equality doesn't hold, the error is turned true.
    # Also keeps track of unwanted chars in the input_text.
    if len(input_text) != (3 * len(operators_list)) + total_length_numbers:
        error = True

    # returns the number_list the operators_list and the error boolean.
    return number_list, operators_list, error


def calculate(number_list, operators_list):
    """
    This function carries out all the operations in the operation list on the
    numbers in the number_list. * and / operations are performed first, while
    + and - operations are performed after. All the operations are performed
    left to right.
    """

    # i keeps track of the position within the operators_list
    i = 0

    # performs the * and / operations left to right
    while i != len(operators_list):

        # performs operations on the numbers in the number_list based on the
        # * and / operators found in the operators_list. The first operator
        # in the operator_list performs the operation on the first two
        # elements in the number_list and so on.
        if operators_list[i] == "*":
            number_list[i] = number_list[i] * number_list[i + 1]
            number_list.pop(i + 1), operators_list.pop(i)
        elif operators_list[i] == "/":
            number_list[i] = number_list[i] // number_list[i + 1]
            # syntax??????
            number_list.pop(i + 1), operators_list.pop(i)
        else:
            i += 1

    # i keeps track of the position within the operators_list
    i = 0

    # Performs the + and - operations from left to right
    while i != len(operators_list):

        # performs operations on the numbers in the number_list based on the
        # + and - operators found in the operators_list The first operator
        # in the operator_list performs the operation on the first two
        # elements in the number_list and so on.
        if operators_list[i] == "+":
            number_list[i] = number_list[i] + number_list[i + 1]
            number_list.pop(i + 1), operators_list.pop(i)
        else:
            number_list[i] = number_list[i] - number_list[i + 1]
            number_list.pop(i + 1), operators_list.pop(i)

    # returns the first and only element of the number_list after all the
    # operations are performed.
    return number_list[0]


def main():
    """
    This function control the flow of the program, and offloads the details to
    the other functions.
    """

    # number_list, operator_list and error are declared
    number_list, operators_list, error = [], [], False

    # Runs an infinite loop. The infinite loop only breaks if there is an
    # empty string input.
    while True:

        # Asks for an input from the user
        input_text = input("> ")

        # The infinite loop breaks once an empty string is input. It prints
        # Goodbye!
        if input_text == "":
            print("Goodbye!")
            break

        # The read function sets the value for number_list, operator_list
        # and error.
        number_list, operators_list, error = read(input_text)

        # If error is true, ERROR prints out.
        if error:
            print("ERROR")

        # If no error is found in the input, the calculate function is
        # called. The calculate function then performs the operations in the
        # operators_list on the numbers in the number_list.
        else:
            print(calculate(number_list, operators_list))


if __name__ == "__main__":
    main()
