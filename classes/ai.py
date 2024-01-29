from random import randint
import pandas as pd
# from tic_tac_toe import TicTacToe

class AI:
    '''
    The AI class is Artificial intelligence. It is designed to slove the tasks of counting the moves of computer:
    1. contain:
        1.1. difficulty level
        1.2. the сurrent game
        1.3. empty value. It contains object that means empty cell (s) of game field
        1.4. list or dict of win combinations
    2. the actions:
        2.1. starting fill of class
        2.2. calculation of the move taking into account the level of difficulty 

    Fields:
        __difficulty_level - int (integer) - difficulty level
        __сurrent_game - Games, TicTacToe (class) - the current game for which moves are calculated based on the difficulty level
        __empty_value - EmptyValue (class) - it contains object that means empty cell (s) of game field
        __win_combinations - dict (dictionary) - it contains list or dick, or another storage of winning combinations
    '''
    __difficulty_level = 0
    __сurrent_game = None
    __empty_value = None
    __win_combinations = None
    def __init__(self, сurrent_game, empty_value, win_combinations, difficulty_level = 0) -> None:
        self.__difficulty_level = difficulty_level
        self.__сurrent_game = сurrent_game
        self.__empty_value = empty_value
        self.__win_combinations = win_combinations

    def get_ai_move(self):
        from tic_tac_toe import TicTacToe
        if type(self.__сurrent_game) == TicTacToe:
            return self.get_tic_tac_toe_move() 
        else:
            raise ValueError('')

    def get_tic_tac_toe_move(self):
        game_data = self.__сurrent_game.get_data_for_ai()
        list_of_options = self.get_ready_list_of_options_of_tic_tac_toe(game_data['game_field'])
        size_of_list_of_options = len(list_of_options)
        list_index = randint(0, size_of_list_of_options - 1) if size_of_list_of_options > 1 else 0
        return list_of_options[list_index]

    def get_ready_list_of_options_of_tic_tac_toe(self, game_field):       
        dict_in_df = {
                'num_row': [],
                'num_column': [],
                'cost': [],
        }  
        i = 0
        j = 0
        for item in game_field:
            j = 0
            for sub_item in item:
                if sub_item.is_empty_value:
                    dict_in_df['num_row'].append(i)
                    dict_in_df['num_column'].append(j)
                    dict_in_df['cost'].append(self.calculate_cost_of_move(i, j, game_field)) 
                j += 1
            i += 1   
        list_of_options = []
        if self.__difficulty_level == 2:  
            for i in range(len(dict_in_df['num_row'])):
                list_of_options.append((dict_in_df['num_row'][i], dict_in_df['num_column'][i])) 
            return list_of_options
        df_of_options = pd.DataFrame(dict_in_df)
        df_of_options.sort_values(['cost'], axis=0, ascending=False, inplace=True)
        if self.__difficulty_level == 0:
            list_of_options.append((df_of_options['num_row'].iloc[0], df_of_options['num_column'].iloc[0]))
        elif self.__difficulty_level == 1:
            n = df_of_options.shape[0]
            useing_n = int(n / 2)
            for i in range(useing_n):
                list_of_options.append((df_of_options['num_row'].iloc[i], df_of_options['num_column'].iloc[i]))
        return list_of_options

    def calculate_cost_of_move(self, num_row, num_column, game_field):
        start_costs = [
            [3, 0, 3],
            [0, 5, 0],
            [3, 0, 3]
        ]
        cost_of_move = start_costs[num_row][num_column]
        if self.check_win_at_one_move_tic_tac_toe(num_row, num_column, game_field):
            cost_of_move += 100
        if self.check_win_at_one_move_of_opponent_tic_tac_toe(num_row, num_column, game_field):
            cost_of_move += 50
        cost_of_move += self.get_cost_priority_move(num_row, num_column, game_field)
        return cost_of_move

    def check_win_at_one_move_tic_tac_toe(self, num_row, num_column, game_field):
        сurrent_gamer = self.__сurrent_game.сurrent_gamer
        for key_of_category_of_win_combinations in self.__win_combinations:
            category_of_win_combinations = self.__win_combinations[key_of_category_of_win_combinations]
            for win_combinations in category_of_win_combinations:
                for i in range(len(win_combinations)):
                    if num_row == win_combinations[i][0] and num_column == win_combinations[i][1]:
                        summ_win_combination = 0
                        for j in range(len(win_combinations)):
                            if j != i and game_field[win_combinations[j][0]][win_combinations[j][1]] is сurrent_gamer:
                                summ_win_combination += 1
                        if summ_win_combination == len(win_combinations) - 1:
                            return True
        return False  

    def check_win_at_one_move_of_opponent_tic_tac_toe(self, num_row, num_column, game_field):
        сurrent_gamer = self.__сurrent_game.сurrent_gamer
        for key_of_category_of_win_combinations in self.__win_combinations:
            category_of_win_combinations = self.__win_combinations[key_of_category_of_win_combinations]
            for win_combinations in category_of_win_combinations:
                for i in range(len(win_combinations)):
                    if num_row == win_combinations[i][0] and num_column == win_combinations[i][1]:
                        summ_win_combination = 0
                        for j in range(len(win_combinations)):
                            if j != i and not (game_field[win_combinations[j][0]][win_combinations[j][1]] is сurrent_gamer) and not (game_field[win_combinations[j][0]][win_combinations[j][1]].is_empty_value):
                                summ_win_combination += 1
                        if summ_win_combination == len(win_combinations) - 1:
                            return True
        return False

    def get_cost_priority_move(self, num_row, num_column, game_field):
        adding_cost = 10
        cost = 0
        сurrent_gamer = self.__сurrent_game.сurrent_gamer
        for key_of_category_of_win_combinations in self.__win_combinations:
            category_of_win_combinations = self.__win_combinations[key_of_category_of_win_combinations]
            for win_combinations in category_of_win_combinations:
                for i in range(len(win_combinations)):
                    if num_row == win_combinations[i][0] and num_column == win_combinations[i][1]:
                        summ_сurrent_gamer_combination = 0
                        summ_empty_field_combination = 0
                        for j in range(len(win_combinations)):
                            if j != i and game_field[win_combinations[j][0]][win_combinations[j][1]] is сurrent_gamer:
                                summ_сurrent_gamer_combination += 1
                            elif j != i and game_field[win_combinations[j][0]][win_combinations[j][1]] is self.__empty_value:
                                summ_empty_field_combination += 1
                        if summ_сurrent_gamer_combination == 1 and summ_empty_field_combination == 2:
                            cost =+ adding_cost
        return cost

    def set_difficulty_level(self, value):
        self.__difficulty_level = value