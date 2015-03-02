class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        """
        :return: Shows last item in the stack
        """
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)



def revstring(word):
    """return a reversed string using Stack"""
    s = Stack()
    for letter in word:
        s.push(letter)
    reverse = ""
    while not s.isEmpty():
        reverse += s.pop()
    return reverse


def parenthesisParser(symbolString):
    """parses a string and tries to see it open and closed parenthesis correspond to eachother"""
    s = Stack()
    correspond = True
    index = 0
    while index < len(symbolString) and correspond:
        symbol = symbolString[index]
        if symbol == "(":
            s.push(symbol)
        else:
            if s.isEmpty():
                correspond = False
            else:
                s.pop()
        index += 1
    if correspond and s.isEmpty():
        return True
    else:
        return False

def matches(open, close):
    """ Returns true if the open and close params correspond to their symbols '([{' opening and closing repreentations"""
    opens = "[{("
    closers = "]})"
    return opens.index(open) == closers.index(close) 


def symbolParser(symbolString):
    """ parses a string to see if the '(,[,{' symbols match their closing parts """

    s = Stack()
    correspond = True
    index = 0
    while index < len(symbolString) and correspond:
        symbol = symbolString[index]
        if symbol in "([{":
            s.push(symbol)
        else:
            if s.isEmpty():
                correspond = False
            else:
                top = s.pop()
                if not matches(top, symbol):
                    correspond = False
        index += 1
    if correspond and s.isEmpty():
        return True
    else:
        return False

