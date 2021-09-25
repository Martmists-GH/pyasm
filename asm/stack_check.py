from opcode import opmap, hasjrel, hasjabs, stack_effect
from struct import unpack

hasbranch = [
    opmap["JUMP_IF_FALSE_OR_POP"],
    opmap["JUMP_IF_TRUE_OR_POP"],
    opmap["POP_JUMP_IF_FALSE"],
    opmap["POP_JUMP_IF_TRUE"],
    opmap["JUMP_IF_NOT_EXC_MATCH"],
]


class StackChecker:
    def __init__(self, code: bytes):
        self.code = code
        self.max = 0

    def check_offset(self, offset: int, current: int, jumped: list):
        # TODO: Support infinite loops

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

            elif op in hasjabs:
                # do jump
                n = arg - current
            elif op in hasjrel:
                # do jump
                n += arg

            if op == opmap["RETURN_VALUE"]:
                break

    def check(self):
        self.check_offset(0, 0, [])
