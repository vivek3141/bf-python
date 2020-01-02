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
