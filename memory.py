class Memory:
    def __init__(self):
        self.mem = [0]
        self.current = 0
    
    def add_pointer(self):
        self.mem.append(0)
        self.current += 1
    
    def add_value(self):
        self.mem[self.current] = self.mem[self.current] + 1 if self.mem