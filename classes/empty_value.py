class EmptyValue:
    '''
    The EmptyValue class is designed to slove indicate empty cells of game field:
    1. contain:
        1.1. symbol of the empty cells of game field
    2. the actions:
        2.1. starting fill of class
        2.2. returning symbol of the empty cell(s) and is empty value as True

    Fields:
        __symbol_of_gamer - str (string) - this is empty symbol of cells of game field
    '''
    __symbol_of_gamer = '-'
    def __init__(self, symbol_of_gamer = '-'):
        self.__symbol_of_gamer = symbol_of_gamer
    @property
    def symbol_of_gamer(self):
        return self.__symbol_of_gamer
    @property
    def is_empty_value(self):
        return True