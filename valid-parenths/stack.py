class Stack:
    def __init__(self):
        self.top = None

    def push(self, value):
        new_node = StackNode(value)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if not self.top:
            return None
        else:
            return_value = self.top.value
            self.top = self.top.next
            return return_value

class StackNode:
    def __init__(self, value):
        self.value = value
        self.next = None

stack = Stack()

class Solution:
    def isValid(self, s: str) -> bool:       
        bracket_stack = Stack()
        opening = ['(', '{', '[']
        closing = [')', '}', ']']
        for bracket in s:
            if bracket in opening:
                bracket_stack.push(bracket)
            elif bracket in closing:
                last_bracket = bracket_stack.pop()
                if last_bracket == None:
                    return False
                elif closing.index(bracket) != opening.index(last_bracket):
                    return False
        if bracket_stack.pop() == None:
            return True
        return False
            

