from opcode import opmap
from typing import TYPE_CHECKING, Any, Tuple

from asm.ops.abc import Opcode, AbsJumpOp, NameOp, MultiOp, VarOp, ConstOp

if TYPE_CHECKING:
    from asm.serializer import Label, Serializer


class BINARY_ADD_ADAPTIVE(Opcode):
    def __init__(self):
        super().__init__(opmap["BINARY_ADD_ADAPTIVE"], 0)


class BINARY_ADD_INT(Opcode):
    def __init__(self):
        super().__init__(opmap["BINARY_ADD_INT"], 0)


class BINARY_ADD_FLOAT(Opcode):
    def __init__(self):
        super().__init__(opmap["BINARY_ADD_FLOAT"], 0)


class BINARY_ADD_UNICODE(Opcode):
    def __init__(self):
        super().__init__(opmap["BINARY_ADD_UNICODE"], 0)


class BINARY_ADD_UNICODE_INPLACE_FAST(Opcode):
    def __init__(self):
        super().__init__(opmap["BINARY_ADD_UNICODE_INPLACE_FAST"], 0)


class BINARY_SUBSCR_ADAPTIVE(Opcode):
    def __init__(self):
        super().__init__(opmap["BINARY_SUBSCR_ADAPTIVE"], 0)


class PUSH_EXC_INFO(Opcode):
    def __init__(self):
        super().__init__(opmap["PUSH_EXC_INFO"], 0)


class BINARY_SUBSCR_LIST_INT(Opcode):
    def __init__(self):
        super().__init__(opmap["BINARY_SUBSCR_LIST_INT"], 0)


class POP_EXCEPT_AND_RERAISE(Opcode):
    def __init__(self):
        super().__init__(opmap["POP_EXCEPT_AND_RERAISE"], 0)


class BINARY_SUBSCR_TUPLE_INT(Opcode):
    def __init__(self):
        super().__init__(opmap["BINARY_SUBSCR_TUPLE_INT"], 0)


class BINARY_SUBSCR_DICT(Opcode):
    def __init__(self):
        super().__init__(opmap["BINARY_SUBSCR_DICT"], 0)


class JUMP_ABSOLUTE_QUICK(AbsJumpOp):
    def __init__(self, arg: 'Label'):
        super().__init__(opmap["JUMP_ABSOLUTE_QUICK"], arg)


class LOAD_ATTR_ADAPTIVE(Opcode):
    def __init__(self):
        super().__init__(opmap["LOAD_ATTR_ADAPTIVE"], 0)


class LOAD_ATTR_SPLIT_KEYS(Opcode):
    def __init__(self):
        super().__init__(opmap["LOAD_ATTR_SPLIT_KEYS"], 0)


class LOAD_ATTR_WITH_HINT(Opcode):
    def __init__(self):
        super().__init__(opmap["LOAD_ATTR_WITH_HINT"], 0)


class LOAD_ATTR_SLOT(Opcode):
    def __init__(self):
        super().__init__(opmap["LOAD_ATTR_SLOT"], 0)


class LOAD_ATTR_MODULE(Opcode):
    def __init__(self):
        super().__init__(opmap["LOAD_ATTR_MODULE"], 0)


class LOAD_GLOBAL_ADAPTIVE(NameOp):
    def __init__(self, arg: str):
        super().__init__(opmap["LOAD_GLOBAL_ADAPTIVE"], arg)


class LOAD_GLOBAL_MODULE(NameOp):
    def __init__(self, arg: str):
        super().__init__(opmap["LOAD_GLOBAL_MODULE"], arg)


class LOAD_GLOBAL_BUILTIN(NameOp):
    def __init__(self, arg: str):
        super().__init__(opmap["LOAD_GLOBAL_BUILTIN"], arg)


class BEFORE_WITH(Opcode):
    def __init__(self):
        super().__init__(opmap["BEFORE_WITH"], 0)


class LOAD_METHOD_ADAPTIVE(NameOp):
    def __init__(self, arg: str):
        super().__init__(opmap["LOAD_METHOD_ADAPTIVE"], arg)


class LOAD_METHOD_CACHED(NameOp):
    def __init__(self, arg: str):
        super().__init__(opmap["LOAD_METHOD_CACHED"], arg)


class LOAD_METHOD_CLASS(NameOp):
    def __init__(self, arg: str):
        super().__init__(opmap["LOAD_METHOD_CLASS"], arg)


class LOAD_METHOD_MODULE(NameOp):
    def __init__(self, arg: str):
        super().__init__(opmap["LOAD_METHOD_MODULE"], arg)


class STORE_ATTR_ADAPTIVE(NameOp):
    def __init__(self, arg: str):
        super().__init__(opmap["STORE_ATTR_ADAPTIVE"], arg)


class STORE_ATTR_SPLIT_KEYS(NameOp):
    def __init__(self, arg: str):
        super().__init__(opmap["STORE_ATTR_SPLIT_KEYS"], arg)


class STORE_ATTR_SLOT(NameOp):
    def __init__(self, arg: str):
        super().__init__(opmap["STORE_ATTR_SLOT"], arg)


class STORE_ATTR_WITH_HINT(NameOp):
    def __init__(self, arg: str):
        super().__init__(opmap["STORE_ATTR_WITH_HINT"], arg)


class LOAD_FAST__LOAD_FAST(MultiOp):
    def __init__(self, arg: Tuple[str, str]):
        super().__init__(opmap["LOAD_FAST__LOAD_FAST"], arg)

    def serialize_left(self, ctx: 'Serializer', arg) -> bytes:
        return VarOp(self.id, arg).serialize(ctx)

    def serialize_right(self, ctx: 'Serializer', arg) -> bytes:
        return VarOp(opmap["LOAD_FAST"], arg).serialize(ctx)


class STORE_FAST__LOAD_FAST(MultiOp):
    def __init__(self, arg: Tuple[str, str]):
        super().__init__(opmap["STORE_FAST__LOAD_FAST"], arg)

    def serialize_left(self, ctx: 'Serializer', arg) -> bytes:
        return VarOp(self.id, arg).serialize(ctx)

    def serialize_right(self, ctx: 'Serializer', arg) -> bytes:
        return VarOp(opmap["LOAD_FAST"], arg).serialize(ctx)


class LOAD_FAST__LOAD_CONST(MultiOp):
    def __init__(self, arg: Tuple[str, Any]):
        super().__init__(opmap["LOAD_FAST__LOAD_CONST"], arg)

    def serialize_left(self, ctx: 'Serializer', arg) -> bytes:
        return VarOp(self.id, arg).serialize(ctx)

    def serialize_right(self, ctx: 'Serializer', arg) -> bytes:
        return ConstOp(opmap["LOAD_CONST"], arg).serialize(ctx)


class MAKE_CELL(Opcode):
    def __init__(self):
        super().__init__(opmap["MAKE_CELL"], 0)


class LOAD_CONST__LOAD_FAST(MultiOp):
    def __init__(self, arg: Tuple[Any, str]):
        super().__init__(opmap["LOAD_CONST__LOAD_FAST"], arg)

    def serialize_left(self, ctx: 'Serializer', arg) -> bytes:
        return ConstOp(self.id, arg).serialize(ctx)

    def serialize_right(self, ctx: 'Serializer', arg) -> bytes:
        return VarOp(opmap["LOAD_FAST"], arg).serialize(ctx)


class STORE_FAST__STORE_FAST(MultiOp):
    def __init__(self, arg: Tuple[str, str]):
        super().__init__(opmap["STORE_FAST__STORE_FAST"], arg)

    def serialize_left(self, ctx: 'Serializer', arg) -> bytes:
        return VarOp(self.id, arg).serialize(ctx)

    def serialize_right(self, ctx: 'Serializer', arg) -> bytes:
        return VarOp(opmap["STORE_FAST"], arg).serialize(ctx)


class CALL_METHOD_KW(Opcode):
    def __init__(self, arg: int):
        super().__init__(opmap["CALL_METHOD_KW"], arg)
