from typing import List

def get_array_of_inputs(file_path: str) -> List[str]:
    with open(file_path, 'r') as file:
        lines = file.readlines()

    word_list = [word.strip() for word in lines]
    return word_list

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node