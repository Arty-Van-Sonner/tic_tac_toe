from languages import Languages
from console import Console
from gamers import Gamers
from games import Games

class Interface:
    '''
    DON'T USE NOW
    '''
    __working_environment = None
    __language = None
    __game = None
    __current_status = None
    __default_language = 'ru'
    def __init__(self, working_environment) -> None:
        self.__working_environment = working_environment
        self.__language = Languages(self.__default_language)
    
    def output_start_menu(self):
        structure_of_output = []  
        sub_structure_of_output = []
        sub_structure_of_output.append(self.__add_structure_of_item(
            'start_menu',
            f'{self.__language.get_string(string_name)} ({self.__language.get_string("choosing_game")})'
        ))   
        structure_of_input = {
            'tic_tac_toe': {
                'structure_of_input': {
                    'commands': ['-ttt', '-t', 'tic_tac_toe'],
                },
            },
        }
        for string_name in structure_of_input:
            structure_of_input[string_name].update({
                'name': string_name,
                'value': f'{i}) {self.__language.get_string(string_name)}',
            })
            sub_structure_of_output.append(self.__add_structure_of_item(**structure_of_input[string_name]))
            i += 1

        sub_structure_of_output.append(self.__add_structure_of_item(
            'select_option',
            f'{self.__language.get_string(string_name)}: ',
            _input = True,
        ))
        structure_of_output.append(self.__add_structure_of_item(
            'start_menu',
            sub_structure_of_output,
            'message',
        ))
        structure_of_input = self.__working_environment.output(structure_of_output)

        
    def __add_structure_of_item(self, name, value, _type = 'string', _input = False, structure_of_input = {}):
        sub_structure_of_output = {
            'name': name,
            'type': _type,
            'value': value,
            'input': _input,
            'structure_of_input': structure_of_input,
        }
        return sub_structure_of_output