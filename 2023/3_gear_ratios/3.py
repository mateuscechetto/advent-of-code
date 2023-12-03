import string
import math
from typing import List, Tuple


def generate_neighbours_positions(line_index: int, column_index: int) -> List[Tuple[int, int]]:
    neighbours = []
    for i in range(-1, 2):
        for j in range(-1, 2):
            if i != 0 or j != 0:  # Exclude the center point itself
                neighbours.append((line_index + i, column_index + j))
    return neighbours

def is_valid_position(position: Tuple[int, int], lines: List[str]) -> bool:
    y, x = position
    if y < 0:
        return False
    if y >= len(lines):
        return False
    if x < 0:
        return False
    if x >= len(lines[y]):
        return False
    return True

def check_symbol_on_neighbours(lines: List[str], line_index: int, column_index: int) -> bool:
    symbols = string.punctuation.replace('.', '')
    neighbours_positions = generate_neighbours_positions(line_index, column_index)
    neighbours_positions = [position for position in neighbours_positions if is_valid_position(position, lines)]
    for x, y in neighbours_positions:
        if lines[x][y] in symbols:
            return True
    return False


def sum_numbers_adjacents_to_symbol(lines: List[str]) -> int:
    sum = 0
    for line_index in range(0, len(lines)):
        line = lines[line_index]
        current_number = ''
        is_current_number_a_part_number = False
        for index in range(0, len(line)):
            char = line[index]
            if char.isnumeric():
                current_number += char
                if not is_current_number_a_part_number and check_symbol_on_neighbours(lines, line_index, index):
                    is_current_number_a_part_number = True
            else:
                if is_current_number_a_part_number:
                    sum += int(current_number)
                is_current_number_a_part_number = False
                current_number = ''
        if is_current_number_a_part_number:
            sum += int(current_number) 
    return sum

def get_array_of_inputs(file_path: str) -> List[str]:
    with open(file_path, 'r') as file:
        lines = file.readlines()

    lines = [line.strip() for line in lines]
    return lines

test = get_array_of_inputs('2023/3_gear_ratios/test.txt')
lines = get_array_of_inputs('2023/3_gear_ratios/input.txt')

print(sum_numbers_adjacents_to_symbol(test))
print(sum_numbers_adjacents_to_symbol(lines))

def find_numbers_coordinates(lines: List[str]) -> List[List[Tuple[int, int]]]:
    number_coords = []
    for i in range(len(lines)):
        number = []
        for j in range(len(lines[i])):
            if not lines[i][j].isdigit() and number:
                number_coords.append(number)
                number = []
            if lines[i][j].isdigit():
                number.append((i, j))
        if number:
            number_coords.append(number)
    
    return number_coords 

def sum_gear_ratios(lines: List[str]) -> int:
    sum = 0
    gears = [(i, j) for i in range(len(lines)) for j in range(len(lines)) if lines[i][j] == "*"]
    number_coords = find_numbers_coordinates(lines)
    for i, j in gears:
        neighbours_nums = []
        neighbours_positions = generate_neighbours_positions(i,j)
        neighbours_positions = [position for position in neighbours_positions if is_valid_position(position, lines)]
        for number in number_coords:
            if any((row, column) in number for row,column in neighbours_positions):
                neighbours_nums.append(int("".join(lines[r][c] for r,c in number)))
        if len(neighbours_nums) == 2:
            sum += math.prod(neighbours_nums)
    return sum


print(sum_gear_ratios(test))
print(sum_gear_ratios(lines))