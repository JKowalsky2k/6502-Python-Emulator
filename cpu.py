class CPU():
    def __init__(self) -> None:
        self.reset()

    def reset(self) -> None:
        self.A = 0
        self.B = 0
        self.OUT = 0
        self.IR = 0
        self.PC = 0
        self.ZF = False
        self.CF = False
        self.HALT = False

    def debug(self) -> None:
        print(f"Register A: {self.A}")
        print(f"Register B: {self.B}")
        print(f"Register OUT: {self.OUT}")
        print(f"Register IR: {self.IR}")
        print(f"Register PC: {self.PC}")
        print(f"Register ZF: {self.ZF}")
        print(f"Register CF: {self.CF}")
        print(f"Register HALT: {self.HALT}")
