import sys
from opcode import opmap
from typing import TYPE_CHECKING

from asm.ops.abc import Opcode, RelJumpOp

if TYPE_CHECKING:
    from asm.serializer import Label


class BINARY_MATRIX_MULTIPLY(Opcode):
    def __init__(self):
        super().__init__(opmap["BINARY_MATRIX_MULTIPLY"], 0)


class INPLACE_MATRIX_MULTIPLY(Opcode):
    def __init__(self):
        super().__init__(opmap["INPLACE_MATRIX_MULTIPLY"], 0)


class GET_AITER(Opcode):
    def __init__(self):
        super().__init__(opmap["GET_AITER"], 0)


class GET_ANEXT(Opcode):
    def __init__(self):
        super().__init__(opmap["GET_ANEXT"], 0)


class BEFORE_ASYNC_WITH(Opcode):
    def __init__(self):
        super().__init__(opmap["BEFORE_ASYNC_WITH"], 0)


class GET_YIELD_FROM_ITER(Opcode):
    def __init__(self):
        super().__init__(opmap["GET_YIELD_FROM_ITER"], 0)


class GET_AWAITABLE(Opcode):
    def __init__(self):
        super().__init__(opmap["GET_AWAITABLE"], 0)


if sys.version_info < (3, 9):
    class WITH_CLEANUP_START(Opcode):
        def __init__(self):
            super().__init__(opmap["WITH_CLEANUP_START"], 0)


    class WITH_CLEANUP_FINISH(Opcode):
        def __init__(self):
            super().__init__(opmap["WITH_CLEANUP_START"], 0)

if sys.version_info < (3, 9):
    class BUILD_LIST_UNPACK(Opcode):
        def __init__(self, arg: int):
            super().__init__(opmap["BUILD_LIST_UNPACK"], arg)


    class BUILD_MAP_UNPACK(Opcode):
        def __init__(self, arg: int):
            super().__init__(opmap["BUILD_MAP_UNPACK"], arg)


    class BUILD_MAP_UNPACK_WITH_CALL(Opcode):
        def __init__(self, arg: int):
            super().__init__(opmap["BUILD_MAP_UNPACK_WITH_CALL"], arg)


    class BUILD_TUPLE_UNPACK(Opcode):
        def __init__(self, arg: int):
            super().__init__(opmap["BUILD_TUPLE_UNPACK"], arg)


    class BUILD_SET_UNPACK(Opcode):
        def __init__(self, arg: int):
            super().__init__(opmap["BUILD_SET_UNPACK"], arg)


class SETUP_ASYNC_WITH(RelJumpOp):
    def __init__(self, arg: 'Label'):
        super().__init__(opmap["SETUP_ASYNC_WITH"], arg)
