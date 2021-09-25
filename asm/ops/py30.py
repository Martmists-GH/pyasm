import sys
from opcode import opmap, cmp_op
from typing import TYPE_CHECKING, Any

from asm.ops.abc import Opcode, AbsJumpOp, RelJumpOp, VarOp, ConstOp, NameOp, CellOp

if TYPE_CHECKING:
    from asm.serializer import Label


class POP_TOP(Opcode):
    def __init__(self):
        super().__init__(opmap["POP_TOP"], 0)


class ROT_TWO(Opcode):
    def __init__(self):
        super().__init__(opmap["ROT_TWO"], 0)


class ROT_THREE(Opcode):
    def __init__(self):
        super().__init__(opmap["ROT_THREE"], 0)


class DUP_TOP(Opcode):
    def __init__(self):
        super().__init__(opmap["DUP_TOP"], 0)


if sys.version_info < (3, 2):
    class ROT_FOUR(Opcode):
        def __init__(self):
            super().__init__(opmap["ROT_FOUR"], 0)


class NOP(Opcode):
    def __init__(self):
        super().__init__(opmap["NOP"], 0)


class UNARY_POSITIVE(Opcode):
    def __init__(self):
        super().__init__(opmap["UNARY_POSITIVE"], 0)


class UNARY_NEGATIVE(Opcode):
    def __init__(self):
        super().__init__(opmap["UNARY_NEGATIVE"], 0)


class UNARY_NOT(Opcode):
    def __init__(self):
        super().__init__(opmap["UNARY_NOT"], 0)


class UNARY_INVERT(Opcode):
    def __init__(self):
        super().__init__(opmap["UNARY_INVERT"], 0)


if sys.version_info < (3, 1):
    class SET_ADD(Opcode):
        def __init__(self, arg: int):
            super().__init__(opmap["SET_ADD"], arg)


    class LIST_APPEND(Opcode):
        def __init__(self, arg: int):
            super().__init__(opmap["LIST_APPEND"], arg)


class BINARY_POWER(Opcode):
    def __init__(self):
        super().__init__(opmap["BINARY_POWER"], 0)


class BINARY_MULTIPLY(Opcode):
    def __init__(self):
        super().__init__(opmap["BINARY_MULTIPLY"], 0)


class BINARY_MODULO(Opcode):
    def __init__(self):
        super().__init__(opmap["BINARY_MODULO"], 0)


class BINARY_ADD(Opcode):
    def __init__(self):
        super().__init__(opmap["BINARY_ADD"], 0)


class BINARY_SUBTRACT(Opcode):
    def __init__(self):
        super().__init__(opmap["BINARY_SUBTRACT"], 0)


class BINARY_SUBSCR(Opcode):
    def __init__(self):
        super().__init__(opmap["BINARY_SUBSCR"], 0)


class BINARY_FLOOR_DIVIDE(Opcode):
    def __init__(self):
        super().__init__(opmap["BINARY_FLOOR_DIVIDE"], 0)


class BINARY_TRUE_DIVIDE(Opcode):
    def __init__(self):
        super().__init__(opmap["BINARY_TRUE_DIVIDE"], 0)


class INPLACE_FLOOR_DIVIDE(Opcode):
    def __init__(self):
        super().__init__(opmap["INPLACE_FLOOR_DIVIDE"], 0)


class INPLACE_TRUE_DIVIDE(Opcode):
    def __init__(self):
        super().__init__(opmap["INPLACE_TRUE_DIVIDE"], 0)


if sys.version_info < (3, 5):
    class STORE_MAP(Opcode):
        def __init__(self):
            super().__init__(opmap["STORE_MAP"], 0)


class INPLACE_ADD(Opcode):
    def __init__(self):
        super().__init__(opmap["INPLACE_ADD"], 0)


class INPLACE_SUBTRACT(Opcode):
    def __init__(self):
        super().__init__(opmap["INPLACE_SUBTRACT"], 0)


class INPLACE_MULTIPLY(Opcode):
    def __init__(self):
        super().__init__(opmap["INPLACE_MULTIPLY"], 0)


class INPLACE_MODULO(Opcode):
    def __init__(self):
        super().__init__(opmap["INPLACE_MODULO"], 0)


class STORE_SUBSCR(Opcode):
    def __init__(self):
        super().__init__(opmap["STORE_SUBSCR"], 0)


class DELETE_SUBSCR(Opcode):
    def __init__(self):
        super().__init__(opmap["DELETE_SUBSCR"], 0)


class BINARY_LSHIFT(Opcode):
    def __init__(self):
        super().__init__(opmap["BINARY_LSHIFT"], 0)


class BINARY_RSHIFT(Opcode):
    def __init__(self):
        super().__init__(opmap["BINARY_RSHIFT"], 0)


class BINARY_AND(Opcode):
    def __init__(self):
        super().__init__(opmap["BINARY_AND"], 0)


class BINARY_XOR(Opcode):
    def __init__(self):
        super().__init__(opmap["BINARY_XOR"], 0)


class BINARY_OR(Opcode):
    def __init__(self):
        super().__init__(opmap["BINARY_OR"], 0)


class INPLACE_POWER(Opcode):
    def __init__(self):
        super().__init__(opmap["INPLACE_POWER"], 0)


class GET_ITER(Opcode):
    def __init__(self):
        super().__init__(opmap["GET_ITER"], 0)


if sys.version_info < (3, 4):
    class STORE_LOCALS(Opcode):
        def __init__(self):
            super().__init__(opmap["STORE_LOCALS"], 0)


class PRINT_EXPR(Opcode):
    def __init__(self):
        super().__init__(opmap["PRINT_EXPR"], 0)


class LOAD_BUILD_CLASS(Opcode):
    def __init__(self):
        super().__init__(opmap["LOAD_BUILD_CLASS"], 0)


class INPLACE_LSHIFT(Opcode):
    def __init__(self):
        super().__init__(opmap["INPLACE_LSHIFT"], 0)


class INPLACE_RSHIFT(Opcode):
    def __init__(self):
        super().__init__(opmap["INPLACE_RSHIFT"], 0)


class INPLACE_AND(Opcode):
    def __init__(self):
        super().__init__(opmap["INPLACE_AND"], 0)


class INPLACE_XOR(Opcode):
    def __init__(self):
        super().__init__(opmap["INPLACE_XOR"], 0)


class INPLACE_OR(Opcode):
    def __init__(self):
        super().__init__(opmap["INPLACE_OR"], 0)


if sys.version_info < (3, 8):
    class BREAK_LOOP(Opcode):
        def __init__(self):
            super().__init__(opmap["BREAK_LOOP"], 0)


if sys.version_info < (3, 5):
    class WITH_CLEANUP(Opcode):
        def __init__(self):
            super().__init__(opmap["WITH_CLEANUP"], 0)


class RETURN_VALUE(Opcode):
    def __init__(self):
        super().__init__(opmap["RETURN_VALUE"], 0)


class IMPORT_STAR(Opcode):
    def __init__(self):
        super().__init__(opmap["IMPORT_STAR"], 0)


class YIELD_VALUE(Opcode):
    def __init__(self):
        super().__init__(opmap["YIELD_VALUE"], 0)


class POP_BLOCK(Opcode):
    def __init__(self):
        super().__init__(opmap["POP_BLOCK"], 0)


if sys.version_info < (3, 9):
    class END_FINALLY(Opcode):
        def __init__(self):
            super().__init__(opmap["POP_EXCEPT"], 0)


class POP_EXCEPT(Opcode):
    def __init__(self):
        super().__init__(opmap["POP_EXCEPT"], 0)


class STORE_NAME(NameOp):
    def __init__(self, arg: str):
        super().__init__(opmap["STORE_NAME"], arg)


class DELETE_NAME(NameOp):
    def __init__(self, arg: str):
        super().__init__(opmap["DELETE_NAME"], arg)


class UNPACK_SEQUENCE(Opcode):
    def __init__(self, arg=0):
        super().__init__(opmap["UNPACK_SEQUENCE"], arg)


class FOR_ITER(RelJumpOp):
    def __init__(self, arg: 'Label'):
        super().__init__(opmap["FOR_ITER"], arg)


class UNPACK_EX(Opcode):
    def __init__(self, arg: int):
        super().__init__(opmap["UNPACK_EX"], arg)


class STORE_ATTR(NameOp):
    def __init__(self, arg: str):
        super().__init__(opmap["STORE_ATTR"], arg)


class DELETE_ATTR(NameOp):
    def __init__(self, arg: str):
        super().__init__(opmap["DELETE_ATTR"], arg)


class STORE_GLOBAL(NameOp):
    def __init__(self, arg: str):
        super().__init__(opmap["STORE_GLOBAL"], arg)


class DELETE_GLOBAL(NameOp):
    def __init__(self, arg: str):
        super().__init__(opmap["DELETE_GLOBAL"], arg)


if sys.version_info < (3, 2):
    class DUP_TOPX(Opcode):
        def __init__(self, arg: int):
            super().__init__(opmap["DUP_TOPX"], arg)


class LOAD_CONST(ConstOp):
    def __init__(self, arg: Any):
        super().__init__(opmap["LOAD_CONST"], arg)


class LOAD_NAME(NameOp):
    def __init__(self, arg: str):
        super().__init__(opmap["LOAD_NAME"], arg)


class BUILD_TUPLE(Opcode):
    def __init__(self, arg: int):
        super().__init__(opmap["BUILD_TUPLE"], arg)


class BUILD_LIST(Opcode):
    def __init__(self, arg: int):
        super().__init__(opmap["BUILD_LIST"], arg)


class BUILD_SET(Opcode):
    def __init__(self, arg: int):
        super().__init__(opmap["BUILD_SET"], arg)


class BUILD_MAP(Opcode):
    def __init__(self, arg: int):
        super().__init__(opmap["BUILD_MAP"], arg)


class LOAD_ATTR(NameOp):
    def __init__(self, arg: str):
        super().__init__(opmap["LOAD_ATTR"], arg)


class COMPARE_OP(Opcode):
    def __init__(self, arg: str):
        super().__init__(opmap["COMPARE_OP"], cmp_op.index(arg))


class IMPORT_NAME(NameOp):
    def __init__(self, arg: str):
        super().__init__(opmap["IMPORT_NAME"], arg)


class IMPORT_FROM(NameOp):
    def __init__(self, arg: str):
        super().__init__(opmap["IMPORT_FROM"], arg)


class JUMP_FORWARD(RelJumpOp):
    def __init__(self, arg: 'Label'):
        super().__init__(opmap["JUMP_FORWARD"], arg)


if sys.version_info < (3, 1):
    class JUMP_IF_FALSE(AbsJumpOp):
        def __init__(self, arg: 'Label'):
            super().__init__(opmap["JUMP_IF_FALSE"], arg)


    class JUMP_IF_TRUE(AbsJumpOp):
        def __init__(self, arg: 'Label'):
            super().__init__(opmap["JUMP_IF_TRUE"], arg)


class JUMP_ABSOLUTE(AbsJumpOp):
    def __init__(self, arg: 'Label'):
        super().__init__(opmap["JUMP_ABSOLUTE"], arg)


class LOAD_GLOBAL(NameOp):
    def __init__(self, arg: str):
        super().__init__(opmap["LOAD_GLOBAL"], arg)


if sys.version_info < (3, 8):
    class CONTINUE_LOOP(AbsJumpOp):
        def __init__(self, arg: 'Label'):
            super().__init__(opmap["CONTINUE_LOOP"], arg)


    class SETUP_LOOP(RelJumpOp):
        def __init__(self, arg: 'Label'):
            super().__init__(opmap["SETUP_LOOP"], arg)


    class SETUP_EXCEPT(RelJumpOp):
        def __init__(self, arg: 'Label'):
            super().__init__(opmap["SETUP_EXCEPT"], arg)


class SETUP_FINALLY(RelJumpOp):
    def __init__(self, arg: 'Label'):
        super().__init__(opmap["SETUP_FINALLY"], arg)


class LOAD_FAST(VarOp):
    def __init__(self, arg: str):
        super().__init__(opmap["LOAD_FAST"], arg)


class STORE_FAST(VarOp):
    def __init__(self, arg: str):
        super().__init__(opmap["STORE_FAST"], arg)


class DELETE_FAST(VarOp):
    def __init__(self, arg: str):
        super().__init__(opmap["DELETE_FAST"], arg)


class RAISE_VARARGS(Opcode):
    # TODO: Enum?
    def __init__(self, arg: int):
        super().__init__(opmap["RAISE_VARARGS"], arg)


class CALL_FUNCTION(Opcode):
    def __init__(self, arg: int = 0):
        super().__init__(opmap["CALL_FUNCTION"], arg)


class MAKE_FUNCTION(Opcode):
    # TODO: Flags utility?
    def __init__(self, arg: int):
        super().__init__(opmap["MAKE_FUNCTION"], arg)


class BUILD_SLICE(Opcode):
    def __init__(self, arg: int):
        super().__init__(opmap["BUILD_SLICE"], arg)


if sys.version_info < (3, 6):
    class MAKE_CLOSURE(Opcode):
        def __init__(self, arg: int):
            super().__init__(opmap["MAKE_CLOSURE"], arg)


class LOAD_CLOSURE(CellOp):
    def __init__(self, arg: int):
        super().__init__(opmap["LOAD_CLOSURE"], arg)


class LOAD_DEREF(CellOp):
    def __init__(self, arg: str):
        super().__init__(opmap["LOAD_DEREF"], arg)


class STORE_DEREF(CellOp):
    def __init__(self, arg: str):
        super().__init__(opmap["STORE_DEREF"], arg)


if sys.version_info < (3, 6):
    class CALL_FUNCTION_VAR(Opcode):
        def __init__(self, arg: int):
            super().__init__(opmap["CALL_FUNCTION_VAR"], arg)


class CALL_FUNCTION_KW(Opcode):
    def __init__(self, arg: int):
        super().__init__(opmap["CALL_FUNCTION_KW"], arg)


if sys.version_info < (3, 6):
    class CALL_FUNCTION_VAR_KW(Opcode):
        def __init__(self, arg: int):
            super().__init__(opmap["CALL_FUNCTION_VAR_KW"], arg)


class EXTENDED_ARG(Opcode):
    def __init__(self, arg: int):
        super().__init__(opmap["EXTENDED_ARG"], arg)
