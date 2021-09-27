from opcode import opmap

from asm.ops.abc import Opcode, NameOp


class LOAD_METHOD(NameOp):
    def __init__(self, arg: str):
        super().__init__(opmap["LOAD_METHOD"], arg)


class CALL_METHOD(Opcode):
    def __init__(self, arg: int):
        super().__init__(opmap["CALL_METHOD"], arg)
