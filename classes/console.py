class Console:
    '''
    DON'T USE NOW
    '''
    __clear_before_output = False
    __row_separator = ''
    __column_separator = ''
    def __init__(self, clear_before_output, row_separator = '\n\n', column_separator = '    |    '):
        self.set_clear_before_output(clear_before_output)
        self.set_row_separator(row_separator)
        self.set_column_separator(column_separator)

    def set_clear_before_output(self, clear_before_output):
        self.__clear_before_output = clear_before_output

    def set_row_separator(self, row_separator):
        self.__row_separator = row_separator

    def set_column_separator(self, column_separator):
        self.__column_separator = column_separator    

    def output(self, structure_of_output):
        self.__get_ready_to_the_output_strings(self, structure_of_output)
    
    def __get_ready_to_the_output_strings(self, structure_of_output):
        structure_of_input = {}
        for item in structure_of_output:
            if type(item) is str:
                if structure_of_output['item']['name'] == 'message':
                    self.__get_ready_to_the_message()
                else:
                    raise ValueError('Ошибка передаваемого')
    def __get_ready_to_the_message(self):
        pass