from opcode import opmap
from typing import TYPE_CHECKING

from asm.ops.abc import Opcode, AbsJumpOp

if TYPE_CHECKING:
    from asm.serializer import Label


class JUMP_IF_FALSE_OR_POP(AbsJumpOp):
    def __init__(self, arg: 'Label'):
        super().__init__(opmap["JUMP_IF_FALSE_OR_POP"], arg)


class JUMP_IF_TRUE_OR_POP(AbsJumpOp):
    def __init__(self, arg: 'Label'):
        super().__init__(opmap["JUMP_IF_TRUE_OR_POP"], arg)


class POP_JUMP_IF_FALSE(AbsJumpOp):
    def __init__(self, arg: 'Label'):
        super().__init__(opmap["POP_JUMP_IF_FALSE"], arg)


class POP_JUMP_IF_TRUE(AbsJumpOp):
    def __init__(self, arg: 'Label'):
        super().__init__(opmap["POP_JUMP_IF_TRUE"], arg)


class LIST_APPEND(Opcode):
    def __init__(self, arg: int):
        super().__init__(opmap["LIST_APPEND"], arg)


class SET_ADD(Opcode):
    def __init__(self, arg: int):
        super().__init__(opmap["SET_ADD"], arg)


class MAP_ADD(Opcode):
    def __init__(self, arg: int):
        super().__init__(opmap["MAP_ADD"], arg)
