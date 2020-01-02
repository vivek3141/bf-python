class Node:
    def __init__(self, value, children, parent):
        self.value = value
        self.children = children
        self.parent = parent

    def __str__(self):
        return f"Value : {self.value}, Children: {[str(i) for i in self.children]}"


with open("test.bf", "r") as f:
    code = f.read()
code = "".join(
    list(filter(lambda x: x in ['+', '-', '[', ']', '<', '>', '.', ','], code)))

memory = [0]
ptr = 0

tree = Node(None, [], None)
tmap = {}
c = tree

for n, i in enumerate(code):
    if i == "[":
        c.children.append(Node(n, [], c))
        c = c.children[-1]

    elif i == "]":
        tmap[c.value] = n
        tmap[n] = c.value
        c = c.parent
cptr = 0
while(cptr < len(code)):
    if ptr >= len(memory):
        memory.append(0)
    i = code[cptr]
    if i == ">":
        ptr += 1

    elif i == "<":
        ptr = ptr - 1 if ptr > 0 else 0

    elif i == "+":
        memory[ptr] = memory[ptr] + 1 if memory[ptr] < 255 else 0

    elif i == "-":
        memory[ptr] = memory[ptr] - 1 if memory[ptr] < 255 else 0

    elif i == "[" and memory[ptr] == 0:
        cptr = tmap[cptr]

    elif i == "]" and memory[ptr] != 0:
        cptr = tmap[cptr]

    elif i == ".":
        print(chr(memory[ptr]), end='')

    cptr += 1

print(ptr, memory)
class BF:
    def __init__(self, file_name):
        with open(file_name, "r") as f:
            self.code = f.read()

        self.memory = [0]
        self.ptr = 0

        self.lex()

    def lex(self):
        self.tree = Node(None, [], None)
        self.map = {}
        c = self.tree

        for n, i in enumerate(self.code):
            if i == "[":
                c.children.append(Node(n, [], c))
                c = c.children[-1]

            elif i == "]":
                self.map[c.value] = n
                c = c.parent

    def eval(self):
        while(self.ptr < len(self.code)):
            if self.code:
                pass

    def exec(self):
        idx = 0
        for n, i in enumerate(self.code):
            if i == "[":
                idx = n
                break

            elif i == ">":
                self.ptr += 1
                if self.ptr >= len(self.memory):
                    self.memory.append(0)

            elif i == "<":
                self.ptr = self.ptr - 1 if self.ptr > 0 else 0

            elif i == "+":
                self.memory[self.ptr] = self.memory[self.ptr] + \
                    1 if self.memory[self.ptr] < 255 else 0

            elif i == "-":
                self.memory[self.ptr] = self.memory[self.ptr] - \
                    1 if self.memory[self.ptr] < 255 else 0
        self.eval(code[idx:], self.tree)

    def exec(self, code):
        for n, i in enumerate(self.code):
            if i == "[":
                idx = n
                break

            elif i == ">":
                self.ptr += 1
                if self.ptr >= len(self.memory):
                    self.memory.append(0)

            elif i == "<":
                self.ptr = self.ptr - 1 if self.ptr > 0 else 0

            elif i == "+":
                self.memory[self.ptr] = self.memory[self.ptr] + \
                    1 if self.memory[self.ptr] < 255 else 0

            elif i == "-":
                self.memory[self.ptr] = self.memory[self.ptr] - \
                    1 if self.memory[self.ptr] < 255 else 0
        self.eval(code[idx:], self.tree)

    def eval(self, code, nodes):
        for i in nodes:
            while(self.memory[self.ptr] != 0):
                pass
