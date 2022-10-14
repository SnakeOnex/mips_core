from enum import Enum

# CONFIG
MEMORY_SIZE = 0x18000
# MEM_ENTRY = 0x80000000
MEM_ENTRY = 0x0
MEMORY_SIZE = 0x4000
PC = 32
REG_COUNT = 32

# MEMORY & REGISTERS INIT
memory = MEMORY_SIZE * b'\x00'
regs = REG_COUNT * b'\x00'

print("regs: ", regs)

class OPCode(Enum):
    # I type instructions
    addi  = 0b001000
    addiu = 0b001001
    andi  = 0b001100
    beq   = 0b000100
    
    bne   = 0b000101

    # J type instructions
    j     = 0b000010
    jal   = 0b000011

# OP code for R-type instructions (function code)
class OPXCode(Enum):
    add   = 0b100000
    addu  = 0b100001
    sub   = 0b100010
    subu  = 0b100011

    AND   = 0b100100
    OR    = 0b100101
    xor   = 0b100110
    nor   = 0b100111

    BREAK = 0b001101
    div   = 0b011010
    divu  = 0b011011

def read32(addr):
    if addr < 0 or addr >= len(memory):
        raise Exception("memory read out of bounds")
    return memory[addr:addr+4]

def run():
    class CPU_Stages(Enum):
        Fetch      = 0
        Execute    = 1
        Writeback  = 2

    stage = CPU_Stages.Fetch
    cycle_counter = 0

    print("stage: ", CPU_Stages((stage.value + 1) % 3))
    exit(0)

    # CPU loop
    while True:
        cycle_counter += 1

        # 1. fetch instruction
        if stage == CPU_Stages.Fetch:
            pass

        # 2. execute instruction
        if stage == CPU_Stages.Execute:
            pass

        # 3. writeback (+ incr of PC)
        if stage == CPU_Stages.Writeback:
            pass

        # go to next CPU stage
        stage = CPU_Stages((stage.value + 1) % 3) 

if __name__ == '__main__':
    run()
