from opcode import opmap

from asm.ops.abc import Opcode


class YIELD_FROM(Opcode):
    def __init__(self):
        super().__init__(opmap["YIELD_FROM"], 0)
