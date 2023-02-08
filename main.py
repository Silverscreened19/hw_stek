class Stack:
    def __init__(self):
        self.stack = []

    def is_empty(self):
        return self.stack == []

    def push(self, el):
        self.stack.append(el)

    def pop(self):
        return self.stack.pop()

    def peek(self):
        return self.stack[-1]

    def size(self):
        return len(self.stack)


def balanced(line):
    stack = Stack()
    for el in line:
        stack.push(el)
    a = 0
    while stack.is_empty() == False:
        a += 1
        if a == stack.size() and stack.is_empty() == False:
            return f'not balanced not paired'
        if stack.size() % 2 == 0:
            for i in range(stack.size()):
                if i < stack.size():
                    if stack.stack[i] == '(' and stack.stack[i+1] == ')':
                        del (stack.stack[i])
                        del (stack.stack[i])
                    elif stack.stack[i] == '[' and stack.stack[i+1] == ']':
                        del (stack.stack[i])
                        del (stack.stack[i])
                    elif stack.stack[i] == '{' and stack.stack[i+1] == '}':
                        del (stack.stack[i])
                        del (stack.stack[i])
        else:
            return f'not balanced not equal'

    if stack.is_empty() == True:
        return f'balanced'


if __name__ == '__main__':
    stack = Stack()
    list_of_lines = [
        '[([])((([[[]]])))]{()}', '(((([{}]))))', '{{[()]}}', '}{}', '{{[(])]}}', '[[{())}]']
    for line in list_of_lines:
        print(f'{line} is {balanced(line)}')
