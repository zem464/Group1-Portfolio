class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None

    def push(self, data):
        new_node = Node(data)
        if self.top:
            new_node.next = self.top
        self.top = new_node

    def pop(self):
        if self.top is None:
            return None
        else:
            popped_node = self.top
            self.top = self.top.next
            popped_node.next = None
            return popped_node.data

    def peek(self):
        if self.top:
            return self.top.data
        else:
            return None

    def is_empty(self):
        return self.top is None

    def infix_to_postfix_step_by_step(self, infix_expression):
        def precedence(operator):
            precedence_dict = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
            return precedence_dict.get(operator, 0)

        def is_operator(char):
            return char in "+-*/^"

        postfix = []
        steps = set()

        for char in infix_expression:
            current = ''.join(postfix)
            steps.add(current)

            if char.isalnum():
                # Operand, append to output
                postfix.append(char)
            elif char == '(':
                # Left parenthesis, push onto stack
                self.push(char)
            elif char == ')':
                # Right parenthesis, pop and append operators from the stack until '(' is encountered
                while not self.is_empty() and self.peek() != '(':
                    postfix.append(self.pop())
                self.pop()  # Remove the '(' from the stack
            elif is_operator(char):
                # Operator
                while not self.is_empty() and precedence(self.peek()) >= precedence(char):
                    postfix.append(self.pop())
                self.push(char)

        # Pop any remaining operators from the stack and append to the output
        while not self.is_empty():
            postfix.append(self.pop())
            steps.add(''.join(postfix))

        # Convert the set of steps to a list and sort it for consistency
        sorted_steps = sorted(list(steps))

        return ''.join(postfix), sorted_steps

