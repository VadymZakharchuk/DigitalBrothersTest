"""This script prompts a user to enter a quantity of parentheses
   and calculate a number of correct parentheses containing N
   opening and N closing parentheses """


def get_catalan_value(number_pairs):
    """
    recursive function for calculating of numbers of Catalan
    :param number_pairs::= quantity of pairs
    :return::= Catalan's number
    """
    if type(number_pairs) is not int:
        raise TypeError('Number of pairs should be real number only')

    if number_pairs < 0:
        raise ValueError('Number of pairs can`t be negative')

    if number_pairs >= 2:
        return int(((2 * ((2 * number_pairs) - 1)) / (number_pairs + 1)) *
                   get_catalan_value(number_pairs - 1))
    return 1  # default value in case of n = 1


init_value = input('Enter, please, a number of quantity of parentheses > ')
# calculating of correct expressions for n parentheses
result = get_catalan_value(int(init_value))
print('Quantity of correct expressions  is = ' + str(result))
