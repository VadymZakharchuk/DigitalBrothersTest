"""This script prompts a user to enter a quantity of parentheses
   and calculate a number of correct parentheses containing N
   opening and N closing parentheses """


def get_catalan_value(number_pairs):
    """
    recursive function for calculating of numbers of Catalan
    :param number_pairs::= quantity of pairs
    :return::= Catalan's number
    """

    if number_pairs >= 2:
        return int(((2 * ((2 * number_pairs) - 1)) / (number_pairs + 1)) *
                   get_catalan_value(number_pairs - 1))
    return 1  # default value in case of n = 1


init_value = input('Enter, please, a number of quantity of parentheses > ')
# checking - is entered value is a number
if init_value.isdigit():
    if int(init_value) > 0:
        # calculating of correct expressions for n parentheses
        result = get_catalan_value(int(init_value))
        print('Quantity of correct expressions  is > ' + str(result))
    else:
        # default value in case of n = 0
        print('Quantity of correct expressions  is > 1')
else:
    print('Please, enter a valid value')
