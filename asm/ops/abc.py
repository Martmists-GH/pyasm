from dataclasses import dataclass
from struct import pack
from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from asm.serializer import Label, Serializer


@dataclass(eq=False)
class Opcode:
    id: int
    arg: object = 0

    def serialize(self, ctx: 'Serializer') -> bytes:
        return self.int_arg(self.arg)

    def int_arg(self, x: int) -> bytes:
        return pack("Bb" if x < 0 else "BB", self.id, x & 0xFF)


class JumpOp(Opcode):
    def __init__(self, id: int, arg: 'Label'):
        super().__init__(id, arg)

        arg.parents.append(self)
        self.target_index = None


class ConstOp(Opcode):
    def __init__(self, id: int, arg: Any):
        super().__init__(id, arg)

    def serialize(self, ctx: 'Serializer') -> bytes:
        from asm.serializer import code_replace

        if self.arg not in ctx.code.co_consts:
            ctx.code = code_replace(
                ctx.code,
                co_consts=ctx.code.co_consts + (self.arg,),
            )
        return self.int_arg(ctx.code.co_consts.index(self.arg))


class NameOp(Opcode):
    def __init__(self, id: int, arg: str):
        super().__init__(id, arg)

    def serialize(self, ctx: 'Serializer') -> bytes:
        from asm.serializer import code_replace

        if self.arg not in ctx.code.co_names:
            ctx.code = code_replace(
                ctx.code,
                co_names=ctx.code.co_names + (self.arg,),
            )
        return self.int_arg(ctx.code.co_names.index(self.arg))


class VarOp(Opcode):
    def __init__(self, id: int, arg: str):
        super().__init__(id, arg)

    def serialize(self, ctx: 'Serializer') -> bytes:
        from asm.serializer import code_replace

        if self.arg not in ctx.code.co_varnames:
            ctx.code = code_replace(
                ctx.code,
                co_varnames=ctx.code.co_varnames + (self.arg,),
            )
        return self.int_arg(ctx.code.co_varnames.index(self.arg))


class CellOp(Opcode):
    def __init__(self, id: int, arg: str):
        super().__init__(id, arg)

    def serialize(self, ctx: 'Serializer') -> bytes:
        if self.arg not in ctx.code.co_freevars:
            if self.arg not in ctx.code.co_cellvars:
                raise ValueError("Could not find {0} in freevars or cellvars!".format(self.arg))
            return self.int_arg(ctx.code.co_cellvars.index(self.arg))
        return self.int_arg(ctx.code.co_freevars.index(self.arg) + len(ctx.code.co_cellvars))


class AbsJumpOp(JumpOp):
    def __init__(self, id: int, arg: 'Label'):
        super().__init__(id, arg)

    def serialize(self, ctx: 'Serializer') -> bytes:
        return self.int_arg(self.arg)


class RelJumpOp(JumpOp):
    def __init__(self, id: int, arg: 'Label'):
        super().__init__(id, arg)

    def serialize(self, ctx: 'Serializer') -> bytes:
        from_index = ctx.current_index
        to_index = self.arg
        return self.int_arg(to_index - from_index)


# Used only in 3.11+
class MultiOp(Opcode):
    def __init__(self, id: int, arg: tuple):
        super().__init__(id, arg)

    def serialize(self, ctx: 'Serializer') -> bytes:
        l = self.serialize_left(ctx, self.arg[0])
        r = self.serialize_right(ctx, self.arg[1])

        return l + r

    def serialize_left(self, ctx: 'Serializer', arg) -> bytes:
        raise NotImplementedError()

    def serialize_right(self, ctx: 'Serializer', arg) -> bytes:
        raise NotImplementedError()
