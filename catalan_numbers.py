"""This script prompts a user to enter a quantity of parentheses
   and calculate a number of correct parentheses containing N
   opening and N closing parentheses """


def get_catalan_value(number_pairs):
    """
    recursive function for calculating of numbers of Catalan
    :param number_pairs::= quantity of pairs
    :return::= Catalan's number
    """
    if number_pairs < 0:
        raise ValueError('Number of pairs can`t be negative')

    if number_pairs >= 2:
        return int(((2 * ((2 * number_pairs) - 1)) / (number_pairs + 1)) *
                   get_catalan_value(number_pairs - 1))
    return 1  # default value in case of n = 1


init_value = int(input('Enter, please, a number of quantity of parentheses > '))
# calculating of correct expressions for n parentheses
if type(init_value) == int:
    result = get_catalan_value(int(init_value))
    print('Quantity of correct expressions  is = ' + str(result))
else:
    print('Quantity of pairs should be a real numbers only')
