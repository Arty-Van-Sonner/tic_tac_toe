class Languages:
    '''
    DON'T USE NOW
    '''
    __short_name = ''
    __name = ''
    __list_access_languages = {
        'ru': {
            'full_name': 'russien',
        }, 
        'en': {
            'full_name': 'english',
        }
    }
    __languages_base = {
        'start_menu': {
            'ru': 'Начальное меню',
            'en': 'Start menu',
        },
        'choosing_game': {
            'ru': 'Выбор игры',
            'en': 'Choosing game',
        },
        'tic_tac_toe': {
            'ru': 'Крестики-нолики',
            'en': 'Tic tac toe'
        },
        'select_option': {
            'ru': 'Выберите опцию',
            'en': 'Select an option' 
        }
    }
    __language_base = {}
    
    def __init__(self, lang) -> None:
        self.__name = self.get_full_name_lang(lang)
        self.__short_name = lang   
        for lang_item in self.__languages_base:
            self.__language_base.update({lang_item: self.__languages_base[lang_item][lang]}) 
    def get_full_name_lang(self, lang) -> str:
        lang_data = self.__list_access_languages.get(lang)
        if lang_data is None:
            raise ValueError('Error setting the interface language (Ошибка установки языка интерфейса)!!!')
        return lang_data.full_name

    def get_string(self, string_name):
        item = self.__languages_base.get(string_name)
        if item is None:
            raise ValueError('Error The language element is missing (Ошибка элемент языка отсутствует)!!!')
        return item

    def __str__(self):
        return f'class: <Languages>; current_language: "{self.__name}"; current_language_short: "{self.__short_name}"'
   
    def __doc__(self):
        return '''This class contains ready-made strings in different languages with keyword access'''
    