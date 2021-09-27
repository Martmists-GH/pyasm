from opcode import opmap

from asm.ops.abc import Opcode


class LOAD_CLASSDEREF(Opcode):
    def __init__(self, arg: int):
        super().__init__(opmap["LOAD_CLASSDEREF"], arg)
