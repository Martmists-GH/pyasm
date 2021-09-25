from opcode import opmap, hasjrel, hasjabs, stack_effect

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
        while offset + n < len(self.code) / 2:
            op = self.code[2*(offset + n):2*(offset + n + 1)]
            n += 1
            current += stack_effect(op[0], op[1]) if op[0] >= 90 else stack_effect(op[0])
            self.max = max(self.max, current)

            if current < 0:
                raise ValueError("Negative stack index!")

            if op[0] in hasbranch:
                new_jumped = jumped + [op[1], current+n]

                # do both branches
                if op[1] not in jumped:
                    self.check_offset(op[1], current, new_jumped)
                if current + n not in jumped:
                    self.check_offset(current + n, current, new_jumped)

            elif op[0] in hasjabs:
                # do jump
                n = op[1] - current
            elif op[0] in hasjrel:
                # do jump
                n += op[1]

            if op[0] == opmap["RETURN_VALUE"]:
                break

    def check(self):
        self.check_offset(0, 0, [])
