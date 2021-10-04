from dis import _unpack_opargs
from opcode import hasjrel, hasjabs, hasconst, hasname, haslocal, cmp_op, hascompare, hasfree
from types import CodeType
from typing import List, Union

from asm.ops import Opcode, ALL_OPS, MultiOp
from asm.stack_check import StackChecker


class Label:
    def __init__(self):
        self.parents: List[Opcode] = []

    def set(self, index: int):
        for p in self.parents:
            p.arg = int(index / 2)

    def __repr__(self):
        return "Label({0})".format(hex(id(self)))


class Deserializer:
    def __init__(self, code: CodeType):
        self.code = code

    def find_labels(self) -> List[int]:
        lbls = []
        for (i, op, arg) in _unpack_opargs(self.code.co_code):
            if op in hasjrel:
                idx = i + arg * 2
                if idx not in lbls:
                    lbls.append(idx)
            elif op in hasjabs:
                if arg * 2 not in lbls:
                    lbls.append(arg * 2)
        return lbls

    def deserialize(self) -> List[Union[Opcode, Label]]:
        labels = sorted(self.find_labels())
        label_objs = {it: Label() for it in labels}
        elements = []
        waiting_element = None
        for (i, op, arg) in _unpack_opargs(self.code.co_code):
            cls = ALL_OPS[op]

            for k, l in label_objs.items():
                if i == k:
                    elements.append(l)
                    break

            if op in hasconst:
                arg = self.code.co_consts[arg]
            elif op in hasname:
                arg = self.code.co_names[arg]
            elif op in haslocal:
                arg = self.code.co_varnames[arg]
            elif op in hascompare:
                arg = cmp_op[arg]
            elif op in hasfree:
                n = len(self.code.co_cellvars)
                if arg < n:
                    arg = self.code.co_cellvars[arg]
                else:
                    arg = self.code.co_freevars[arg - n]
            elif op in hasjabs:
                arg = label_objs[arg * 2]
            elif op in hasjrel:
                arg = label_objs[i + arg * 2]

            if op < 90:
                x = cls()
            else:
                x = cls(arg)

            if waiting_element is not None:
                x, waiting_element = waiting_element, None
                x.arg = (x.arg, arg)

            if issubclass(cls, MultiOp):
                waiting_element = x
            else:
                elements.append(x)

        return elements


class Serializer:
    def __init__(self, ops: List[Union[Opcode, Label]], code: CodeType):
        self.ops = ops
        self.current_index = 0
        self.code = code

    @staticmethod
    def calculate_stack(code: bytes) -> int:
        checker = StackChecker(code)
        checker.check()
        return checker.max

    def serialize(self) -> CodeType:
        self.current_index = 0

        for x in self.ops:
            if not isinstance(x, Label):
                self.current_index += 2
                if isinstance(x, MultiOp):
                    self.current_index += 2  # Offset 2 more
            else:
                x.set(self.current_index)

        data = b""

        self.current_index = 0
        for x in self.ops:
            if isinstance(x, Opcode):
                data += x.serialize(self)
                self.current_index += 2
                if isinstance(x, MultiOp):
                    self.current_index += 2  # Offset 2 more

        self.code = self.code.replace(co_code=data,
                                      co_stacksize=self.calculate_stack(data),
                                      co_nlocals=len(self.code.co_varnames))
        return self.code
