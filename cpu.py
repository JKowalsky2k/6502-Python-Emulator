class CPU():
    def __init__(self) -> None:
        self.instructions = {
            "0x0": "NOP",
            "0x1": "LDA",
            "0x2": "ADD",
            "0x3": "SUB",
            "0x4": "STA",
            "0x5": "LDI",
            "0x6": "JMP",
            "0x7": "JC",
            "0x8": "JZ",
            "0xe": "OUT",
            "0xf": "HLT"
        }
        self.reset()
        self.load()

    def load(self):
        self.RAM[0]     = 0x2e
        self.RAM[1]     = 0xe0
        self.RAM[2]     = 0x4f
        self.RAM[3]     = 0x2e
        self.RAM[4]     = 0xe0
        self.RAM[5]     = 0x7b
        self.RAM[6]     = 0x4e
        self.RAM[7]     = 0x2f
        self.RAM[8]     = 0xe0
        self.RAM[9]     = 0x7b
        self.RAM[10]    = 0x61
        self.RAM[11]    = 0xf0
        self.RAM[12]    = 0x0
        self.RAM[13]    = 0x0
        self.RAM[14]    = 0x1
        self.RAM[15]    = 0x1


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
        print(f"Register IR:    {hex(self.IR)} -> {self.instructions[str(hex((self.IR & 0xF0) >> 4))]}")
        print(f"Register PC:    {bin(self.PC)}")
        print(f"Register ZF:    {bin(self.ZF)}")
        print(f"Register CF:    {bin(self.CF)}")
        print(f"Register HALT:  {bin(self.HALT)}")
        print(f"Register RAM:   {[hex(ram_cell) for ram_cell in self.RAM]}")

    def execute(self) -> None:
        opcode = (self.IR & 0xF0) >> 4
        argument = self.IR & 0x0F

        match opcode:
            case 0b0000:
                # NOP
                # print(f"DEBUG: NOP")
                pass
            case 0x0001:
                # LDA
                # print(f"DEBUG: LDA")
                self.A = self.RAM[argument]
            case 0b0010:
                # ADD
                # print(f"DEBUG: ADD")
                self.B = self.RAM[argument]
                self.A = (self.A + self.B) & 0xFF
                self.CF = (self.A + self.B) > 0xFF
                self.ZF = self.A == 0
            case 0b0011:
                # SUB
                # print(f"DEBUG: SUB")
                self.CF = (self.A - self.B) < 0x00
                self.ZF = self.A == 0
            case 0b0100:
                # STA
                # print(f"DEBUG: STA")
                self.RAM[argument] = self.A
            case 0b0101:
                # LDI
                # print(f"DEBUG: LDI")
                self.A = argument
            case 0b0110:
                # JMP
                # print(f"DEBUG: JMP")
                self.PC = argument - 1
            case 0b0111:
                # JC
                # print(f"DEBUG: JC")
                if self.CF == True:
                    self.PC = argument - 1
            case 0b1000:
                # JZ
                # print(f"DEBUG: JZ")
                if self.ZF == True:
                    self.PC = argument - 1
            case 0b1110:
                # OUT
                # print(f"DEBUG: OUT")
                self.OUT = self.A
                print(f"> {self.OUT}")             
            case 0b1111:
                # HALT
                # print(f"DEBUG: HALT")
                self.HALT = True
            
        # print(f"Opcode: {hex(opcode)}", end=" ")
        # print(f"Argument: {hex(argument)}", end=" ")
        # print(f"PC: {self.PC}")

    def run(self) -> None:
        try:
            while not self.HALT:
                self.IR = self.RAM[self.PC]
                
                self.execute()
                
                self.PC += 1
                # self.debug()
                # input("Press Enter to continue...")
        except:
            pass
        print("All done")

cpu = CPU()
# cpu.debug()
cpu.run()
cpu.debug()