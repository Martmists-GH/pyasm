import sys
from opcode import opmap, cmp_op
from typing import TYPE_CHECKING, Any

from asm.ops.abc import Opcode, AbsJumpOp, RelJumpOp, NameOp

if TYPE_CHECKING:
    from asm.serializer import Label


class SETUP_ANNOTATIONS(Opcode):
    def __init__(self):
        super().__init__(opmap["SETUP_ANNOTATIONS"], 0)


if sys.version_info < (3, 7):
    class STORE_ANNOTATION(NameOp):
        def __init__(self, arg: str):
            super().__init__(opmap["STORE_ANNOTATION"], arg)


class CALL_FUNCTION_EX(Opcode):
    def __init__(self, arg: int):
        super().__init__(opmap["CALL_FUNCTION_EX"], arg)


class FORMAT_VALUE(Opcode):
    # TODO: Flags?
    def __init__(self, arg: int):
        super().__init__(opmap["FORMAT_VALUE"], arg)


class BUILD_CONST_KEY_MAP(Opcode):
    def __init__(self, arg: int):
        super().__init__(opmap["BUILD_CONST_KEY_MAP"], arg)


class BUILD_STRING(Opcode):
    def __init__(self, arg: int):
        super().__init__(opmap["BUILD_STRING"], arg)


if sys.version_info < (3, 9):
    class BUILD_TUPLE_UNPACK_WITH_CALL(Opcode):
        def __init__(self, arg: int):
            super().__init__(opmap["BUILD_TUPLE_UNPACK_WITH_CALL"], arg)
