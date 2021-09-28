from opcode import opmap, hasjrel, hasjabs, stack_effect
from struct import unpack

hasbranch = [
    opmap.get("JUMP_IF_FALSE_OR_POP"),
    opmap.get("JUMP_IF_TRUE_OR_POP"),
    opmap.get("POP_JUMP_IF_FALSE"),
    opmap.get("POP_JUMP_IF_TRUE"),
    opmap.get("JUMP_IF_NOT_EXC_MATCH"),
]


class StackChecker:
    def __init__(self, code: bytes):
        self.code = code
        self.max = 0

    def check_offset(self, offset: int, current: int, jumped: list):
        n = 0
        while 2 * (offset + n) < len(self.code):
            op = self.code[2 * (offset + n):]
            op, arg = unpack("BB", op[:2])
            n += 1
            current += stack_effect(op, arg) if op >= 90 else stack_effect(op)
            self.max = max(self.max, current)

            # TODO: Something still goes wrong here
            # if current < 0:
            #     raise ValueError("Negative stack index!")

            if op in hasbranch:
                new_jumped = jumped + [arg, current + n]

                # do both branches
                if arg not in jumped:
                    self.check_offset(arg, current, new_jumped)
                if current + n not in jumped:
                    self.check_offset(current + n, current, new_jumped)
                return

            elif op in hasjabs and arg not in jumped:
                # do jump
                self.check_offset(arg, current, jumped + [arg])
                return
            elif op in hasjrel and offset + n + arg not in jumped:
                # do jump
                self.check_offset(offset + n + arg, current, jumped + [offset + n + arg])
                return

            if op == opmap["RETURN_VALUE"]:
                break

    def check(self):
        self.check_offset(0, 0, [])
