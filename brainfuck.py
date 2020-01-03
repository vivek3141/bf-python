import sys

with open(sys.argv[1], "r") as f:
    code = f.read()
code = "".join(
    list(filter(lambda x: x in ['+', '-', '[', ']', '<', '>', '.', ','], code)))

memory = [0]
ptr = 0

stack = []
tmap = {}

for n, i in enumerate(code):
    if i == "[":
        stack.append(n)
    elif i == "]":
        v = stack.pop()
        tmap[v] = n
        tmap[n] = v

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

    elif i == ",":
        memory[ptr] = input()

    cptr += 1
