class CPU():
    def __init__(self) -> None:
        self.reset()
        self.load()

    def load(self):
        self.RAM[0] = 0x1e
        self.RAM[14] = 0xFF
        self.RAM[1] = 0xF0

    def reset(self) -> None:
        # 8-bit
        self.A = 0
        
        # 8-bit
        self.B = 0
        
        # 8-bit
        self.OUT = 0
        
        # 8-bit
        self.IR = 0
        
        # 4-bit
        self.PC = 0
        
        # 1-bit
        self.ZF = False
        
        # 1-bit
        self.CF = False

        # 1-bit
        self.HALT = False

        # 16 bytes
        self.RAM = [0] * 16

    def debug(self) -> None:
        print(f"Register A:     {hex(self.A)}")
        print(f"Register B:     {hex(self.B)}")
        print(f"Register OUT:   {hex(self.OUT)}")
        print(f"Register IR:    {hex(self.IR)}")
        print(f"Register PC:    {bin(self.PC)}")
        print(f"Register ZF:    {bin(self.ZF)}")
        print(f"Register CF:    {bin(self.CF)}")
        print(f"Register HALT:  {bin(self.HALT)}")
        print(f"Register RAM:   {[hex(ram_cell) for ram_cell in self.RAM]}")

    def execute(self) -> None:
        opcode = (self.IR & 0xF0) >> 4
        argument = self.IR & 0x0F

        match opcode:
            case 0x0000:
                pass
            case 0x0001:
                # LDA
                self.A = self.RAM[argument]
            case 0x0010:
                # ADD
                self.B = self.RAM[argument]
                self.A = (self.A + self.B) & 0xFF
                self.CF = (self.A + self.B) > 0xFF
                self.ZF = self.A == 0
            case 0x0011:
                # SUB
                self.CF = (self.A - self.B) < 0x00
                self.ZF = self.A == 0
            case 0x0100:
                # STA
                self.RAM[argument] = self.A
            case 0x0101:
                # LDI
                self.A = argument
            case 0x0110:
                # JMP
                self.PC = argument - 1
            case 0x0111:
                # JC
                if self.CF == True:
                    self.PC = argument - 1
            case 0x1000:
                # JZ
                if self.ZF == True:
                    self.PC = argument - 1
            case 0x1110:
                # OUT
                self.OUT = self.A
                print(f"> {self.OUT}")             
            case 0x1111:
                # NOP
                self.HALT = True
            
        print(f"Opcode: {hex(opcode)}", end=" ")
        print(f"Argument: {hex(argument)}", end=" ")
        print(f"PC: {self.PC}")

    def run(self) -> None:
        try:
            while not self.HALT:
                print(f"{self.HALT=}")
                self.IR = self.RAM[self.PC]
                
                self.execute()
                
                self.PC += 1
        except:
            pass
        print("All done")

cpu = CPU()
cpu.debug()
cpu.run()
cpu.debug()