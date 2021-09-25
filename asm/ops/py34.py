import sys
from opcode import opmap, cmp_op
from typing import TYPE_CHECKING, Any

from asm.ops.abc import Opcode, AbsJumpOp, RelJumpOp
if TYPE_CHECKING:
    from asm.serializer import Label


class LOAD_CLASSDEREF(Opcode):
    def __init__(self, arg: int):
        super().__init__(opmap["LOAD_CLASSDEREF"], arg)
