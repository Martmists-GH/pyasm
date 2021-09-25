import sys
from opcode import opmap, cmp_op
from typing import TYPE_CHECKING, Any

from asm.ops.abc import Opcode, AbsJumpOp, RelJumpOp, NameOp

if TYPE_CHECKING:
    from asm.serializer import Label


class LOAD_METHOD(NameOp):
    def __init__(self, arg: str):
        super().__init__(opmap["LOAD_METHOD"], arg)


class CALL_METHOD(Opcode):
    def __init__(self, arg: int):
        super().__init__(opmap["CALL_METHOD"], arg)
