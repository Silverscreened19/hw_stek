class Stack:

    def __init__(self):
        self.stack = []

    def isEmpty(self):
        if len(self.stack) == 0:
            return True
        else:
            return False

    def push(self, el):
        self.stack.append(el)

    def pop(self):
        return self.stack.pop()

    def peek(self):
        return self.stack[len(self.stack) - 1]

    def size(self):
        return len(self.stack)


def parentheses():
    list_ = Stack()
    symbols = '{{[()]}}'
    for i in symbols:
        list_.push(i)
    while list_.isEmpty() is not True:
        if list_.size() % 2 == 0:
            for i in range(list_.size()):
                if i < list_.size():
                    if list_.stack[i] == '[' and list_.stack[i + 1] == ']':
                        del (list_.stack[i])
                        del (list_.stack[i])
                    elif list_.stack[i] == '(' and list_.stack[i + 1] == ')':
                        del (list_.stack[i])
                        del (list_.stack[i])
                    elif list_.stack[i] == '{' and list_.stack[i + 1] == '}':
                        del (list_.stack[i])
                        del (list_.stack[i])
                    else:
                        list_.stack.clear()
                        break

        else:
            print('Несбалансированная последовательность - нечетное число скобок')
            break
    if list_.isEmpty() is not False:
        print('Сбалансированная последовательность')
        print(len(list_.stack))
        print(list_.stack)


if __name__ == '__main__':
    parentheses()
