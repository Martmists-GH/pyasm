import sys
from opcode import opmap, cmp_op
from typing import TYPE_CHECKING, Any

from asm.ops.abc import Opcode, AbsJumpOp, RelJumpOp
if TYPE_CHECKING:
    from asm.serializer import Label


class YIELD_FROM(Opcode):
    def __init__(self):
        super().__init__(opmap["YIELD_FROM"], 0)
