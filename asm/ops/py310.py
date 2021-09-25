import sys
from opcode import opmap, cmp_op
from typing import TYPE_CHECKING, Any

from asm.ops.abc import Opcode, AbsJumpOp, RelJumpOp
if TYPE_CHECKING:
    from asm.serializer import Label


class GET_LEN(Opcode):
    def __init__(self):
        super().__init__(opmap["GET_LEN"], 0)


class MATCH_MAPPING(Opcode):
    def __init__(self):
        super().__init__(opmap["MATCH_MAPPING"], 0)


class MATCH_SEQUENCE(Opcode):
    def __init__(self):
        super().__init__(opmap["MATCH_SEQUENCE"], 0)


class MATCH_KEYS(Opcode):
    def __init__(self):
        super().__init__(opmap["MATCH_KEYS"], 0)


class COPY_DICT_WITHOUT_KEYS(Opcode):
    def __init__(self):
        super().__init__(opmap["COPY_DICT_WITHOUT_KEYS"], 0)


class ROT_N(Opcode):
    def __init__(self, arg: int):
        super().__init__(opmap["ROT_N"], arg)


class RERAISE(Opcode):
    def __init__(self, arg: bool = False):
        super().__init__(opmap["RERAISE"], arg)


class GEN_START(Opcode):
    def __init__(self, arg: int):
        super().__init__(opmap["GEN_START"], arg)


class MATCH_CLASS(Opcode):
    def __init__(self, arg: int):
        super().__init__(opmap["MATCH_CLASS"], arg)
