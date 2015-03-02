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

    