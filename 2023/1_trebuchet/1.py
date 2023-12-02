from typing import List
from utils import get_array_of_inputs, LinkedList

def find_first_number_from_string(word: str) -> str:
    for char in word:
        if char.isnumeric():
            return char
    return '0'

def calculate_sum_of_calibrating_values(words: List[str]) -> int:
    sum = 0
    for word in words:
        value = ''
        value += find_first_number_from_string(word)
        value += find_first_number_from_string(word[::-1])
        sum += int(value)
    return sum

words = get_array_of_inputs('2023/1_trebuchet/1.txt')
print(calculate_sum_of_calibrating_values(words))


class Path:
    def __init__(self, word: str, value: str):
        self.value = value
        self.linked_list = LinkedList()
        for s in word:
            self.linked_list.append(s)
        self._active_node = self.linked_list.head


    def reset(self) -> bool:
        """Resets the active element to the first of the path.

        Returns:
            bool: True if the active element was changed, False otherwise .
        """
        changed = self._active_node != self.linked_list.head
        self._active_node = self.linked_list.head
        return changed
        
    def walk(self) -> bool:
        """Move the active element to the next node in the path.

        If it reached the end, resets the path.

        Returns:
            bool: True if reached the end of the path, False otherwise.
        """
        if self._active_node.next == None:
            self.reset()
            return True
        self._active_node = self._active_node.next
        return False

    @property
    def active(self) -> str:
        return self._active_node.data



def reset_paths(paths: List[Path]) -> None:
    for path in paths:
        path.reset()

def calculate_sum_of_calibrating_values_considering_spelled_numbers(words: List[str]) -> int:
    active_paths = [
        Path('one', '1'),
        Path('two', '2'),
        Path('three', '3'),
        Path('four', '4'),
        Path('five', '5'),
        Path('six', '6'),
        Path('seven', '7'),
        Path('eight', '8'),
        Path('nine', '9'),
    ]
    sum = 0
    for word in words:
        reset_paths(active_paths)
        first = None
        last = None
        for char in word:
            if char.isnumeric():
                if first is None:
                    first = char
                last = char
            else:
                for path in active_paths:
                    if path.active == char:
                        if path.walk():
                            if first is None:
                                first = path.value
                            last = path.value
                    else:
                        if path.reset() and path.active == char:
                            path.walk()
        value = first + last
        sum += int(value)
    return sum

words = get_array_of_inputs('2023/1_trebuchet/1.txt')
print(calculate_sum_of_calibrating_values_considering_spelled_numbers(words))