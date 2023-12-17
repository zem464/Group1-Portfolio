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

    def print_stack(self):
        current_node = self.top
        while current_node:
            print(current_node.data)
            current_node = current_node.next

    def infix_to_postfix_step_by_step(infix_expression):
        def precedence(operator):
            precedence_dict = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
            return precedence_dict.get(operator, 0)

        def is_operator(char):
            return char in "+-*/^"

        postfix = []
        stack = []

        print("\nOutput Postfix Steps:")

        for char in infix_expression:
            if char.isalnum():
                # Operand, append to output
                postfix.append(char)
                print(''.join(postfix))
            elif char == '(':
                # Left parenthesis, push onto stack
                stack.append(char)
            elif char == ')':
                # Right parenthesis, pop and append operators from the stack until '(' is encountered
                while stack and stack[-1] != '(':
                    postfix.append(stack.pop())
                stack.pop()  # Remove the '(' from the stack
                print(''.join(postfix))
            elif is_operator(char):
                # Operator
                while stack and precedence(stack[-1]) >= precedence(char):
                    postfix.append(stack.pop())
                stack.append(char)
                print(''.join(postfix))

        # Pop any remaining operators from the stack and append to the output
        while stack:
            postfix.append(stack.pop())
            print(''.join(postfix))

        print("\nFinal Postfix Expression:", ''.join(postfix))

    # Example usage:
    infix_expression = input("Input Infix: ")
    infix_to_postfix_step_by_step(infix_expression)
