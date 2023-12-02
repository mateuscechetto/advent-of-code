from typing import List, Dict

class CustomDict(dict):
    def __setitem__(self, key, value):
        if key in self:
            if value > self[key]:
                super().__setitem__(key, value)
        else:
            super().__setitem__(key, value)
    
    def is_possible_with(self, dict_to_compare: Dict) -> bool:
        for key, value in dict_to_compare.items():
            if key not in self or value < self[key]:
                return False
        return True


def get_array_of_inputs(file_path: str) -> List[str]:
    with open(file_path, 'r') as file:
        lines = file.readlines()

    lines = [line.strip() for line in lines]
    return lines

def create_dict_from_string(input_string: str) -> CustomDict:
    data = CustomDict()
    game_results = input_string.split(';')
    for game_result in game_results:
        results = game_result.strip().split(', ')
        for result in results:
            value, color = result.split(' ')
            data[color] = int(value)
    return data

def create_games(lines: List[str]) -> Dict[str, CustomDict]:
    games = {}
    for line in lines:
        game_and_id, game_results = line.split(':')
        game_id = game_and_id.strip().split(' ')[1]
        game = create_dict_from_string(game_results)
        games[game_id] = game
    return games

def sum_of_valid_games(games: Dict[str, CustomDict], bag: Dict[str, int]) -> int:
    sum = 0
    for game_id, game in games.items():
        if game.is_possible_with(bag):
            sum += int(game_id)
    return sum

test = create_games(get_array_of_inputs('2023/2_cube_conundrum/test.txt'))
lines = get_array_of_inputs('2023/2_cube_conundrum/input.txt')
bag = {'red': 12, 'green': 13, 'blue': 14}
games = create_games(lines)
print(sum_of_valid_games(games, bag))

def sum_of_power_of_minimum_bag(games: Dict[str, CustomDict]) -> int:
    sum = 0
    for game in games.values():
        power = 1
        for value in game.values():
            power *= value
        sum += power
    return sum


print(sum_of_power_of_minimum_bag(games))
