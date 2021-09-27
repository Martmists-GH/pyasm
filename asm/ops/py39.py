import sys
from opcode import opmap
from typing import TYPE_CHECKING

from asm.ops.abc import Opcode, AbsJumpOp

if TYPE_CHECKING:
    from asm.serializer import Label

if sys.version_info < (3, 10):
    class RERAISE(Opcode):
        def __init__(self):
            super().__init__(opmap["RERAISE"], 0)


class WITH_EXCEPT_START(Opcode):
    def __init__(self):
        super().__init__(opmap["WITH_EXCEPT_START"], 0)


class LOAD_ASSERTION_ERROR(Opcode):
    def __init__(self):
        super().__init__(opmap["LOAD_ASSERTION_ERROR"], 0)


class LIST_TO_TUPLE(Opcode):
    def __init__(self):
        super().__init__(opmap["LIST_TO_TUPLE"], 0)


class IS_OP(Opcode):
    def __init__(self, arg: bool = False):
        super().__init__(opmap["IS_OP"], arg)


class CONTAINS_OP(Opcode):
    def __init__(self, arg: bool = False):
        super().__init__(opmap["CONTAINS_OP"], arg)


class JUMP_IF_NOT_EXC_MATCH(AbsJumpOp):
    def __init__(self, arg: 'Label'):
        super().__init__(opmap["JUMP_IF_NOT_EXC_MATCH"], arg)


class LIST_EXTEND(Opcode):
    def __init__(self, arg: int):
        super().__init__(opmap["LIST_EXTEND"], arg)


class SET_UPDATE(Opcode):
    def __init__(self, arg: int):
        super().__init__(opmap["SET_UPDATE"], arg)


class DICT_MERGE(Opcode):
    def __init__(self, arg: int):
        super().__init__(opmap["DICT_MERGE"], arg)


class DICT_UPDATE(Opcode):
    def __init__(self, arg: int):
        super().__init__(opmap["DICT_UPDATE"], arg)
