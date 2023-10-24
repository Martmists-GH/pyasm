from opcode import opmap
from typing import TYPE_CHECKING, Any, Tuple

from asm.ops.abc import Opcode, AbsJumpOp, NameOp, MultiOp, VarOp, ConstOp, RelJumpOp, BackRelJumpOp

if TYPE_CHECKING:
    from asm.serializer import Label, Serializer


class CACHE(Opcode):
    def __init__(self):
        super().__init__(opmap["CACHE"], 0)


class PUSH_NULL(Opcode):
    def __init__(self):
        super().__init__(opmap["PUSH_NULL"], 0)


class PUSH_EXC_INFO(Opcode):
    def __init__(self):
        super().__init__(opmap["PUSH_EXC_INFO"], 0)


class CHECK_EXC_MATCH(Opcode):
    def __init__(self):
        super().__init__(opmap["CHECK_EXC_MATCH"], 0)


class CHECK_EG_MATCH(Opcode):
    def __init__(self):
        super().__init__(opmap["CHECK_EG_MATCH"], 0)


class BEFORE_WITH(Opcode):
    def __init__(self):
        super().__init__(opmap["BEFORE_WITH"], 0)


class RETURN_GENERATOR(Opcode):
    def __init__(self):
        super().__init__(opmap["RETURN_GENERATOR"], 0)


class ASYNC_GEN_WRAP(Opcode):
    def __init__(self):
        super().__init__(opmap["ASYNC_GEN_WRAP"], 0)


class PREP_RERAISE_STAR(Opcode):
    def __init__(self):
        super().__init__(opmap["PREP_RERAISE_STAR"], 0)


class SWAP(Opcode):
    def __init__(self, arg: int):
        super().__init__(opmap["SWAP"], arg)


class POP_JUMP_FORWARD_IF_FALSE(RelJumpOp):
    def __init__(self, arg: 'Label'):
        super().__init__(opmap["POP_JUMP_FORWARD_IF_FALSE"], arg)


class POP_JUMP_FORWARD_IF_TRUE(RelJumpOp):
    def __init__(self, arg: 'Label'):
        super().__init__(opmap["POP_JUMP_FORWARD_IF_TRUE"], arg)


class COPY(Opcode):
    def __init__(self, arg: int):
        super().__init__(opmap["COPY"], arg)


class BINARY_OP(Opcode):
    # TODO: Remap op to string from _nb_ops?
    def __init__(self, arg: int):
        super().__init__(opmap["BINARY_OP"], arg)


class SEND(Opcode):
    def __init__(self):
        super().__init__(opmap["SEND"], 0)


class POP_JUMP_FORWARD_IF_NOT_NONE(RelJumpOp):
    def __init__(self, arg: 'Label'):
        super().__init__(opmap["POP_JUMP_FORWARD_IF_NOT_NONE"], arg)


class POP_JUMP_FORWARD_IF_NONE(RelJumpOp):
    def __init__(self, arg: 'Label'):
        super().__init__(opmap["POP_JUMP_FORWARD_IF_NONE"], arg)


class GET_AWAITABLE(Opcode):
    def __init__(self, arg: int):
        super().__init__(opmap["GET_AWAITABLE"], arg)


class JUMP_BACKWARD_NO_INTERRUPT(BackRelJumpOp):
    def __init__(self, arg: 'Label'):
        super().__init__(opmap["JUMP_BACKWARD_NO_INTERRUPT"], arg)


class MAKE_CELL(Opcode):
    def __init__(self, arg: int):
        super().__init__(opmap["MAKE_CELL"], arg)


class JUMP_BACKWARD(BackRelJumpOp):
    def __init__(self, arg: 'Label'):
        super().__init__(opmap["JUMP_BACKWARD"], arg)


class COPY_FREE_VARS(Opcode):
    def __init__(self, arg: int):
        super().__init__(opmap["COPY_FREE_VARS"], arg)


class RESUME(Opcode):
    def __init__(self, arg: int):
        super().__init__(opmap["RESUME"], arg)


class PRECALL(Opcode):
    def __init__(self, arg: int = 0):
        super().__init__(opmap["PRECALL"], arg)


class CALL(Opcode):
    def __init__(self, arg: int = 0):
        super().__init__(opmap["CALL"], arg)


class KW_NAMES(ConstOp):
    def __init__(self, arg: int):
        super().__init__(opmap["KW_NAMES"], arg)


class POP_JUMP_BACKWARD_IF_NOT_NONE(BackRelJumpOp):
    def __init__(self, arg: 'Label'):
        super().__init__(opmap["POP_JUMP_BACKWARD_IF_NOT_NONE"], arg)


class POP_JUMP_BACKWARD_IF_NONE(BackRelJumpOp):
    def __init__(self, arg: 'Label'):
        super().__init__(opmap["POP_JUMP_BACKWARD_IF_NONE"], arg)


class POP_JUMP_BACKWARD_IF_FALSE(BackRelJumpOp):
    def __init__(self, arg: 'Label'):
        super().__init__(opmap["POP_JUMP_BACKWARD_IF_FALSE"], arg)


class POP_JUMP_BACKWARD_IF_TRUE(BackRelJumpOp):
    def __init__(self, arg: 'Label'):
        super().__init__(opmap["POP_JUMP_BACKWARD_IF_TRUE"], arg)
