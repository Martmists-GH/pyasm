import sys
from opcode import opmap
from typing import TYPE_CHECKING

from asm.ops.abc import Opcode, RelJumpOp, CellOp

if TYPE_CHECKING:
    from asm.serializer import Label


class DUP_TOP_TWO(Opcode):
    def __init__(self):
        super().__init__(opmap["DUP_TOP_TWO"], 0)


class DELETE_DEREF(CellOp):
    def __init__(self, arg: str):
        super().__init__(opmap["DELETE_DEREF"], arg)


if sys.version_info < (3, 11):
    class SETUP_WITH(RelJumpOp):
        def __init__(self, arg: 'Label'):
            super().__init__(opmap["SETUP_WITH"], arg)
